import board_settings

print(__name__+": Entered main_mode")
import ujson
import board
import mc_server_protocol
import settings
import network
try:
    import usocket as socket
    print(__name__+": Using usocket")
except:
    import socket
    print(__name__ + ": Using socket")
import utime, ntptime
from PID import PID
import select
broadcast_ip=None
sensoring_interval=2
networking_interval=10
sensoring_time=0
networking_time=0
is_file_in_use=False
is_local=False
is_on = True
server_url = "localhost:8000"
temp_pid=PID(1,0.02,0.3,settings.target_temperature,sample_time = 2)
humidity_pid=PID(0.5,0.03,0.3,settings.target_temperature,sample_time = 2)

def sensoring_routine():
    global is_on, is_file_in_use, sensoring_time
    time=utime.time()
    if time-sensoring_time>sensoring_interval:
        data = board.get_sensors_data()
        t_c=temp_pid(data["temp_c"])
        board.set_heater_state(t_c> 0)
        h_c=humidity_pid(data["humidity"])
        board.set_pulverizer_state( h_c> 0)
        lights_on=settings.start_time <= utime.localtime()[3] <= settings.end_time
        board.set_lights_state(lights_on)
        data["time"]=utime.localtime(board.get_real_time_s(time))[3:6]
        while(is_file_in_use):
            pass
        is_file_in_use=True
        outfile= open("telemetry_json.txt", "w")
        outfile.write(board.get_telemetry_jstring(data))
        outfile.close()
        is_file_in_use=False
        sensoring_time=time
        board_settings.debug_pin.on()
        utime.sleep_ms(700)
        board_settings.debug_pin.off()
        print(data)

def get_broadcst_ip(ip,mask):
    ip = [int(i) for i in ip.split('.')]
    mask = [int(i) for i in mask.split('.')]
    return '.'.join([str((ioctet | ~moctet) & 0xff) for ioctet, moctet in zip(ip, mask)])

def apply_data(data):
    changed=False
    if "date" in data:
        time=data["time"]
    else:
        time=None
    if "mc_settings" in data:
        changed=True
        for k,v in data["mc_settings"].items():
            settings.data["mc_settings"][k]=v
        if time:
            settings.data["date"]=time
        else:
            settings.data["date"]=board.get_real_time_s(utime.time())

    if "climate_settings" in data:
        print(data["climate_settings"])
        for k, v in data["climate_settings"].items():
            print(k,v)
            settings.data["climate_settings"][k] = v
        if time:
            settings.data["date"] = time
        else:
            settings.data["date"] = board.get_real_time_s(utime.time())
        changed=True

    if changed:
        settings.rewrite_settings_file()
        settings.reassign_data()

def acces_port_mode(wifi):

    pass

def local_net_mode(wifi):
    global is_file_in_use
    print(__name__+": Creating receive sock")
    receive_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receive_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(__name__ + ": Binding receive sock")
    receive_sock.bind(('', 12345))
    receive_sock.listen(2)
    print(__name__ + ": Creating poll")
    p = select.poll()
    p.register(receive_sock)
    print(__name__ + ": Creating broadcast sock")
    broadcast_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    broadcast_sock.settimeout(0.2)
    ip=wifi.ifconfig()[0]
    message = bytes(ip,'ASCII')
    print(__name__ + ": Sending broadcast to "+broadcast_ip)
    broadcast_sock.sendto(message, (broadcast_ip, 37020))
    print(__name__ + ": Broadcast sent")
    r = p.poll(2000)
    if len(r) > 0:
        print(__name__ + ": Poll event")
        conn, addr = receive_sock.accept()
        if r[0][1] & select.POLLIN:
            print(__name__ + ": Receiveing from sock")
            strdata = str(conn.recv(1024))[2:-1]
            try:
                print(__name__ + ": Parsing received data")
                data=ujson.loads(strdata)
                print(__name__ + ": Applying received data")
                apply_data(data)
            except:
                print(__name__ + ": Exception in parsing "+strdata)
        #if r[0][1] & select.POLLOUT:
            print(__name__ + ": Sending data")
            while (is_file_in_use):
                pass
            is_file_in_use = True
            print(__name__ + ": File reading")
            outfile = open("telemetry_json.txt", "r")
            data = outfile.read()
            outfile.close()
            is_file_in_use = False
            conn.write(bytes(data,'ASCII'))
            print(__name__ + ": Data sent")
        print(__name__ + ": Closing connection")
        conn.close()
        del conn
    print(__name__+": Closing sockets")
    p.unregister(receive_sock)
    del p
    receive_sock.close()
    broadcast_sock.close()
    del receive_sock
    del broadcast_sock

def networking_routine(wifi):
    global is_on, server_url,is_file_in_use,networking_time,is_local
    time=utime.time()
    if time-networking_time>networking_interval:
        print(__name__+": Checking internet connection")
        if mc_server_protocol.check_connection():
            print(__name__+": Have connection")
            while (is_file_in_use):
                pass
            is_file_in_use=True
            t_file= open("telemetry_json.txt", "r")
            mc_server_protocol.send_telemetry(ujson.load(t_file))
            t_file.close()
            is_file_in_use=False
        else:
            if wifi.isconnected():
                print(__name__ + ": No connection")
                local_net_mode(wifi)
            else:
                pass
        networking_time=time


def enter():
    global broadcast_ip,is_local
    wifi=network.WLAN(network.STA_IF)
    wifi.active(True)
    while not wifi.active():
        pass
    print(__name__ + ": Activated Wi-Fi adapter")
    wifi.connect(settings.wifi_ssid, settings.wifi_password)
    timeout=0
    while not wifi.isconnected():
        if timeout>100:
            print(__name__+": Failed to connect")
            wifi=network.WLAN(network.AP_IF)
            wifi.active(True)
            wifi.config(essid = 'KiposModuleWiFi', password = "")
            is_local=True
            break
        utime.sleep_ms(200)
        timeout+=1
    if ~is_local:
        print(__name__ + ": Wi-Fi connected")
        configs=wifi.ifconfig()
        broadcast_ip=get_broadcst_ip(configs[2],configs[1])
        print(__name__+": Try setting time")
        try:
            ntptime.settime()
        except:
            print(__name__ + ": Exception in setting real time")
        print(__name__ + ": Time set")
    while is_on:
        sensoring_routine()
        if is_local:
            acces_port_mode(wifi)
        else:
            networking_routine(wifi)
        utime.sleep_ms(500)

def leave():
    is_on=False
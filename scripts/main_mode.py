import board_settings

print(__name__ + ": Entered main_mode")
import ujson
import board
import mc_server_protocol
import settings
import network

try:
    import usocket as socket

    print(__name__ + ": Using usocket")
except:
    import socket

    print(__name__ + ": Using socket")
import utime, ntptime
from PID import PID
import select

wifi = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid = 'KiposModuleWiFi', password = "")
ap.active(False)
broadcast_ip = None
sensoring_interval = 2
networking_interval = 10
sensoring_time = 0
networking_time = 0
is_file_in_use = False
is_local_mode = False
is_in_access_mode = False
is_on = True
server_url = "localhost:8000"
temp_pid = PID(1, 0.02, 0.3, settings.target_temperature, sample_time = 2)
humidity_pid = PID(0.5, 0.03, 0.3, settings.target_temperature, sample_time = 2)


def sensoring_routine():
    global is_on, is_file_in_use, sensoring_time
    time = utime.time()
    if time - sensoring_time > sensoring_interval:
        print(__name__ + ": Sensoring")
        data = board.get_sensors_data()
        print(__name__ + ": Sensors data: {}".format(data))
        t_c = temp_pid(data["temp_c"])
        board.set_heater_state(t_c > 0)
        h_c = humidity_pid(data["humidity"])
        board.set_pulverizer_state(h_c > 0)
        lights_on = settings.start_time <= utime.localtime()[3] <= settings.end_time
        board.set_lights_state(lights_on)
        data["time"] = time
        while (is_file_in_use):
            pass
        is_file_in_use = True
        outfile = open("telemetry_json.txt", "w")
        outfile.write(ujson.dumps(data))
        outfile.close()
        is_file_in_use = False
        sensoring_time = time
        board_settings.debug_pin.on()
        utime.sleep_ms(700)
        board_settings.debug_pin.off()


def get_broadcst_ip(wifi):
    configs = wifi.ifconfig()
    ip = [int(i) for i in configs[2].split('.')]
    mask = [int(i) for i in configs[1].split('.')]
    return '.'.join([str((ioctet | ~moctet) & 0xff) for ioctet, moctet in zip(ip, mask)])


def apply_data(data):
    print(__name__ + ": Applying received data")

    file_changed = False
    need_restart = False

    if "last_update_time" not in data:
        print(__name__ + ": Time were not provided")
        return
    time = data["last_update_time"]

    if time <= settings.last_update_time:
        print(__name__ + ": Data is out of date")
        return

    if "mc_settings" in data:
        need_restart = True
        file_changed = True
        for k in data["mc_settings"]:
            settings.data["mc_settings"][k] = data["mc_settings"][k]

    if "climate_settings" in data:
        for k in data["climate_settings"]:
            settings.data["climate_settings"][k] = data["climate_settings"][k]
        file_changed = True

    if "uuid" in data:
        settings.uuid = data["uuid"]
        file_changed = True

    if file_changed:
        settings.data["last_update_time"] = time
        settings.rewrite_settings_file()
        settings.reassign_data()
    if need_restart:
        leave()


def local_net_mode(wifi):
    global is_file_in_use
    print(__name__ + ": Creating receive sock")
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
    broadcast_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    broadcast_sock.settimeout(0.2)
    ip = wifi.ifconfig()[0]
    message = bytes(ip, 'ASCII')
    ip = get_broadcst_ip(wifi)
    print(__name__ + ": Sending broadcast to " + ip)
    broadcast_sock.sendto(message, (ip, 37020))
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
                data = ujson.loads(strdata)
                apply_data(data)
            except:
                print(__name__ + ": Exception in parsing " + strdata)
            print(__name__ + ": Sending data")
            try:
                while (is_file_in_use):
                    pass
                is_file_in_use = True
                print(__name__ + ": File reading")
                outfile = open("telemetry_json.txt")
                data = ujson.load(outfile)
                outfile.close()
                is_file_in_use = False
                conn.write(bytes(ujson.dumps(board.get_telemetry(data)), 'ASCII'))
                print(__name__ + ": Data sent")
            except Exception as e:
                print(__name__+": Exception in sending data "+str(e))
        print(__name__ + ": Closing connection")
        conn.close()
        del conn
    print(__name__ + ": Closing sockets")
    p.unregister(receive_sock)
    del p
    receive_sock.close()
    broadcast_sock.close()
    del receive_sock
    del broadcast_sock


def networking_routine():
    global is_on, server_url, is_file_in_use, networking_time, is_local_mode, is_in_access_mode, wifi, ap
    time = utime.time()
    if time - networking_time > networking_interval:
        print(__name__ + ": Checking internet connection")
        try:
            if ~is_in_access_mode and settings.uuid != -1 and mc_server_protocol.check_connection():
                is_local_mode = False
                print(__name__ + ": Have connection")
                while is_file_in_use:
                    pass
                is_file_in_use = True
                t_file = open("telemetry_json.txt")
                data = ujson.load(t_file)
                t_file.close()
                is_file_in_use = False
                print(__name__+": Sending data to server")
                response = mc_server_protocol.send_telemetry(board.get_telemetry(data))
                apply_data(response.json())
            else:
                print(__name__ + ": Can't establish connection to server")
                if wifi.isconnected():
                    ap.active(False)
                    is_local_mode = True
                    is_in_access_mode = False
                else:
                    is_in_access_mode = True
                    is_local_mode = True
                    ap.active(True)

            if is_local_mode:
                if is_in_access_mode:
                    print(__name__ + ": Using access mode")
                    local_net_mode(ap)
                else:
                    print(__name__ + ": Using local network")
                    local_net_mode(wifi)
        except Exception as e:
            print(__name__ + ": " + str(e))
        finally:
            networking_time = time


def enter():
    global broadcast_ip, is_local_mode, is_in_access_mode, wifi, ap
    if settings.wifi_ssid != None:
        wifi.active(True)
        while not wifi.active():
            pass
        print(__name__ + ": Activated Wi-Fi adapter")
        wifi.connect(settings.wifi_ssid, settings.wifi_password)
        timeout = 0
        while not wifi.isconnected():
            if timeout > 100:
                print(__name__ + ": Failed to connect")
                ap.active(True)
                is_in_access_mode = True
                break
            utime.sleep_ms(200)
            timeout += 1
        print(__name__ + ": Wi-Fi connected")
        print(__name__ + ": Try setting time")
        try:
            ntptime.settime()
            print(__name__ + ": Time set")
        except:
            print(__name__ + ": Exception in setting real time")
    else:
        is_in_access_mode = True
    while is_on:
        sensoring_routine()
        networking_routine()
        utime.sleep_ms(500)


def leave():
    global is_on
    is_on = False

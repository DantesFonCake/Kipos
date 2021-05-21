import network
import ujson
import settings
try:
    import usocket as socket
    print(__name__+": Using usocket")
except:
    import socket
    print(__name__ + ": Using socket")
def enter():
    print(__name__ + ": Entered initialization_mode")
    ssid="ModuleInitializationWiFi"
    w=network.WLAN(network.AP_IF)
    w.active(True)
    w.config(essid=ssid,password="")
    print(__name__ + ": Starting wi-fi")
    while not w.active():
        pass
    print(__name__ + ": Started wi-fi at "+repr(w.ifconfig()))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    print(__name__ + ": Socket bound")
    s.listen(5)
    print(__name__ + ": Started listening")
    while True:
        conn, addr = s.accept()
        print(__name__ + ": Received connection")
        print(__name__ + ": Try receiving data")
        try:
            data=conn.recv(1024)
            print(__name__ + ": Data received")
            data_string=repr(data)[2:-1]
            print(__name__ + ": Try parsing data")
            try:
                new_settings = ujson.loads(data_string)
                print(__name__ + ": Data parsed")
                if "ssid" in new_settings and "password" in new_settings and "name" in new_settings and "time_zone" in new_settings:
                    print(__name__ + ": Setting init-settings")
                    settings.set_initialization_settings(new_settings["name"],
                                                         new_settings["ssid"],
                                                         new_settings["password"],
                                                         new_settings["time_zone"])
                    conn.close()
                    break
            except:
                print(__name__ + ": Data parsing exception")
        except:
            print(__name__ + ": Data receiving exception")
    print(__name__ + ": Leaving initialization_mode")
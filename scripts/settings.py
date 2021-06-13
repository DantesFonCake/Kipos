import ujson

last_update_time=None
initialized=False
timezone=0
wifi_ssid=None
wifi_password=None
module_name=None
target_temperature = 35
target_humidity = 95
start_time = 7
end_time = 21
file_changed = False
uuid = -1
data = {}

def rewrite_settings_file():
    print(__name__ + ": Started rewriting settings file")
    s= open("settings_json.txt", "w")
    ujson.dump(data, s)
    s.close()
    print(__name__ + ": Rewrote settings file")


def on_boot():
    print(__name__ + ": Settings boot started")
    reassign_data()


def reassign_data():
    global target_humidity, target_temperature, start_time, end_time, \
        file_changed, data, uuid, initialized, wifi_ssid, \
        wifi_password, module_name, timezone, last_update_time
    print(__name__ + ": Settings file reading")
    s = open("settings_json.txt", "r")
    data = ujson.load(s)
    s.close()
    print(__name__ + ": Settings file read")
    wifi_ssid = data["mc_settings"].get("ssid",None)
    wifi_password = data["mc_settings"].get("password",None)
    module_name = data["mc_settings"].get("name","Module")
    timezone = int(data["mc_settings"].get("time_zone",0))
    target_temperature = data["climate_settings"].get("target_temperature",30)
    target_humidity = data["climate_settings"].get("target_humidity",90)
    start_time = data["climate_settings"].get("start_time",7)
    end_time = data["climate_settings"].get("end_time",22)
    last_update_time=int(data.get("last_update_time",0))
    print(__name__ + ": Settings boot ended")


if file_changed:
    rewrite_settings_file()


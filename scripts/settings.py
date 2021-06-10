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

def set_initialization_settings(name:str, ssid:str,password:str,tz:int):
    global data,wifi_ssid,wifi_password,module_name,initialized,timezone
    data["mc_settings"]["name"] = name
    data["mc_settings"]["ssid"]=ssid
    data["mc_settings"]["password"]=password
    data["mc_settings"]["time_zone"] = tz
    data["mc_settings"]["initialized"]=True
    initialized=True
    timezone=tz
    module_name=name
    wifi_ssid=ssid
    wifi_password=password
    rewrite_settings_file()

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
    initialized = data["mc_settings"]["initialized"]
    if initialized:
        wifi_ssid = data["mc_settings"]["ssid"]
        wifi_password = data["mc_settings"]["password"]
        module_name = data["mc_settings"]["name"]
        timezone = int(data["mc_settings"]["time_zone"])
    target_temperature = data["climate_settings"]["target_temperature"]
    target_humidity = data["climate_settings"]["target_humidity"]
    start_time = data["climate_settings"]["start_time"]
    end_time = data["climate_settings"]["end_time"]
    if "last_update_time" in data:
        last_update_time=int(data["last_update_time"])
    print(__name__ + ": Settings boot ended")


if file_changed:
    rewrite_settings_file()


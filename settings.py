import json,uuid
target_temperature=35
target_humidity=95
start_time=7
end_time=21
file_changed=False
with open("settings_json","r") as s:
    data=json.load(s)
    if not data["mc_settings"]["have_uuid"]:
        data["mc_settings"]["have_uuid"]=True
        data["mc_settings"]["uuid"]=10000
        file_changed=True
    target_temperature=data["climate_settings"]["target_temperature"]
    target_humidity =data["climate_settings"]["target_humidity"]
    start_time =data["climate_settings"]["start_time"]
    end_time=data["climate_settings"]["end_time"]

if file_changed:
    with open("settings_json", "w") as s:
        json.dump(data,s)

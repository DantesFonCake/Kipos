import json
import random
import board_settings

board_initialized=False

# TODO
def set_up():
    global board_initialized
    if not board_initialized:
        board_initialized=True

# TODO
def get_sensors_data():
    count = 0
    humidity_sum = 0
    temperature_sum=0
    for humidity_sensor in board_settings.sensors_pin_list:
        data=humidity_sensor.read()
        humidity_sum += data["humidity"]
        temperature_sum+=data["temp_c"]
        count+=1
    return humidity_sum / count


# TODO put it in to get_sensors_data
def read_water_level():
    return random.random()


# TODO put it in to get_sensors_data
def read_concentrate_level():
    return random.random()

def set_pulverizer_state(state):
    if state:
        board_settings.pulverizer_out_pin.on()
    else:
        board_settings.pulverizer_out_pin.off()

def set_heater_state(state):
    if state:
        board_settings.heater_out_pin.on()
    else:
        board_settings.heater_out_pin.off()

def set_lights_state(state):
    if state:
        board_settings.lights_out_pin.on()
    else:
        board_settings.lights_out_pin.off()

def get_telemetry_jstring(data=None):
    if(data==None):
        data=get_sensors_data()
    return json.dumps(
            {"temperature"      : data["temp_c"], "humidity": data["humidity"], "water_level": read_water_level(),
             "concentrate_level": read_concentrate_level()})


set_up()

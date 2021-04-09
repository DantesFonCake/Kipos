import json
import random
import board_settings

# TODO
def set_up():
    pass


# TODO
def read_temperature():
    count=0
    temp_sum=0
    for temp_sensor in board_settings.sensors_pin_list:
        temp_sum+=temp_sensor.read()["temp_c"]
    return temp_sum/count


# TODO
def read_humidity():
    count = 0
    humidity_sum = 0
    for humidity_sensor in board_settings.sensors_pin_list:
        humidity_sum += humidity_sensor.read()["humidity"]
    return humidity_sum / count


# TODO
def read_water_level():
    return random.random()


# TODO
def read_concentrate_level():
    return random.random()


# TODO
def set_pulverizer_state(state):
    if state:
        board_settings.pulverizer_out_pin.on()
    else:
        board_settings.pulverizer_out_pin.off()


# TODO
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


def get_telemtry_jstring():
    return json.dumps(
            {"temperature"      : read_temperature(), "humidity": read_humidity(), "water_level": read_water_level(),
             "concentrate_level": read_concentrate_level()})


set_up()

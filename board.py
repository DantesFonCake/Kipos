import json
import random


# TODO
def set_up():
    pass


# TODO
def read_temperature():
    return random.random() * 50


# TODO
def read_humidity():
    return random.random() * 100


# TODO
def read_water_level():
    return random.random()


# TODO
def read_concentrate_level():
    return random.random()


# TODO
def set_pulverizer_state(state):
    pass


# TODO
def set_heater_state(state):
    pass


def get_telemtry_jstring():
    return json.dumps(
            {"temperature"      : read_temperature(), "humidity": read_humidity(), "water_level": read_water_level(),
             "concentrate_level": read_concentrate_level()})


set_up()

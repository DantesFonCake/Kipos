print("importing board")

import ujson
import board_settings
print("import b_settings")
import settings
print("import settings")

board_initialized = False

# TODO
def set_up():
    global board_initialized
    if not board_initialized:
        board_initialized = True

def get_real_time_s(s):
    if settings.timezone!=None:
        return s + settings.timezone * 3600
    return s

# TODO
def get_sensors_data():
    count = 0
    humidity_sum = 0
    temperature_sum = 0
    for sensor in board_settings.sensors_pin_list:
        try:
            sensor.measure()
            humidity_sum += sensor.humidity()
            temperature_sum += sensor.temperature()

        except:
            humidity_sum+=0
            temperature_sum+=0
        count += 1
    return {'temp_c':temperature_sum/count,'humidity':humidity_sum / count}


# TODO put it in to get_sensors_data
def read_water_level():
    pass


# TODO put it in to get_sensors_data
def read_concentrate_level():
    pass


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


def get_telemetry_jstring(data = None):
    if data is None:
        data = get_sensors_data()
    return ujson.dumps(
            {"telemetry":
                 {"temperature"      : data["temp_c"], "humidity": data["humidity"], "water_level": read_water_level(),
                  "concentrate_level": read_concentrate_level()},
             "uuid"     : settings.uuid})


set_up()

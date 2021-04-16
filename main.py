import settings, time, threading
#import board
from datetime import datetime
from simple_pid import PID

temp_pid=PID(1,0.02,0.3,settings.target_temperature,sample_time = 1)
humidity_pid=PID(0.5,0.03,0.3,settings.target_temperature,sample_time = 1)
is_on=True


def sensoring_thread():
    global is_on
    while is_on:
        #data=board.get_sensors_data()
        #board.set_heater_state(temp_pid(data["temp_c"])>0)
        #board.set_pulverizer_state(humidity_pid(data["humidity"])>0)
        #board.set_lights_state(settings.start_time <= datetime.now().hour <= settings.end_time)
        #with open("telemetry_json", "w") as outfile:
        #    outfile.write(board.get_telemetry_jstring(data))
        time.sleep(1)

def networking_thread():
    global is_on, server_url
    while is_on:

        time.sleep(10)

if __name__ == '__main__':
    sensoring = threading.Thread(target = sensoring_thread)
    sensoring.start()


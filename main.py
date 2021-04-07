import board, settings, time, threading

settings = settings.Settings()


def sensoring_thread():
    while True:
        temp = board.read_temperature()
        if temp < settings.target_temperature - 5:
            board.set_heater_state(True)
        elif temp >= settings.target_temperature:
            board.set_heater_state(False)
        humidity = board.read_humidity()
        if humidity < settings.target_humidity - 5:
            board.set_pulverizer_state(True)
        elif humidity >= settings.target_humidity:
            board.set_pulverizer_state(False)
        print(board.get_telemtry_jstring())
        time.sleep(1)


if __name__ == '__main__':
    sensoring = threading.Thread(target = sensoring_thread)
    sensoring.start()

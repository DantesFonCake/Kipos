import json
class Settings:
    def __init__(self):
        self.target_temperature=30
        self.target_humidity=95
        self.start_time=7
        self.end_time=21
    def get_jstring(self):
        return json.dumps(self.__dict__)

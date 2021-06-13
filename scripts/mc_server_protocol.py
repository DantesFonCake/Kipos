import  requests
import settings
server_url = 'http://192.168.0.6:8080/kipos'


def send_telemetry(data):
    if data is not None:
        return requests.post(server_url + "/module/update", json = data)


def get_settings():
    return requests.get(server_url + "/module/settings", args = "")


def check_connection():
    try:
        resp=requests.post(server_url+"/connection_check",json={"uuid":settings.uuid})
        answer=resp.content
        return bool(answer)
    except Exception:
        return False

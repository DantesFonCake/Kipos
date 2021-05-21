import  requests

server_url = 'http://kipos.com'


def send_telemetry(data):
    pass
    #if data is not None:
        #return requests.post(server_url + "/module/telemetry_update", data = data)


def get_settings():
    return requests.get(server_url + "/module/settings", args = "")


def check_connection():
    host='kipos.com'
    port =80
    try:
        resp=requests.get(server_url+'/check_connection')
        resp.close()
        return resp.status_code<400
    except Exception:
        return False

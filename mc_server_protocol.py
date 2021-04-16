import requests, board
server_url="http://kipos.com"
def send_telemetry(data):
    if data!=None:
        return requests.post(server_url+"/module/telemetry_update",data=data,args="")

def get_settings():
    return requests.get(server_url+"/module/settings",args="")

def check_connection():
    return requests.get(server_url+"/connection_check")
from machine import Pin
from pigpio_dht import DHT22
sensors_pin_list=[DHT22(0),DHT22(2),DHT22(4)]
heater_out_pin=Pin(5,Pin.OUT,value=0)
pulverizer_out_pin=Pin(6,Pin.OUT,value=0)
lights_out_pin=Pin(7,Pin.OUT,value=0)
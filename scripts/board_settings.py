print("importing machine")

from machine import Pin
print("importing dht")
def reset_callback(pin):
    import main_mode
    main_mode.leave()

import dht
print("imported dht")
s1=dht.DHT22(Pin(4))
print("created dht1")
s2=dht.DHT22(Pin(5))
print("created dht2")
s3=dht.DHT22(Pin(12))
print("created dht3")
sensors_pin_list = (s1, s2, )
print("sensor list created")
heater_out_pin = Pin(13, Pin.OUT, value = 0)
print("heater out pin created")
pulverizer_out_pin = Pin(14, Pin.OUT, value = 0)
print("pulverizer out pin created")
lights_out_pin = Pin(15, Pin.OUT, value = 0)
print("lights out pin created")
reset_interrupt_pin=Pin(25,Pin.IN,Pin.PULL_UP)
reset_interrupt_pin.irq(reset_callback,Pin.IRQ_FALLING)

debug_pin=Pin(2,Pin.OUT,value = 0)

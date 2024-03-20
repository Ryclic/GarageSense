from machine import Pin
from internet import connect_internet
from update import send_update
from debug import blink
import time
import os
import json
import urequests

# Debug information
print(os.uname())
board_led = Pin("LED", Pin.OUT, value=0)
# Setup internet
connect_internet()
blink(board_led, 3)
# Setup GPIO and LED pins
interval = 0.5 
state = None
magnet = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT)
# Main loop
for i in range(0, 10):
    send_update(str(i))
    time.sleep(2)



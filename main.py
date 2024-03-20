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
send_update("Raspberry Pi connected")
# Setup GPIO and LED pins
interval = 0.5 
state = None
magnet = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT)
# Main loop
while True:
    old_state = state
    state = magnet.value()

    if state == 0:
        if old_state != state and old_state != None:
            print('Contact!')
            led.on()
            send_update("Garage door closed!")
    elif state == 1:
        if old_state != state and old_state != None:
            print('No contact!')
            led.off()
            send_update("Garage door opened!")
    time.sleep(interval)


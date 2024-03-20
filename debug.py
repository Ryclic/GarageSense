import time

def blink(led, blink_num):
    for i in range(blink_num):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

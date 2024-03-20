import network
import time

def connect_internet():
    ssid = "REDACTED"
    password = "REDACTED"
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    max_wait = 20
    while max_wait > 0:
      if wlan.status() < 0 or wlan.status() >= 3:
        break
      max_wait -= 1
      print('Waiting for connection...')
      time.sleep(1)

    if wlan.status() != 3:
       print(wlan.status())
       raise RuntimeError('Network connection failed!')
    else:
      print('Connected: ' + str(wlan.status()))
      status = wlan.ifconfig()

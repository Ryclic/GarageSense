import urequests
import time

def send_update(update):
    url = "https://api.pushover.net/1/messages.json"
    data = {
        "token": "REDACTED",
        "user": "REDACTED",
        "message": update
    }
    req = urequests.post(url, json=data)
    print("Update Response: " + str(req.status_code))
    req.close()
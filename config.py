import ujson as json

config = {}

print("## Loading the configuration")
try:
    with open("/config.json") as f:
        print(" - Reading /config.json")
        config = json.loads(f.read())
except Exception as inst:
    print(" - **Abort Abort** _Config load exception_")
    time.sleep(5)
    print(type(inst))
    print(inst.args)
    print(inst)
except (OSError, ValueError):
    print(" - Crap!! The file is broken, or missing (/config.json)")

# The config data defined below should be stored in /config.json
"""
{
    "wifi": {
        "ssid": "<MY-SSID>",
        "password": "<MY-PASSWORD>"
    },
    "mqtt": {
        "broker": "<mqtt_hostname>",
        "username": "<mqtt_username>",
        "password": "<mqtt_password>",
        "client": "<client_id>",
        "topics": {
            # pub: Can use #client# #topic# #username# (eg. /weather/#client#/#topic#)
            "pub": "<topic_pub>", 
            # As above but this only listens for configs ATM (eg. /weather/#client#/config)
            "sub": "<topic_sub>",
        }
    },
    "sleep": {
        "duration": 10, # The sleep duration
        "delay": 2 # The time between finishing up and going to sleep
    }
}
"""

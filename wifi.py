import config
import network
import time

def connect():
	print("## Wifi configuration")
	try:
		sta_if = network.WLAN(network.STA_IF)
		if not sta_if.isconnected():
			print(' - Hooking me up...')
			sta_if.active(True)
			sta_if.connect(config.config['wifi']['ssid'], config.config['wifi']['password'])
			while not sta_if.isconnected():
				pass

	except Exception as inst:
	    print(" - **Abort Abort** _WIFI exception on connecting?_")
	    time.sleep(5)
	    print(type(inst))
	    print(inst.args)
	    print(inst)

	print(' - Configuration selfie:', sta_if.ifconfig())


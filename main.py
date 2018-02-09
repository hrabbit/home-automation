import config
import wifi
from mqtt import MQTT
# from pollers import poller
import poller
import sleep
import utime
import time

queue = None

def reboot():
	import machine
	machine.reboot()

def main():
	print("## Main routine")
	print("### Sending MQTT message")
	queue.publish("Wakeup notification")

	queue.publish(poller.temperature(), "temperature")
	queue.publish(poller.humidity(), "humidity")
	queue.publish(poller.raining(), "raining")

	# Iterate each poller item, sending a message response for each one
	# pollers = poller();

	pass

if __name__ == '__main__':
	time_startup = utime.ticks_ms()
	try:
		sleep.setup()
		wifi.connect()
		queue = MQTT()
		main()
	except Exception as inst:
		print(" - **Abort Abort** _Startup failure!_")
		time.sleep(5)
		print(type(inst))
		print(inst.args)
		print(inst)

	# Done what we can, time to have a nap
	print("## Back from main.. Bring out your main! Bring our your main!")
	# time_finish = utime.ticks_ms()
	uptime = utime.ticks_diff(utime.ticks_ms(), time_startup)
	print(" - Runtime (for shiggles): %s" % uptime)

	queue.disconnect()
	sleep.now()

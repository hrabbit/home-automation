import machine
import config

def setup():
	causes = {
		0: "Power on",
		1: "Power reset",
		2: "Hard reset",
		3: "Watchdog reset",
		4: "Deepsleep reset",
		5: "Soft reset"
	}

	print("## Sleep configuration")
	print("### Who disturbs my slumber?")
	print(" - Wake reason:", causes[machine.reset_cause()])

	# configure RTC.ALARM0 to be able to wake the device
	rtc = machine.RTC()
	rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

	# set RTC.ALARM0 to fire after 10 seconds (waking the device)
	# Value is actually in milliseconds
	duration = 10000
	if "sleep" in config.config and "duration" in config.config['sleep']:
		duration = config.config['sleep']['duration'] * 1000
	else:
		print(" - _No configured sleep time! Using default_")

	print(" - Duration set to **%s** seconds" % (duration / 1000))

	rtc.alarm(rtc.ALARM0, duration)

def now():
	print("## About to sleep")
	# If we want to delay the sleep period, before deepsleeping, this is the place
	# Basically allows a recovery by pushing a config with a sleep wait window
	if "sleep" in config.config and "delay" in config.config['sleep'] and config.config['sleep']['delay'] > 0:
		print(" - Delaying sleep for %s seconds" % config.config['sleep']['delay'])
		import time
		time.sleep(config.config['sleep']['delay'])

	print(" - And.. gone")
	machine.deepsleep()
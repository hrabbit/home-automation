# This file is executed on every boot (including wake-boot from deepsleep)

# This disabled the watchdog, in case things go wacky and it wants to take control
# import machine
# machine.WDT().deinit()

# import esp
# esp.osdebug(None)

import gc

# import the below to enable the webservice
# import webrepl
# Also, create a webrepl_cfg.py file in the root direct containing
# 	PASS = 'mypassword'

gc.collect()
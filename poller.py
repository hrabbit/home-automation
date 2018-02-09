import machine
import dht

d = dht.DHT22(machine.Pin(4))
d.measure()
rain = machine.Pin(15)

def temperature():
	print("Temperature:", d.temperature())
	return d.temperature()

def humidity():
	print("Humidity:", d.humidity())
	return d.humidity()

def raining():
	print("Rain:", rain.value())
	return rain.value()
import RPi.GPIO as GPIO
import dht11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

sensor = dht11.DHT11(pin=40)
temp = sensor.read()

#if temp.is_valid():
print("T:")
print( temp.temperature)
print("H:")
print( temp.humidity)
#else:	print("Te jodes")

# importamos la libreria GPIO
import RPi.GPIO as GPIO

# importamos la libreria time
import time
# desactivamos mensajes de error
GPIO.setwarnings(False)
# indicamos el uso de  la identificacion BCM para los GPIO
GPIO.setmode(GPIO.BOARD)
# indicamos que el GPIO18 es de salida de corriente
GPIO.setup(18,GPIO.OUT)

buzz=GPIO.PWM(18, 800000)
buzz.start(50)
while True:
	a=input()

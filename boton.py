import RPi.GPIO as GPIO
GPIO.setmode (GPIO. BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(3, GPIO.IN)

while True:
	if GPIO.input(3): 
		GPIO.output(7, True)
	else: 
		GPIO.output(7, False)

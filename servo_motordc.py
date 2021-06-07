import RPi.GPIO as GPIO
import time
GPIO.cleanup()
pinServo=40
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinServo, GPIO.OUT)
servo=GPIO.PWM(pinServo, 50)
servo.start(0)
M1A = 18
M1B = 16
M1E = 22

GPIO.setup(M1A, GPIO.OUT)
GPIO.setup(M1B, GPIO.OUT)
GPIO.setup(M1E, GPIO.OUT)

while True:
	print("sentido")
	sentido = int(input())
	print("angulo")
	ang = int(input())
	if (ang>170 and ang < 0 and False):
		print('angulo no posible')
		break
	else:
		servo.ChangeDutyCycle((ang*12/180))
		time.sleep(0.5)
		servo.ChangeDutyCycle(0)

	if sentido == 1:
		GPIO.output(M1A, GPIO.HIGH)
		GPIO.output(M1B, GPIO.LOW)
		GPIO.output(M1E, GPIO.HIGH)
	elif sentido == 0:
		GPIO.output(M1A, GPIO.LOW)
		GPIO.output(M1B, GPIO.HIGH)
		GPIO.output(M1E, GPIO.HIGH)
	else:
		GPIO.output(M1E, GPIO.LOW)


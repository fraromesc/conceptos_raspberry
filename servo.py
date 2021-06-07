import RPi.GPIO as GPIO
import time

pinServo=40
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinServo, GPIO.OUT)
servo=GPIO.PWM(pinServo, 50)
servo.start(0)
while True:
	ang = int(input())
#	if (ang>170 and ang < 0):
#		print('angulo no posible')
#		break
#	else:
	servo.ChangeDutyCycle((ang*12/180))
	time.sleep(0.5)

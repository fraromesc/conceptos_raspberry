import RPi.GPIO as GPIO
import time

pinServo=40
pinServo2=38
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinServo, GPIO.OUT)
GPIO.setup(pinServo2, GPIO.OUT)
servo=GPIO.PWM(pinServo, 50)
servo.start(0)
servo2=GPIO.PWM(pinServo2, 50)
servo2.start(0)
while True:
	print('servo')
	ang = int(input())
	servo.ChangeDutyCycle((ang*12/180))
	time.sleep(0.5)
	servo.ChangeDutyCycle(0)
	print('Servo2:')
	ang = int(input())
	servo2.ChangeDutyCycle((ang*12/180))
	time.sleep(0.5)
	servo2.ChangeDutyCycle(0)

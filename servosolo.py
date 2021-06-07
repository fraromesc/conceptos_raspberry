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
GPIO.output(M1E, GPIO.HIGH)
GPIO.output(M1A, GPIO.LOW)
GPIO.output(M1B, GPIO.HIGH)

while True:
	servo.ChangeDutyCycle((165*12/180))
	time.sleep(0.5)
	servo.ChangeDutyCycle(0)


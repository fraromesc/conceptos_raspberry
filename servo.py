import RPi.GPIO as GPIO #Importamos la libreria RPi.GPIO y para usarlo más facilmente le ponemos el nombre GPIO. Se puede poner cualquiera. 
import time

pinServo=7 

GPIO.setmode(GPIO.BOARD) #Indicamos que se utiliza la numeración de los pines.
GPIO.setup(pinServo, GPIO.OUT) #Indicamos el pin 7 como salida. 
servo=GPIO.PWM(servoPin, 50)
servo.start(0)
def giro(servoObjeto, ang)
	if (ang>170 and ang < 0)
		print('angulo no posible')
		break
	else
		servoObjeto.ChangeDutyCycle((a*12/180))
		time.sleep(0.5)


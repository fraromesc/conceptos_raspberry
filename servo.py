import RPi.GPIO as GPIO #Importamos la libreria RPi.GPIO y para usarlo más facilmente le ponemos el nombre GPIO. Se puede poner cualquiera. 
import time 

GPIO.setmode(GPIO.BOARD) #Indicamos que se utiliza la numeración de los pines.
GPIO.setup(7, GPIO.OUT) #Indicamos el pin 7 como salida. 

servo = GPIO.PWM(7, 50) #Indicamos que el pin 7, ademas de salida, es PWM
#pin y frecuencia
#Corresponde a un ciclo de 20 ms

servo.start(0) #Comienzo a usar el servo
#Para tarminar de usarlo se utiliza 'servo.stop()'
while True: 
	a = float(input("Introduzca Duty Cycle"))
	servo.ChangeDutyCycle((a*12/180)) #Para sg90 a 50 Hz
					# 1 = 0º
					#12 = 180º
					#6 =90º
					#0 => para el movimiento 
#Realmente esta relación lineal no se cuple. Al meter 15, se va a 0, los 90º los cumple. Para hacer 180º reales, 
#hay que meter 170.
#si metemos otros valores, se va a un rango que no funciona bien. En algunos casos crece manteniendo la misma
#relacion, pero llega un punto que vuelve al origne da igual el angulo. 
#Si se quiere una mejor relación, hacer un switch. 
	time.sleep(0.5) #No estoy seguro que unidad es
	servo.ChangeDutyCycle(0) #Ponemos el DutyCycle a 0 para evitar vibraciones


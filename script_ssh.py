import keyboard ##hay que instalarla
import RPi.GPIO as GPIO
import time
from bluepy.btle import Scanner

GPIO.setmode(GPIO.BCM)
####MODOS FUNCIONAMIENTO
    #O --> manual -->"m"
    #1 --> automatico --> "n"
    #2 --> reposo --> "b"
    #3 --> reset --> " "
modo=0 #empezamos en modo manual
manual = "m"
MANUAL = "M"
automatico = "n"
AUTOMATICO = "N"
reposo = "b"
REPOSO ="B"
reset =" "

#Sensores distancias
disTrig=[] #Delantero, izq medio, der medio, izq tras, der tras
disEcho=[] #idem
for i in disTrig:
    GPIO.setup(i, GPIO.OUT)
for i in disEcho:
    GPIO.setup(i, GPIO.IN)

"""distTrigDel =
distEchoDel =
distTrigIzq =
distEchoIzq =
distTrigDer =
distTrigTrasIzq =
distEchoTrasIzq =
distTrigTrasDer =
distEchoTrasDer ="""
def distancia():
    r=[0,0,0,0,0]
    for i in range(0,4):
        GPIO.output(disTrig[i], True)
        time.sleep(0.00001)
        GPIO.output(disTrig[i], False)
        tiempoInicio = time.time()
        tiempoFin = time.time()
        while GPIO.input(disEcho[i]) == 0:
            tiempoInicio = time.time()
        while GPIO.input(disEcho[i]) == 1:
            tiempoFin = time.time()
        difTiempo = tiempoFin - tiempoInicio
        d = (difTiempo * 34300) / 2
        print("no se si es en cm o no- funcion distancia")
        if  d <= 2
            r[i]=1
    return r

#Motor
MotorIN1 =
MotorIN2 =
MotorE1 =
motor = GPIO.PWM(MotorE1, 50)
motor.start(0)
def velocidad(sentido)
    #sentido = 1 --> hacia delante
    #sentido = 0 --> hacia atras
    if sentido == 1:
        GPIO.output(MotorIN1,GPIO.LOW) # Establecemos el sentido de giro con los pines IN1 e IN2
        GPIO.output(MotorIN2,GPIO.HIGH)  # Establecemos el sentido de giro con los pines IN1 e IN2
        motor.ChangeDutyCyle(50)
    else
        GPIO.output(MotorIN1,GPIO.HIGH) # Establecemos el sentido de giro con los pines IN1 e IN2
        GPIO.output(MotorIN2,GPIO.LOW)  # Establecemos el sentido de giro con los pines IN1 e IN2
        motor.ChangeDutyCyle(25)
#Servo
pinCam1=
pinCam2=
pinDir=
GPIO.setup(pinCam1, GPIO.OUT)
cam1=GPIO.PWM(pinCam1, 50)
GPIO.setup(cam2, GPIO.OUT)
cam2=GPIO.PWM(pinCam2, 50)
GPIO.setup(pinDir, GPIO.OUT)
direc=GPIO.PWM(pinDir, 50)
angCam1Init=
angCam2Init=
angDirecInit=
angDirecDer=
angDirecIzq=
angCam1=angCam1Init
angCam2=angCam2Init
angDirec=angFirecInit
def ang2dc(ang): #convertir angulo en duty cycle
    return ang*12/180

#Escaner bluetooh
    #Direcciones Mac
beacon0=""
beacon1=""
beacon2=""
    #Posiciones beacon
pBeacon0=np.array([0,0])
pBeacon1=np.array([1,0])
pBeacon2=np.array([0,1])
    #Posiciones modo AUTOMATICO
p1=np.array([0.3, 0.1])
p2=np.array([0.7, 0.1])
p3=np.array([1.3, 3])

def ang():
    scanner = Scanner()
    devices = scanner.scan(10.0)



while True:
    #CAMBIAMOS DE MODO
    tecla = keyboard.read_key()
    if tecla == manual or tecla == MANUAL:
        while tecla ==manual or tecla == MANUAL:
            modo = 0 #Pasamos a modo automática al pulsa m o M
    elif tecla == automatico or tecla == AUTOMATICO:
        while tecla = automatico or tecla == AUTOMATICO:
            modo = 1
    elif tecla == reposo or tecla == REPOSO:
        while tecla == reposo or tecla == REPOSO:
            modo = 2

    elif tecla == reset
        modo = 0
        motor.ChangeDutyCycle(0)
        angCam1=angCam1Init
        cam1.ChangeDutyCyle(ang2dc(angCam1))
        angCam2=angCam2Init
        cam2.ChangeDutyCycle(ang2dc(angCam2))
        angDirec=angDirecInit
        direc.ChangeDutyCycle(angDirec)


    if modo != 0 and modo != 1 and modo != 2:
        modo = 2;


    #MAQUINA DE ESTADO
    if modo = 0: #MODO MANUAL
        if tecla == "w" or tecla == "W":  #hacia delante
            velocidad(1)
        elif tecla == "s" or tecla == "S":  #hacia atras
            velocidad(0)
        else:  #PARAR MOTOR
            motor.ChangeDutyCycle(0)

        if tecla == "d" or tecla == "D": #giro derecha
            direc.ChangeDutyCycle(angDirecDer)
        elif tecla == "a" or tecla =="A": #giro izquierda
            direc.ChangeDutyCycle(angDirecIzq)
        else:
            direc.ChangeDutyCycle(angDirecInit)

        if tecla == "i" or tecla == "I": #camara arriba
            if angCam1 < 168 :
                angCam1 = angCam1 + 2
                cam1.ChangeDutyCyle(ang2dc(angCam1))
        elif tecla == "k" or tecla == "K": #camara abajo
            if angCam1 > 2 :
                angCam1 = angCam1 - 2
                cam1.ChangeDutyCycle(ang2dc(angCam1))
        elif tecla == "j" or tecla == "J": #camara izquierda
            if angCam2 > 168 :
                angCam2 = angCam2 + 2
                cam2.ChangeDutyCycle(ang2dc(angCam2))
        elif tecla == "l" or tecla == "L": #camara derecha
            if angCam2 < 2 :
                angCam2 = angCam2 - 2
                cam2.ChangeDutyCycle(ang2dc(angCam2))

    elif modo = 1: #MODO AUTOMATICO
        ###pseucodigo
            #1. determinar posicion
            #2. hacer avanzar el coche
            #3. determianr segundo punto
            #4. con los 2 ptos, obtener el vector director
            #5.calcular ángulo necesario para llegar al punto deseado
            #6. hacer andar al coche e ir midiendo la desviación
    elif modo = 2: #MODO REPOSO
        motor.ChangeDutyCycle(0)

#Incluimos las librerías
import socket
import sys

#Creamos el socket de comunicación
try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
        print ('Fallo al crear socket')
        sys.exit()
print ('Socket Creado')

#Creamos las variables para comunicarnos
IP = '192.168.2.252'
puerto = 15000

#Configuramos el socket
try:
    s.bind((IP,puerto))
except socket.error as e:
        print ('Fallo al configurar socket')
        s.close()
        sys.exit()

#Nos disponemos a estar en escucha
try:
    s.listen(10)
except socket.error as e:
        print ('Fallo al conectar')
        s.close()
        sys.exit()
print('Puerto escuchando...')

#Aceptamos comunicación
sconn, direccion = s.accept()
print ('Conectado con ' + str(direccion[0]) + 'desde el puerto ' + str(direccion[1]))

#Variable para mantener el bucle while
Salida = True

#Bucle while sale cuando se introduce por teclado Adios
while Salida:
    #Esperamos recibir mensaje del cliente
    respuesta = sconn.recv(1024)
    #Decodificamos el mensaje
    print (respuesta.decode())
    #Comprobamos si el mensaje es Adios
    if respuesta.decode() =='Adios':
        #Preparamos salida
        Salida = False
        #Mensaje de despedida
        msg = 'Adios'
        msg=msg.encode()
    else:
        #Componemos un nuevo mensaje con lo recibido
        msg = respuesta
        #Intentamos enviar el mensaje
    try:
        sconn.sendall(msg)
    except socket.error as e:
        print ('error al enviar el mensaje')
        sconn.close()
        sys.exit()
    print ('Respuesta enviada')
#Finaliza el bucle, cierra los sockets y cierra el programa
sconn.close()
s.close()
print ('Socket cerrado. Saliendo...')
sys.exit()

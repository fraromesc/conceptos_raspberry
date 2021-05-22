from bluepy.btle import Scanner
A=-50
n=2
while True: 
	macJavi="b4:c4:fc:fa:f6:e0"
	macHelena="60:ab:67:1d:20:23"
	macMario="e0:33:8e:c9:83:b2"
	scanner = Scanner()
	devices = scanner.scan(10.0)
	print(devices)
	for device in devices:
	    print("hola")
	    if (macJavi==device.addr or macHelena==device.addr or device.addr==macMario): 
		    print("hola1")
		    d=10**((device.rssi-A)/10*n)
		    d1=10**(-(device.rssi-1)/10*n)
	    	    cad=str(d)+"\t"+str(d1)
		    print(device.addr)
		    print(device.rssi)


import serial 

# Abrir el puerto serial
Rpi = serial.Serial('/dev/ttyACM0', 115200)

try:
    Rpi.Open()
    print("Conectado")
except:
    if(Rpi.isOpen()):
        print("Connectado")
    else:
        print("No conectado")

while True:
    if (Rpi.isOpen()):
        dt= Rpi.readline()
        Dt_s = dt.decode('UTF-8')

    print(dt)
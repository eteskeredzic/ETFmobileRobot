import serial
import time
arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=0.5)
time.sleep(1)  # give the connection a second to settle

while True:
    v = 0
    w = 0
    #print("Unesi linearnu brzinu: ")
    #v = input()
    #print("Unesi ugaonu brzinu: ")
    #w = input()
    #print(str(v) + " " + str(w))
    us1 = int(416.67 * v + 70.834 * w + 1500)
    us2 = int(416.67 * v - 70.834 * w + 1500)

    if us1 < 1000:
        us1 = 1000
    elif us1 > 2000:
        us1 = 2000
    elif 1350 <= us1 < 1500:
        us1 = us1 - 150
    elif 1500 < us1 <= 1650:
        us1 = us1 + 150

    if us2 < 1000:
        us2 = 1000
    elif us2 > 2000:
        us2 = 2000
    elif 1350 <= us2 < 1500:
        us2 = us2 - 150
    elif 1500 < us2 <= 1650:
        us2 = us2 + 150

    us1 = input()
    us2 = input()
    us1 = (str(us1))
    us2 = (str(us2))
    us1 = us1.encode(encoding='ascii')
    us2 = us2.encode(encoding='ascii')
    print(us1 + " " + us2)
    arduino.write(us1)
    arduino.write(us2)

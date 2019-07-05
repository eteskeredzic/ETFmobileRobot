import keyboard
import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=0.5)
time.sleep(1)  # give the connection a second to settle


def move_rover(speed_left, speed_right):
    speed_left = (str(speed_left))
    speed_right = (str(speed_right))
    speed_left = speed_left.encode(encoding='ascii')
    speed_right = speed_right.encode(encoding='ascii')
    arduino.write(speed_left)
    arduino.write(speed_right)
    print speed_left + " " + speed_right

last_pressed = 'x'
while True:
    time.sleep(0.2)
    if keyboard.is_pressed('w') and last_pressed != 'w':
        move_rover(1800, 1800)
	last_pressed = 'w'
    elif keyboard.is_pressed('s') and last_pressed != 's':
        move_rover(1200, 1200)
	last_pressed = 's'
    elif keyboard.is_pressed('a') and last_pressed != 'a':
        move_rover(1200, 1800)
	last_pressed ='a' 
    elif keyboard.is_pressed('d') and last_pressed != 'd':
        move_rover(1800, 1200)
	last_pressed = 'd'
    elif last_pressed != 'x' and not keyboard.is_pressed('a') and not keyboard.is_pressed('w') and not keyboard.is_pressed('s') and not keyboard.is_pressed('d'):
        move_rover(1500, 1500)
	last_pressed = 'x'

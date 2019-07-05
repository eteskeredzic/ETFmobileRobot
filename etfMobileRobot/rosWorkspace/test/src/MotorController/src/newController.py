#!/usr/bin/env python
import roslib
import serial
roslib.load_manifest('MotorController')
import rospy 
from std_msgs.msg import Int32
from std_msgs.msg import String
from geometry_msgs.msg import Twist

arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=0.5)
rospy.sleep(1.) # give the connection a second to settle

pozvan_key = 0

def callback2(msg):

	global pozvan_key

	v = msg.linear.x;
	v = -v;
	w = msg.angular.z;
	w = -w;
	if v != 0 or w != 0:
		pozvan_key = 1

	if pozvan_key == 1:
		us1 = int(416.67 * v + 70.834 * w + 1500)
    		us2 = int(416.67 * v - 70.834 * w + 1500)
    		us1 = (str(us1))
    		us2 = (str(us2))
    		us1 = us1.encode(encoding='ascii')
    		us2 = us2.encode(encoding='ascii')

    		arduino.write(us1)
    		arduino.write(us2)
	#pozvan_key = 0
		print('zavrsen')


def callback(msg):
	if pozvan_key == 1:
		return
	rospy.loginfo('---------------')
	rospy.loginfo('Primio poruku !')
	v = msg.linear.x
	v=-v;
	w = msg.angular.z
	w = -w;
	us1 = int(416.67 * v + 2*70.834 * w + 1500)
    	us2 = int(416.67 * v - 2*70.834 * w + 1500)
	rospy.loginfo(v);
	rospy.loginfo(w);
    	if us1 < 1000:
        	us1 = 1000
    	elif us1 > 2000:
        	us1 = 2000

    	if us2 < 1000:
        	us2 = 1000
    	elif us2 > 2000:
        	us2 = 2000

	if us1 > 1300 and us1 < 1550 and us2 > 1550 and us2 < 1650:
		us1 = 1300
		us2 = 1650
	
	if us2 > 1300 and us2 < 1550 and us1 > 1550 and us1 < 1650:
		us2 = 1300
		us1 = 1650
	
	if us1 > 1500 and us1 < 1680:
		us1 = 1680
    	if us1 > 1320 and us1 < 1500:
		us1 = 1320


	if us2 > 1500 and us2 < 1680:
		us2 = 1680
	if us2 > 1320 and us2 < 1500:
		us2 = 1320
	


 
   	us1 = (str(us1))
    	us2 = (str(us2))
    	us1 = us1.encode(encoding='ascii')
    	us2 = us2.encode(encoding='ascii')
    	arduino.write(us1)
    	arduino.write(us2)
	rospy.loginfo(us1)
	rospy.loginfo(us2)
	rospy.loginfo('---------------')




rospy.init_node('motorController')
sub = rospy.Subscriber('/cmd_vel', Twist, callback)
sub2 = rospy.Subscriber('/key_vel', Twist, callback2)
print('Hello there!')

rospy.spin()


# import libararies

import RPi.GPIO as GPIO
import time


# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)
# Set pins 12 & 13 & 18 as outputs, and define as PWM servo1 & servo2 & servo3
GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(12,50)

# Start PWM running on 2 servos, value of 0 (pulse off)
servo1.start(0)

# Read Coordinates
# f = open('/home/minsu/coordinates.txt', 'r')
# c = f.read()
# f.close()
# webcam_X_Center = 208
# webcam_X_Center_Left = -30
# webcam_X_Center_Right = 30
# c = 208(webcam's x_center coordinates) - (object's x_center coordinates)
# Turn servo1


try :
	while(1):
		f = open('/home/minsu/coordinates.txt', 'r')
		c = f.read()
#		c = float()
		f.close()
		if c == None :
			for i in range (0,180):
				global DC
				DC=1/18.*(i)+2
				servo1.ChangeDutyCycle(DC)
				time.sleep(.02)
			for i in range(180,0,-1):
				DC=1/18.*(i)+2
				servo1.ChangeDutyCycle(DC)
				time.sleep(.02)
		else :
			c = int(c)
			if c < -30 :
				DC -=1
				servo1.ChangeDutyCycle(DC)
				time.sleep(.02)
			elif -30 < c < 30 :
				servo1.stop()
			else :
				DC +=1
				servo1.ChangeDutyCycle(DC)
				time.sleep(.02)
#try :
	#while True:
		#servo1.ChangeDutyCycle(12.5)
		#time.sleep(2)
		#servo1.ChangeDutyCycle(10.0)
		#time.sleep(2)
		#servo1.ChangeDutyCycle(7.5)
		#time.sleep(2)
		#servo1.ChangeDutyCycle(5.0)
		#time.sleep(2)
		#servo1.ChangeDutyCycle(2.5)
		#time.sleep(2)
		#servo1.ChangeDutyCycle(5.0)
		#time.sleep(2)
		#servo1.ChangeDutyCycle(7.5)
		#time.sleep(2)
		#servo1.ChangeDutyCycle(10.0)
		#time.sleep(2)


except KeyboardInterrupt:
	servo1.stop()

GPIO.cleanup()


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

# Turn servo1 

try :
	while True:
		servo1.ChangeDutyCycle(12.5)
		time.sleep(2)
		servo1.ChangeDutyCycle(10.0)
		time.sleep(2)
		servo1.ChangeDutyCycle(7.5)
		time.sleep(2)
		servo1.ChangeDutyCycle(5.0)
		time.sleep(2)
		servo1.ChangeDutyCycle(2.5)
		time.sleep(2)
		servo1.ChangeDutyCycle(5.0)
		time.sleep(2)
		servo1.ChangeDutyCycle(7.5)
		time.sleep(2)
		servo1.ChangeDutyCycle(10.0)
		time.sleep(2)


except KeyboardInterrupt:
	servo1.stop()


GPIO.cleanup()


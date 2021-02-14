import RPi.GPIO as GPIO
import time

pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin,50)
p.start(0)

try :
	while True:
		p.ChangeDutyCycle(1)
		print("angle : 1 ")
		time.sleep(2)
		#p.ChangeDutyCycle(5)
		#print("angle : 5 ")
		#time.sleep(1)
		p.ChangeDutyCycle(12.5)
		print("angle : 12.5 ")
		time.sleep(2)
except KeyboardInterrupt:
	p.stop()

GPIO.cleanup()

import RPi.GPIO as GPIO
from time import sleep
import BlynkLib

in1 = 2 #Connect pin 2 of Raspberry Pi to in1 of the motor Driver
in2 = 3 #Connect pin 3 of Raspberry Pi to in2 of the motor Driver
in3 = 4 #Connect pin 4 of Raspberry Pi to in3 of the motor Driver
in4 = 17 #Connect pin 17 of Raspberry Pi to in4 of the motor Driver

GPIO.setwarning(False) # turning off warnings in debugging

GPIO.setmode(GPIO.BWM)

GPIO.setup(in1, GPIO.OUT)# setup the output pins
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

# Initiate Blynk
blynk = BlynkLib.Blynk('Project Token Key from the Blynk app')

class dir:
	# setting up variables for motor direction
	m1 = 0
	m2 = 0
#register Blynk Virtual pins, reading the input and setting the direction variables
@blynk.VIRTUAL_WRITE(2)# Read Virtual pin 2
def right_handler(value):
	inp = '{}'.format(value)
	numInput = inp[3:-2]
	if (numInput == '1'):
		#print ("Right") # Uncomment for debugging
		dir.m1 +=1
		dir.m2 +=1
	if (numInput == '0'):
		dir.m1 -=1
		dir.m2 -=1

@blynk.VIRTUAL_WRITE(3)# Read Virtual pin 3
def back_handler(value):
	inp = '{}'.format(value)
	numInput = inp[3:-2]
	if (numInput == '1'):
		#print ("Back") # Uncomment for debugging
		dir.m1 -=1
		dir.m2 +=1
	if (numInput == '0'):
		dir.m1 +=1
		dir.m2 -=1

@blynk.VIRTUAL_WRITE(0)# Read Virtual pin 0
def fwd_handler(value):
	inp = '{}'.format(value)
	numInput = inp[3:-2]
	if (numInput == '1'):
		#print ("Forward") # Uncomment for debugging
		dir.m1 +=1
		dir.m2 -=1
	if (numInput == '0'):
		dir.m1 -=1
		dir.m2 +=1

@blynk.VIRTUAL_WRITE(1)# Read Virtual pin 1
def left_handler(value):
	inp = '{}'.format(value)
	numInput = inp[3:-2]
	if (numInput == '1'):
		#print ("Left") # Uncomment for debugging
		dir.m1 -=1
		dir.m2 -=1
	if (numInput == '0'):
		dir.m1 +=1
		dir.m2 +=1

# Running an infinite loop to exectue this continuously
while True:
	blynk.run()
	if (dir.m1 > 0):
		GPIO.output(in1, GPIO.HIGH)
		GPIO.output(in2, GPIO.LOW)
	if (dir.m1 == 0):
		GPIO.output(in1, GPIO.LOW)
		GPIO.output(in2, GPIO.LOW)
	if (dir.m1 > 0):
		GPIO.output(in1, GPIO.LOW)
		GPIO.output(in2, GPIO.HIGH)

	if (dir.m2 > 0):
		GPIO.output(in3, GPIO.HIGH)
		GPIO.output(in4, GPIO.LOW)
	if (dir.m2 == 0):
		GPIO.output(in3, GPIO.LOW)
		GPIO.output(in4, GPIO.LOW)
	if (dir.m2 > 0):
		GPIO.output(in3, GPIO.LOW)
		GPIO.output(in4, GPIO.HIGH)




#!/usr/bin/python

#Setup

import Adafruit_BBIO.PWM as pwm
import sys, os
import XboxController
import time


pin1 = "P9_14"
pin2 = "P8_19"

frequency = 50
# 5% = 1ms @ 50hz
# 10% = 2ms @ 50hz
duty = 7.50

# pwm.start
pwm.start(pin1, duty, frequency)
pwm.start(pin2, duty, frequency)

'''
while True:

	duty = input("enter duty:")
	print "You said:",duty
	if duty == 99:
		duty = 7.5
	pwm.set_duty_cycle(pin, duty)
	print "Running at ", duty, "%"

	if duty == 0:
		pwm.stop(pin)
		pwm.cleanup()
		sys.exit()	
'''

def myCallback(controlId, value):
	duty = value / 10 + 7.5
	print value, duty

def leftTrigger(value):
	duty = value / 10 + 7.5
	pwm.set_duty_cycle(pin1, duty)

def rightTrigger(value):
	duty = value / 10 + 7.5
	pwm.set_duty_cycle(pin2, duty)


xboxCont = XboxController.XboxController(
	controllerCallBack = myCallback,
	joystickNo = 0,
	deadzone = 15,
	scale = 25,
	invertYAxis = False)

xboxCont.setupControlCallback(xboxCont.XboxControls.LTRIGGER, leftTrigger)
xboxCont.setupControlCallback(xboxCont.XboxControls.RTRIGGER, rightTrigger)



try:
	xboxCont.start()
	print "Controller Ready"
	while True:
		time.sleep(0.1)


except KeyboardInterrupt:
	print "User Quit"


finally:
	xboxCont.stop()
        pwm.stop(pin1)
        pwm.stop(pin2)
        pwm.cleanup()


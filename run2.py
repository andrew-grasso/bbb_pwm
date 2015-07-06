#!/usr/bin/python

#Setup

import Adafruit_BBIO.PWM as pwm
import sys

pin = "P8_19"

frequency = 50
# 5% = 1ms @ 50hz)
duty = 5.0

# pwm.start
pwm.start(pin, duty, frequency)


while True:

	duty = input("enter duty:")
	pwm.set_duty_cycle(pin, duty)
	print "Running at ", duty, "%"

	if duty == 0:
		pwm.stop(pin)
		pwm.cleanup()
		sys.exit()	

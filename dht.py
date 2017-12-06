# -*- coding: utf-8 -*-

import Adafruit_DHT
import RPi.GPIO as GPIO
import sys
import time
gc=u"\u00b0"
sensor = 22 #dht22
pin =  17 #gpio 17 pin 11
hum, temp = Adafruit_DHT.read_retry(sensor, pin)
while True:

     print "DHT temperatuur= " ,"%.2f" % temp,u"\u00b0C"
     print "DHT relatieve luchtvochtigheid", "%2i" % hum,"%"
     time.sleep(2)

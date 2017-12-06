#!/usr/bin/env python

import sys
import time
import datetime
import random 
import SDL_DS3231


ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)


while True:
       print "DS3231=\t\t%s" % ds3231.read_datetime()

       print "DS3231 Temp=", ds3231.getTemp()
       time.sleep(10.0)

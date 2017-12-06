# -*- coding: utf-8 -*-


import Adafruit_DHT
import RPi.GPIO as GPIO
import sys
import os
import time
import datetime
import SDL_DS3231



#set adress  klok
ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)

#ds18b20 1 en 2 op gpio 4 pin 7

#de DHT zie hieronder
sensor = 22 #dht22
pin = 17    #gpio 17 pin 11

 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

ds18_1 = '/sys/bus/w1/devices/28-03168264b0ff/w1_slave'
ds18_2 = '/sys/bus/w1/devices/28-031681a54eff/w1_slave'

def get_dht():
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    return temp, hum

def temp_raw(fn):
    f=open(fn, 'r')
    lines=f.readlines()
    f.close()
    return lines

def read_temp(nummer):
    if nummer==1:
       lines= temp_raw(ds18_1)
    elif nummer ==2:
       lines= temp_raw(ds18_2)

     # while lines[0].strip()[-3] != 'YES': 
      #    time.sleep(0.2)
       #   lines= temp_raw(nummer)
    temp_output = lines[1].find('t=')
    if temp_output !=-1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c= float(temp_string) /1000
        return temp_c

while True:

        dht=get_dht()

        T1=read_temp(1)
        T2=read_temp(2)
        T3=dht[0]
        H1=dht[1]

        #print "Temperatuur probe 1: ","%.2f" % read_temp(1)
        #//print "Temperatuur probe 2: ","%.2f" % read_temp(2)
        #dht=get_dht()
        #print "DHT temperatuur= " ,"%.2f" % dht[0],u"\u00b0C"
        #print "DHT relatieve luchtvochtigheid", "%2i" % dht[1],"%"
        
        #print T1,T2,T3,H1
        if T1<T2:
           print "T1 heeft het koud", " het is nu " , ds3231.read_datetime()
        elif T2<T1:
           print "T2 heeft het koud", " het is nu " , ds3231.read_datetime()
        elif T1==T2:
           print " kan niet waar zijn ze hebben dezelfde temperatuur"   
        time.sleep(1)

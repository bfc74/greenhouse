import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

ds18_1 = '/sys/bus/w1/devices/28-03168264b0ff/w1_slave'
ds18_2 = '/sys/bus/w1/devices/28-031681a54eff/w1_slave'

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
        print "Temperatuur probe 1: ","%.2f" % read_temp(1)
        print "Temperatuur probe 2: ","%.2f" % read_temp(2)
        time.sleep (1)

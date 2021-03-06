#import graph
#pyplot doesn't seem to work on pi

import lib, config
from time import time, sleep
import serial

degree_sign= u'\N{DEGREE SIGN}'

temp=graph.Graph("Temperature over the past 12 hours", "Time before current time, hours", "Temperature, "+degree_sign+"C", "temp.png")
ph=graph.Graph("ph over the past 12 hours", "Time before current time, hours", "ph", "ph.png")
humidity=graph.Graph("Humidity over the past 12 hours", "Time before current time, hours", "Humidity, %RH", "humidity.png")

ser = serial.Serial('COM3', 9600, timeout=1)

sensors=lib.UpdateSensors(ser)
sprayers=lib.Sprayers()

while(True):
    ttime=time()
    if int(ttime)%5==0:
        sleep(1)
        #this is to prevent modulous from triggering multiple times in a second
        sensors.update()
    # if int(ttime)%(config.ON_TIME)==0:
    #     sprayers.spray(config.OFF_TIME)

    # if int(ttime)%(config.SENSOR_UPDATE_TIME*60)==0:
    #     sensors.update()
        temp.add(sensors.get_temp())
        humidity.add(sensors.get_humidity())

    #     temp.make_graph()
    #     humidity.make_graph()

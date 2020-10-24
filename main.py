import lib, graph, config
from time import time

degree_sign= u'\N{DEGREE SIGN}'

temp=graph.Graph("Temperature over the past 12 hours", "Time before current time, hours", "Temperature, "+degree_sign+"C", "temp.png")
ph=graph.Graph("ph over the past 12 hours", "Time before current time, hours", "ph", "ph.png")

sensors=lib.UpdateSensors()
sprayers=lib.Sprayers()

while(True):
    ttime=time()
    # if int(ttime)%(config.ON_TIME)==0:
    sprayers.spray(config.OFF_TIME)

    # if int(ttime)%(config.SENSOR_UPDATE_TIME*60)==0:
    temp.add(sensors.get_temp())
    ph.add(sensors.get_ph())

    temp.graph()
    ph.graph()
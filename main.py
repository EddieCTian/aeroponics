import lib, graph, config
from time import time

degree_sign= u'\N{DEGREE SIGN}'

temp=graph.Graph("Temperature over the past 12 hours", "Time before current time, hours", "Temperature, "+degree_sign+"C", "temp.png")
ph=graph.Graph("ph over the past 12 hours", "Time before current time, hours", "ph", "ph.png")
humidity=graph.Graph("Humidity over the past 12 hours", "Time before current time, hours", "Humidity, %RH", "humidity.png")

sensors=lib.UpdateSensors()
sprayers=lib.Sprayers()

while(True):
    ttime=time()
    if int(ttime)%5==0:
        sensors.update()
        print(sensors.get_temp())
        print(sensors.get_humidity())
    # if int(ttime)%(config.ON_TIME)==0:
    #     sprayers.spray(config.OFF_TIME)

    # if int(ttime)%(config.SENSOR_UPDATE_TIME*60)==0:
    #     sensors.update()
        temp.add(sensors.get_temp())
        humidity.add(sensors.get_humidity())

        temp.make_graph()
        humidity.make_graph()
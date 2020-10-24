# See this for their 1115 library
# https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/ads1015-slash-ads1115


# sensor=2 (SDA)
#        3 (SCL)
# water=14 

#from gpiozero import LED


#LED placeholder class
import config
from threading import Timer

class LED: 
    def __init__(self, pin):
        self.pin=pin
        self.on=0
    def on(self):
        self.on=1
        return True
    def off(self):
        self.on=0
        return True
# end LED placeholder class

class UpdateSensors:
    def __init__(self):
        self.temp=0
        self.ph=0
        self.temp_danger=0
        self.ph_danger=0
    def update(self):
        self._temp_reading()
        self._ph_reading()
        self._danger()
        return True
    def get_temp(self):
        return self.temp
    def get_ph(self):
        return self.ph
    def get_danger(self):
        return [self.temp_danger, self.ph_danger]
    def _ph_reading(self):
        temp=0
        self.temp=temp
        return True
    def _temp_reading(self):
        ph=0
        self.ph=ph
        return True
    
    def _danger(self):
        if self.temp>config.TEMP_HIGH:
            self.temp_danger=self.temp-config.TEMP_HIGH
        elif self.temp<config.TEMP_LOW:
            self.temp_danger=config.TEMP_LOW-self.temp
        if self.ph>config.PH_HIGH:
            self.ph_danger=self.ph-config.PH_HIGH
        elif self.ph<config.PH_LOW:
            self.ph_danger=config.PH_LOW-self.ph
        return True

class Sprayers:
    def __init__(self):
        self.pump=LED(config.PUMP)
    def spray(self, time):
        t=Timer(float(time), self.off)
        self.on()
        t.start()
        return True
    def on(self):
        # self.pump.on()
        # what's wrong here?
        return True
    def off(self):
        # self.pump.off()
        # what's wrong here?
        return True

from gpiozero import LED
import config
import arduino
from threading import Timer

#LED placeholder class
# class LED: 
#     def __init__(self, pin):
#         self.pin=pin
#         self.on=0
#     def on(self):
#         self.on=1
#         return True
#     def off(self):
#         self.on=0
#         return True
# end LED placeholder class

class UpdateSensors:
    def __init__(self, serial):
        self.serial=serial
        self.temp=0
        self.ph=0
        self.humidity=0
        self.temp_danger=False
        self.ph_danger=False
    def update(self):
	print('updating')
        self._temp_reading()
        #self._ph_reading()
        self._humidity_reading()
        self._danger()
        return True
    def get_temp(self):
        return self.temp
    def get_humidity(self):
        return self.humidity
    def get_ph(self):
        return self.ph
    def get_danger(self):
        return [self.temp_danger, self.ph_danger]
    def _temp_reading(self):
        self.temp=arduino.get_temp_from_arduino(ser)
        return True
    def _ph_reading(self):
        self.ph=arduino.get_ph_from_arduino(ser)
        return True
    def _humidity_reading(self):
        self.humidity=arduino.get_humidity_from_arduino(ser)
        return True
    
    def _danger(self):
        if self.temp>config.TEMP_HIGH:
            self.temp_danger=True
        elif self.temp<config.TEMP_LOW:
            self.temp_danger=True
        else:
            self.temp_danger=False

        if self.ph>config.PH_HIGH:
            self.ph_danger=True
        elif self.ph<config.PH_LOW:
            self.ph_danger=True
        else:
            self.temp_danger=False
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

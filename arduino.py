import serial

def get_temp_from_arduino():
    ser=serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    ser.write('0')
    data=ser.read(4)
    ser.close()
    return data
def get_humidity_from_arduino():
    ser=serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    ser.write('1')
    data=ser.read(4)
    ser.close()
    return data
def get_ph_from_arduino():
    ser=serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    ser.write('2')
    data=ser.read(4)
    ser.close()
    return float(data)
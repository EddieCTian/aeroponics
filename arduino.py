import serial

def get_temp_from_arduino():
    ser.flush()
    #ser.write('0')
    while True:
        if ser.in_waiting>0:
            data=ser.readline()
            print("got temp")
            break
    print(type(data))
    print("This is the temperature: "+ data)
    return data
def get_humidity_from_arduino():
    ser.flush()
    #ser.write('1')
    while True:
        if ser.in_waiting>0:
            data=ser.readline()
            print("got humidity")
            break
    print(type(data))
    print("This is the humidity: "+ data)
    return data
def get_ph_from_arduino():
    ser.flush()
    #ser.write('2')
    while True:
        if ser.in_waiting>0:
            data=ser.readline().decode('utf-8').rstrip()
            break
    return data

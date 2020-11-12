import serial, time

def get_temp_from_arduino(sserial):
    time.sleep(1)
    return write_read("temp", sserial)
def get_humidity_from_arduino(sserial):
    time.sleep(1)
    return write_read("hum", sserial)
def get_ph_from_arduino(sserial):
    time.sleep(1)
    return write_read("ph", sserial)

def write_read(val, sserial):
    sserial.flush()
    sserial.write((val+"\n").encode('utf-8'))
    while True:
        if sserial.in_waiting>0:
            break
    line = sserial.readline()
    return float(line)

if __name__ == "__main__":
    sserial = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)
    print(get_temp_from_arduino(sserial))
    print(get_humidity_from_arduino(sserial))
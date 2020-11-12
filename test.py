<<<<<<< HEAD
import serial, time
ser = serial.Serial('COM3', 9600, timeout=1)
ser.flush()
while True:
    # ser.write(b"aa\n")
    hi=input()
    ser.write((hi+"\n").encode('utf-8'))
    while True:
        if ser.in_waiting>0:
            break
    # line = ser.readline().decode('utf-8').rstrip()
    line = ser.readline()
    print(line)
    print(type(line))
    time.sleep(1)
    # time.sleep(1)
    # #ser.write(0b0)
    # # if ser.in_waiting > 0:
    # line = ser.read()
    # print(line)
=======
import serial
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
>>>>>>> 2c75e5d43f6b4469e53b066c78f1dd7c1e503385

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

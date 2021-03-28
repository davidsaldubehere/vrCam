import serial
import time
ser = serial.Serial()
ser.baudrate= 9600
ser.port = '/dev/ttyUSB0'
ser.open()
for i in range(90, 100):
    ser.write((f"X90Y{i}").encode())
    time.sleep(.5)
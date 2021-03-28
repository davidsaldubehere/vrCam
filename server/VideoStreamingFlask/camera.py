import cv2
import serial
import time
import random
ds_factor=0.6
ser = serial.Serial()
ser.baudrate= 9600
ser.port = '/dev/ttyUSB0'
ser.open()
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        #ser.write((f"X90Y{random.randint(90,140)}").encode())
        #time.sleep(4)
        image=cv2.resize(image,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

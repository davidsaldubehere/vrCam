
from flask import Flask, render_template, Response, redirect, url_for, request
from camera import VideoCamera
import serial
app = Flask(__name__)
ser = serial.Serial()
ser.baudrate= 9600
ser.port = '/dev/ttyUSB0'
ser.open()
@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/move',methods = ['POST', 'GET'])
def move():
    gamma = request.json['gamma']
    alpha = request.json["alpha"]
    print(alpha)
    if int(gamma)>0:
        alpha = 180-(180-int(alpha))
    elif int(gamma)<0:
        alpha = 180-(360-int(alpha))
    print(alpha)
    if(int(gamma)<0):
        gamma = (int(gamma) * -1)
    elif(int(gamma)>0):
        gamma = 180 - int(gamma)
    if not alpha < 0 and not alpha > 180:

        ser.write(f"X{int(alpha)}Y{int(gamma)}".encode())
    return "moving"




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, ssl_context=('cert.pem', 'key.pem'))

import serial
import pipes
import threading
from io_blueprint import IOBlueprint
from flask_socketio import SocketIO, emit

t = pipes.Template()
# t.append('tr a-z A-Z 0-9', '--')

ledSocket =  IOBlueprint('/led')
# ser = serial.Serial('/dev/ttyUSB2', 115200)


@ledSocket.on('led')
def echo(msg):
    f = t.open('pipes/enigme', 'w')
    f.write("enigme--"+str(reponse['id'])+"--"+reponse['action']+"--"+reponse['auto'])
    f.close()
    print(t.open('pipefile', 'r').read())
    i = 0
    colorled = 22200
    while i < 99:
        colorled += 1
        print(str(colorled))
        ser.write(str(colorled).encode())
        i += 1
    emit('enigme', reponse, namespace='/enigme')

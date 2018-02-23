import serial
import pipes
import threading
from io_blueprint import IOBlueprint
from flask_socketio import SocketIO, emit

t = pipes.Template()
# t.append('tr a-z A-Z 0-9', '--')

enigmeSocket =  IOBlueprint('/enigme')
# ser = serial.Serial('/dev/ttyUSB2', 115200)

def infoenigmes():
    with t.open('pipes/enigme_0', 'r') as f:
        command = f.read().split('--')
    return '{"enigme_0": "'+str(command[0])+'"}'



@enigmeSocket.on('enigme_0')
def enigme(reponse):
    with t.open('pipes/enigme_0', 'w') as f:
        f.write(reponse['action']+"--"+str(reponse['auto']))

@enigmeSocket.on('enigme_1')
def enigme(reponse):
    with t.open('pipes/enigme_1', 'r') as f:
        f.write(reponse['action']+"--"+str(reponse['auto']))
        # emit('0', f.read(), namespace='/enigme')
    emit('info', 'test', namespace='/enigme')


@enigmeSocket.on('info')
def enigme(reponse):
    print( infoenigmes())
    emit('info', infoenigmes(), namespace='/enigme')

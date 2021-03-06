import serial
import pipes
import threading
from io_blueprint import IOBlueprint
from flask import jsonify
from flask_socketio import SocketIO, emit

t = pipes.Template()

enigmeSocket =  IOBlueprint('/enigme')
# ser = serial.Serial('/dev/ttyUSB2', 115200)
test = []
def infoenigmes():
    with t.open('pipes/enigme_0', 'r') as f:
        enigme0 = f.read().split('--')
    with t.open('pipes/enigme_1', 'r') as f:
        enigme1 = f.read().split('--')
    with t.open('pipes/enigme_2', 'r') as f:
        enigme2 = f.read().split('--')
    with t.open('pipes/enigme_3', 'r') as f:
        enigme3 = f.read().split('--')

    return '{ \"enigme\": [\"'+str(enigme0[0])+'\", \"'+str(enigme1[0])+'\", \"'+str(enigme2[0])+'\", \"'+str(enigme3[0])+'\"] }'



@enigmeSocket.on('enigme_0')
def enigme(reponse):
    print(reponse)
    with t.open('pipes/enigme_0', 'w') as f:
        f.write(reponse['action']+"--"+str(reponse['auto']))

@enigmeSocket.on('enigme_1')
def enigme(reponse):
    with t.open('pipes/enigme_1', 'w') as f:
        f.write(reponse['action']+"--"+str(reponse['auto']))

@enigmeSocket.on('enigme_2')
def enigme(reponse):
    if reponse['action'] == "reload":
        with t.open('pipes/enigme_2', 'w') as f:
            f.write(reponse['action']+"--"+str(reponse['auto']+"--True"))
    else:
        with t.open('pipes/enigme_2', 'w') as f:
            f.write(reponse['action']+"--"+str(reponse['auto'])+"--false")

@enigmeSocket.on('enigme_3')
def enigme(reponse):
    if reponse['action'] == "reload":
        with t.open('pipes/enigme_3', 'w') as f:
            f.write("0--"+str(reponse['auto'])+"--True")
    else:
        with t.open('pipes/enigme_3', 'w') as f:
            f.write(reponse['action']+"--"+str(reponse['auto'])+"--false")

@enigmeSocket.on('info_enigme')
def enigme(reponse):
    emit('info_enigme', infoenigmes(), namespace='/enigme')

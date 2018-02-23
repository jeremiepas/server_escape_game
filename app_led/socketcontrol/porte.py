import serial
import pipes
import threading
from io_blueprint import IOBlueprint
from flask_socketio import SocketIO, emit

t = pipes.Template()
# t.append('tr a-z A-Z 0-9', '--')

porteSocket =  IOBlueprint('/porte')
# ser = serial.Serial('/dev/ttyUSB2', 115200)


@porteSocket.on('porte')
def enigme(reponse):
    reponse.get(id)
    emit('enigme', reponse, namespace='/enigme')

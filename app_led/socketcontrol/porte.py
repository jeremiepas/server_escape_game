import serial
import pipes
import threading
from io_blueprint import IOBlueprint
from flask_socketio import SocketIO, emit

t = pipes.Template()
# t.append('tr a-z A-Z 0-9', '--')

porteSocket =  IOBlueprint('/porte')
# ser = serial.Serial('/dev/ttyUSB2', 115200)

def infoportes():
    with t.open('pipes/porte_0', 'r') as f:
        porte0 = f.read().split('--')
    with t.open('pipes/porte_1', 'r') as f:
        porte1 = f.read().split('--')
    with t.open('pipes/porte_2', 'r') as f:
        porte2 = f.read().split('--')
    with t.open('pipes/porte_3', 'r') as f:
        porte3 = f.read().split('--')
    return '{"porte": ['+str(porte0[0])+', '+str(porte1[0])+', '+str(porte2[0])+', '+str(porte3[0])+']}'



@porteSocket.on('porte_0')
def porte(reponse):
    with t.open('pipes/porte_0', 'w') as f:
        f.write(reponse['action']+"--"+str(reponse['auto']))
@porteSocket.on('porte_1')
def porte(reponse):
    with t.open('pipes/porte_1', 'w') as f:
        f.write(reponse['action']+"--"+str(reponse['auto']))
@porteSocket.on('porte_2')
def porte(reponse):
    with t.open('pipes/porte_2', 'w') as f:
        p = f.read().split('--')
    with t.open('pipes/porte_2', 'w') as f:
        f.write(reponse['action']+"--"+str(reponse['auto'])+"--"+p[2])
@porteSocket.on('porte_3')
def porte(reponse):
        with t.open('pipes/porte_3', 'w') as f:
            p = f.read().split('--')
    with t.open('pipes/porte_3', 'w') as f:
        f.write(reponse['action']+"--"+str(reponse['auto']+"--"+p[2]))
@porteSocket.on('info_porte')
def enigme(reponse):
    emit('info_porte', infoportes(), namespace='/porte')

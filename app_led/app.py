from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room, Namespace

from socketcontrol.enigme import enigmeSocket
from socketcontrol.led import ledSocket
from socketcontrol.porte import porteSocket

from controller.led import Led
from controller.home import Home
import configparser

config = configparser.ConfigParser()
# config['DEFAULT'] = {'ServerAliveInterval': '45',
#                         'Compression': 'yes',
#                         'CompressionLevel': '9'}
config.read('./config.ini')
# port = config['DEFAULT']['port']

app = Flask(__name__, static_url_path='/static')
app.register_blueprint(Home, url_prefix='/')
app.register_blueprint(Led, url_prefix='/led')

socketio = SocketIO(app)

enigmeSocket.init_io(socketio)
porteSocket.init_io(socketio)
ledSocket.init_io(socketio)

if __name__ == '__main__':
    socketio.run("0.0.0.0", port=5000)

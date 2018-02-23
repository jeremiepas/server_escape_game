import serial
import smbus
import pipes
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

# ser = serial.Serial('/dev/ttyUSB0', 115200)
t = pipes.Template()

bus = smbus.SMBus(1)
address = 0x05

with t.open('pipes/enigme_0', 'w') as f:
    f.write('0--True')
with t.open('pipes/enigme_1', 'w') as f:
    f.write('0--True')

def writeNumber(value):
    bus.write_byte(address, value)
    return -1
def readNumber():
    number = bus.read_byte(address)
    return number

#def enigme(id, action, auto):

def enigme_0():
    with t.open('pipes/enigme_0', 'r') as f:
        command = f.read().split('--')
        print(command)
    if command[1] == "True":
        GPIO.output(12, readNumber())
        print(readNumber())
        with t.open('pipes/enigme_0', 'w') as f:
            f.write(str(readNumber())+"--True")
    if command[1] == "false":
        GPIO.output(12, int(command[0]))

def enigme_1():
    with t.open('pipes/enigme_1', 'r') as f:
        command = f.read().split('--')
    if command[1] == "True":
        GPIO.output(12, readNumber())
        print(readNumber())
        with t.open('pipes/enigme_1', 'w') as f:
            f.write(str(readNumber())+"--True")
    if command[1] == "false":
        GPIO.output(12, int(command[0]))

while True:
    enigme_0()
    time.sleep( 1 )

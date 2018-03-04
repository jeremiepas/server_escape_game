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
address0 = 0x05
address1 = 0x06
address2 = 0x07
address3 = 0x08
trap     = 0x11
prote_1  = 0x12
porte_3  = 0x13
with t.open('pipes/enigme_0', 'w') as f:
    f.write('0--True') #valeur,  mode-auto
with t.open('pipes/enigme_1', 'w') as f:
    f.write('0--True') #valeur,  mode-auto
with t.open('pipes/enigme_2', 'w') as f:
    f.write('0--True') #valeur,  mode-auto
with t.open('pipes/enigme_3', 'w') as f:
    f.write('0--True--false') # valeur,  mode-auto, restart enigme

def writeNumber(address, value):
    try:
        bus.write_byte(address, value)
        return 1
    except OSError as e:
        return -1
def readNumber(address):
    try:
        number = bus.read_byte(address)
        return number
    except OSError as e:
        return -1



def enigme_0():
    with t.open('pipes/enigme_0', 'r') as f:
        command = f.read().split('--')
        print(command)
    if command[1] == "True":
        GPIO.output(12, readNumber(address0))
        with t.open('pipes/enigme_0', 'w') as f:
            f.write(str(readNumber(address0))+"--True")
    if command[1] == "false":
        GPIO.output(12, int(command[0]))

def enigme_1():
    with t.open('pipes/enigme_1', 'r') as f:
        command = f.read().split('--')
    if command[1] == "True":
        GPIO.output(12, readNumber(address1))
        with t.open('pipes/enigme_1', 'w') as f:
            f.write(str(readNumber(address1))+"--True")
    if command[1] == "false":
        GPIO.output(12, int(command[0]))

def enigme_3():
    with t.open('pipes/enigme_3', 'r') as f:
        command = f.read().split('--')
        print(command)
        print(readNumber(address3))

    if command[0] == '-1':
        with t.open('pipes/enigme_3', 'w') as f:
            f.write(str(readNumber(address3))+"--True--false")
    else:
        if command[1] == "True":
            with t.open('pipes/enigme_3', 'w') as f:
                f.write(str(readNumber(address3))+"--True--false")
        if command[1] == "false":
            writeNumber(address3, int((command[0] == 1)if 3 else command[0] ))
        if command[2] == "True":
            writeNumber(address3, int(2))
            with t.open('pipes/enigme_3', 'w') as f:
                f.write(str(readNumber(address3))+"--True--false")

while True:
    # enigme_0()
    enigme_3()
    time.sleep( 1 )

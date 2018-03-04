import serial
import smbus
import pipes
import time
import RPi.GPIO as GPIO
import api_i2c.porte_0 as Porte
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

# ser = serial.Serial('/dev/ttyUSB0', 115200)
t = pipes.Template()
porte = Porte.Porte()

bus = smbus.SMBus(1)
address0 = 0x05
address1 = 0x06
address2 = 0x07
address3 = 0x08

# porte_0  = 0x11 # trape apres enigme_1
porte_1  = 0x12 # trape clavier lazer
porte_2  = 0x13 # porte salle 1 -> salle 2
porte_3  = 0x14 # porte salle 2 -> salle 3

led_0 = 0x21 # led salle une couleur blanc joune puis couleur rouge
led_2 = 0x22 # led salle 3 couleur bleu

with t.open('pipes/enigme_0', 'w') as f:
    f.write('0--True') #valeur,  mode-auto
with t.open('pipes/enigme_1', 'w') as f:
    f.write('0--True') #valeur,  mode-auto
with t.open('pipes/enigme_2', 'w') as f:
    f.write('0--True') #valeur,  mode-auto
with t.open('pipes/enigme_3', 'w') as f:
    f.write('0--True--false') # valeur,  mode-auto, restart enigme

with t.open('pipes/porte_0', 'w') as f:
    f.write('0--True--0') #valeur,  mode-auto
with t.open('pipes/porte_1', 'w') as f:
    f.write('0--True') #valeur,  mode-auto
with t.open('pipes/porte_2', 'w') as f:
    f.write('0--True') #valeur,  mode-auto
with t.open('pipes/porte_3', 'w') as f:
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
            writeNumber(address3, int(command[0]))
        if command[2] == "True":
            writeNumber(address3, int(2))
            with t.open('pipes/enigme_3', 'w') as f:
                f.write(str(readNumber(address3))+"--True--false")


while True:
    porte.porte_A()
    # enigme_0()
    enigme_3()
    time.sleep( 1 )

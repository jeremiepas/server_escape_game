import smbus
import pipes
import time

class Porte:
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.porte_0  = 0x11 # trape apres enigme_1
        with t.open('pipes/porte_0', 'w') as f:
            f.write('0--True--') # valeur,  mode-aut, valeur-enigme
    def porte_0():
        with t.open('pipes/porte_0', 'r') as f:
            command = f.read().split('--')
            print(command)
        if command[1] == "True":
            GPIO.output(12, readNumber(address0))
            with t.open('pipes/porte_0', 'w') as f:
                f.write(str(readNumber(address0))+"--True--"+str(command[2]))
        if command[1] == "false":
            GPIO.output(12, int(command[0]))


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
import smbus
import pipes
import time

bus = smbus.SMBus(1)

class Porte:
    def __init__(self):
        self.t = pipes.Template()
        self.porte_0  = 0x11 # trape apres enigme_1
        self.porte_1  = 0x12 # trape clavier
        self.porte_2  = 0x13 # porte salle 1 -> 2
        self.porte_3  = 0x14 # porte salle 2 -> 3
        with self.t.open('pipes/porte_0', 'w') as f:
            f.write('0--True--0') # valeur,  mode-aut, valeur-enigme
        with self.t.open('pipes/porte_1', 'w') as f:
            f.write('0--True--0') # valeur,  mode-aut, valeur-enigme
        with self.t.open('pipes/porte_2', 'w') as f:
            f.write('0--True--0') # valeur,  mode-aut, valeur-enigme
        with self.t.open('pipes/porte_3', 'w') as f:
            f.write('0--True--0') # valeur,  mode-aut, valeur-enigme
    def trape_A(self):
        with self.t.open('pipes/porte_0', 'r') as f:
            command = f.read().split('--')
        if command[1] == "True":
            # writeNumber(self.porte_0, int(command[2]))
            with self.t.open('pipes/porte_0', 'w') as f:
                f.write(str(readNumber(self.porte_0))+"--True--")

        if command[1] == "false":
            writeNumber(self.porte_0, int(command[0]))
            with self.t.open('pipes/porte_0', 'w') as f:
                f.write(str(readNumber(self.porte_0))+"--True--")

    def trape_B(self):
        with self.t.open('pipes/porte_1', 'r') as f:
            command = f.read().split('--')
        if command[1] == "True":
            # writeNumber(self.porte_0, int(command[2]))
            with self.t.open('pipes/porte_1', 'w') as f:
                f.write(str(readNumber(self.porte_1))+"--True--")

        if command[1] == "false":
            writeNumber(self.porte_1, int(command[0]))
            with self.t.open('pipes/porte_1', 'w') as f:
                f.write(str(readNumber(self.porte_1))+"--True--")
    def porte_A(self):
        with self.t.open('pipes/porte_2', 'r') as f:
            command = f.read().split('--')
        if command[1] == "True":
            writeNumber(self.porte_2, int(command[2]))
            with self.t.open('pipes/porte_2', 'w') as f:
                f.write(str(readNumber(self.porte_2))+"--True--"+str(command[2]))

        if command[1] == "false":
            writeNumber(self.porte_2, int(command[0]))
            with self.t.open('pipes/porte_2', 'w') as f:
                f.write(str(readNumber(self.porte_2))+"--True--"+str(command[0]))
    def porte_B(self):
        with self.t.open('pipes/porte_3', 'r') as f:
            command = f.read().split('--')
        if command[1] == "True":
            writeNumber(self.porte_3, int(command[2]))
            with self.t.open('pipes/porte_3', 'w') as f:
                f.write(str(readNumber(self.porte_3))+"--True--"+str(command[2]))

        if command[1] == "false":
            writeNumber(self.porte_3, int(command[0]))
            with self.t.open('pipes/porte_3', 'w') as f:
                f.write(str(readNumber(self.porte_3))+"--True--"+str(command[2]))

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

import serial
import smbus
import pipes
import time
import RPi.GPIO as GPIO
import api_i2c.enigme as enigme_3
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

porte_0  = 0x11 # trape apres enigme_1
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



while True:
    # enigme_0()
    enigme_3()
    porte_0()
    time.sleep( 1 )

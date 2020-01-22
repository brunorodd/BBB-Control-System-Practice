#Copyright  Bruno Rodriguez 2019
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM  as PWM
from Adafruit_BBIO.SPI import SPI
import time
from eStop import e_stop, release 

int_bits = 32
cs1 = "P9_23"
cs2 = "P9_27"

#it should be noted that this function only works with numbers that are less than or equal to  2 bytes in length
def highByte(num):
    num = int(num)
    length = num.bit_length()
    if length < 8:
        return 0
    high = num >>  8 # -8 because thats many bits there are in a byte
    high = high & 0xFF
    return high

def lowByte(num):
    num = int(num)
    return num & 0xFF


def write4921(value, SPI, cs_pin):
    value = int(value)
    GPIO.output(cs_pin, GPIO.LOW)
    data = highByte(value)
    data = 0b00001111 & data
    data = 0b00110000 | data
    print "data as is: {}".format(data)
    print "data as a list {}".format([data])
    print (SPI.xfer2([data]))
    data = 0xFF & value
    SPI.xfer2([data])
    GPIO.output(cs_pin, GPIO.HIGH)

# main script setup
#Sets up the slave select 1
GPIO.setup(cs1, GPIO.OUT)
GPIO.output(cs1, GPIO.HIGH)

#Sets up the slave select 2
GPIO.setup(cs2, GPIO.OUT)
GPIO.output(cs2, GPIO.HIGH)

spi1 = SPI(1,0)
spi2 = SPI(2,0)
spi1.msh = 10500000
spi2.msh = 10500000
spi1.cshigh = False 
spi2.cshigh = False
release()

def center(value):
    write4921(value, spi1, cs1)
    write4921(value, spi2, cs2)

def spi_write(speed, direction):
    write4921(speed, spi2, cs2) #in testing right now
    write4921(direction, spi1, cs1)
    
# spi1, spi2 = spi_setup()
# center(830)
# while True:
#     analogValue = raw_input("DAC Input 1: ")
#     analogValue2 = raw_input("DAC Input 2: ")
#     if (analogValue == "" or analogValue2 == ""):
#         e_stop()
#     else:
#         write4921(int(analogValue2), spi2, cs2) #in testing right now
#         write4921(int(analogValue), spi1, cs1)
#         time.sleep(2)

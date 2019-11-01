#Copyright Bruno Rodriguez 2019
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM  as PWM
from Adafruit_BBIO.SPI import SPI
import time

int_bits = 32
cs1 = "P9_23"
cs2 = "P9_27"

#it should be noted that this function only works with numbers that are less than or equal to  2 bytes in length 
def highByte(num):
    length = num.bit_length()
    if length < 8:
        return 0
    high = num >>  8 # -8 because thats many bits there are in a byte 
    high = high & 0xFF
    return high

def lowByte(num):
    return num & 0xFF


def write4921(value, SPI, cs_pin):
    GPIO.output(cs_pin, GPIO.LOW)
    data = highByte(value)
    data = 0b00001111 & data
    data = 0b00110000 | data
    SPI.xfer2([data])
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
spi1.cshigh = True
spi2.cshigh = True
while True:
    analogValue = 2048
    analogValue2 = 1024
    write4921(analogValue2, spi2, cs2) #in testing right now
    write4921(analogValue, spi1, cs1)
    time.sleep(2)


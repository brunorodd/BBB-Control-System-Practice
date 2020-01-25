import time
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.ADC as ADC
from BBB_ADC import adc_return, adc_return_raw
#from BBB_SPI import center, spi_write
from calibrate import calib

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
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

def center(value):
    write4921(value, spi1, cs1)
    write4921(value, spi2, cs2)

def spi_write(speed, direction):
    write4921(speed, spi2, cs2) #in testing right now
    write4921(direction, spi1, cs1)


int_bits = 32
cs1 = "P9_23"
cs2 = "P9_27"


ADC.setup()
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

spi_write(845, 845)

#center(830)
speed_in, direction_in, center = calib()
direction_out = [650, 990]
speed_out = [650, 990]
print speed_in, direction_in, center

while True:
    analog1, analog2 = adc_return_raw()
    print(analog1, analog2)
    out1 = map_value (analog1, speed_in[0], speed_in[1], speed_out[0], speed_out[1])

    out2 = map_value(analog2, direction_in[0], direction_in[1], direction_out[0], direction_out[1])

    print(out1, out2)

    spi_write(out1, out2)

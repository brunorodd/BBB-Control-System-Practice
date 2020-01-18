import time
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.SPI import SPI

cs1 = "P9_23"
cs2 = "P9_27"

spi1 = SPI(1,0)
spi2 = SPI(2,0)
spi1.msh = 10500000
spi2.msh = 10500000
spi1.cshigh = False
spi2.cshigh = False 


GPIO.setup(cs1, GPIO.OUT)
GPIO.output(cs1, GPIO.HIGH)
#Sets up the slave select 2
GPIO.setup(cs2, GPIO.OUT)
GPIO.output(cs2, GPIO.HIGH)


# extracts the high byte of a number, used to communicate with the DAC
def highByte(num):
    length = num.bit_length()
    if length < 8:
        return 0
    high = num >>  8 # 8 because thats many bits there are 8 bits in a byte
    high = high & 0xFF
    return high


def write4921(value, SPI, cs_pin):
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



while True:
    analogValue = 2048
    analogValue2 = 2048
    write4921(analogValue2, spi2, cs2) 
    write4921(analogValue, spi1, cs1)
    #time.sleep(.001)

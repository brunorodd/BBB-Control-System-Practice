import time
import math
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
from  Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.GPIO as GPIO

cs1 = "P9_23"
cs2 = "P9_27"
pwm_pin1 = "P9_14"
pwm_pin2 = "P9_16"
pwm_pin3 = "P9_42"
ADC_pin1 = "P9_33"
ADC_pin2 = "P9_35"
TX_pin = "P9_41"

segA = "P8_7"
segB = "P8_8"

joystickCenterList = [0,0,0,0,0,0,0,0,0,0]
joystickForwardList = [0,0,0,0,0,0,0,0,0,0]
joystickBackwardsList = [0,0,0,0,0,0,0,0,0,0]
joystickLeftList = [0,0,0,0,0,0,0,0,0,0]
joystickRightList = [0,0,0,0,0,0,0,0,0,0]

clbCenter = [0,0]


def write4921(value, SPI, cs_pin):
    GPIO.output(cs_pin, GPIO.LOW)
    data = highByte(value)
    data = 0b00001111 & data
    data = 0b00110000 | data                    
    SPI.xfer2([data])
    data = 0xFF & value
    SPI.xfer2([data])
    GPIO.output(cs_pin, GPIO.HIGH)

def highByte(num):
    length = num.bit_length()
    if length < 8:
        return 0
    high = num >>  8 # -8 because thats many bits there are in a byte 
    high = high & 0xFF
    return high

def lowByte(num):
    return num & 0xFF

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
          
def rounder(x, base=5):
     return int(base * round(float(x)/base))

def calib(pin, index):
    length = len(lister)
    calibration_flag = True
    recalibration = True
    # for calibrating the center
    if index == 0:
        while calibration_flag:
            recalibration = False
            print("Calibrating Center Joystick...")
            time.sleep(3)
            for i in range(length):
                if abs(joystickSpeed[i]-joystickSpeed[i-1]) > 10 or abs(joystic:
                    print("Error in Calibration. Recalibrating...")
                    recalibration = True
                    time.sleep(1)
                    break
                joystickCenter.append(ADC.read_raw(pin))
                print(joystickCenter[i])
                time.sleep(0.5)

            if recalibration:
                continue
            else:
                calibration_flag = False
        
        return [sum(joystickCenter)/len(joystickCenter),sum(joystickDirection)/len(joystickDirection)]

    if index == 1:
        

            


                


GPIO.setup(cs1, GPIO.OUT)
GPIO.output(cs1, GPIO.HIGH)
#Sets up the slave select 2
GPIO.setup(cs2, GPIO.OUT)
GPIO.output(cs2, GPIO.HIGH)

# ADC Enable
ADC.setup()

# SPI Enable
spi1 = SPI(1,0)
spi2 = SPI(2,0)
spi1.msh = 10500000
spi2.msh = 10500000
spi1.cshigh = True
spi2.cshigh = True



while True:
    clbCenter = calib(ADC_pin1, 0)
    joystickSpeed = ADC.read_raw(ADC_pin1)
    joystickDirection = ADC.read_raw(ADC_pin2)
    

    print(joystickSpeed)
    print(joystickDirection)
    print("")
    
    joystickSpeed = map_value(joystickSpeed, 1700, 2680, 640, 1040)
    joystickDirection = map_value(joystickDirection, 1700, 2750, 640, 1040)
    
    joystickSpeed = rounder(int(joystickSpeed))
    joystickDirection = rounder(int(joystickDirection))
    
    

    print(joystickSpeed)
    print(joystickDirection)
    write4921(joystickSpeed, spi1, cs1)
    write4921(joystickDirection, spi2, cs2)
    time.sleep(2)


#while True:
"""    analogValue = 2048
    analogValue2 = 2048
    write4921(analogValue2, spi2, cs2) #in testing right now
    write4921(analogValue, spi1, cs1)
    time.sleep(2)"""




import time
import math
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
from Adafruit_BBIO.SPI import SPI
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

joystickCenter1 = [0]
joystickCenter2 = [0]
joystickForward = [0]
joystickBackward = [0]
joystickLeft = [0]
joystickRight = [0]
joystickDirectionList = [0]
joystickSpeedList = [0]

clbCenter = [0]


def write4921(value, SPI, cs_pin):
    GPIO.output(cs_pin, GPIO.LOW)
    data = highByte(value)
    data = 0b00001111 & data
    data = 0b00110000 | data                    
    SPI.xfer2([data])
    data = 0xFF & value
    SPI.xfer2([data])
    GPIO.output(cs_pin, GPIO.HIGH)

# extracts the high byte of a number, used to communicate with the DAC
def highByte(num):
    length = num.bit_length()
    if length < 8:
        return 0
    high = num >>  8 # 8 because thats many bits there are 8 bits in a byte 
    high = high & 0xFF
    return high

def lowByte(num):
    return num & 0xFF

#this function just maps a set of values to another
def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
          
#this function rounds to the nearest fifth of a number
def rounder(x, base=5):
     return int(base * round(float(x)/base))

#this is the main calibration function which calibrates the center, direction and speed values
def calib(index):
    length = 50
    calibration_flag = True
    recalibration = False
    # for calibrating the center
    if index == 0:
        while calibration_flag:
            del joystickCenter1
            del joystickCenter2
            joystickCenter1 = []
            joystickCenter2 = []
            recalibration = False
            print("Calibrating Joystick Center...")
            input("Center the joystick and press Enter to continue: ")
            time.sleep(0.5)
            for i in range(length):
                if abs(joystickCenter1[i]-joystickCenter1[i-1]) > 10 or abs(joystickCenter2[i]-joystickCenter2[i-1]) > 10:
                    print("Error in Calibration. Recalibrating...")
                    recalibration = True
                    time.sleep(1)
                    break
                joystickCenter1.append(ADC.read_raw(ADC_pin1))
                joystickCenter2.append(ADC.read_raw(ADC_pin2))
                print(joystickCenter1[i])
                print(joystickCenter2[i])
                time.sleep(0.05)

            if recalibration:
                continue
            else:
                calibration_flag = False
                break
        
        return [sum(joystickCenter1)/len(joystickCenter1),sum(joystickCenter2)/len(joystickCenter2)]

# for calibrating the upper and lower bounds of each direction to map 
    if index == 1:
        while calibration_flag:
            joystickForward[:] = []
            #joystickForward = []
            recalibration = False
            print("Calibrating Direction Threshold. Hold the Joystick all the way forward")
            input("Press Enter to Continue: ")
            time.sleep(0.5)
            for i in range(length-1):
                if abs(joystickForward[i+1]-joystickForward[i]) > 10:
                    print("Error in Calibration. Recalibrating...")
                    recalibration = True
                    time.sleep(1)
                    break
                joystickForward.append(ADC.read_raw(ADC_pin2))
                print(joystickForward[i])
                time.sleep(0.05)
            
            if recalibration:
                continue
            else:
                calibration_flag = False
                break
        # returns the average of the maximum values for the forward direction
        return sum(joystickForward)/length


    if index == 2:
        while calibration_flag:
            joystickBackward[:] = []
            recalibration = False
            print("Calibrating Direction Threshold. Hold the Joystick all the way backward")
            input("Press Enter to Continue")
            time.sleep(0.5)
            for i in range(length):
                if abs(joystickBackward[i]-joystickBackward[i-1]) > 10:
                    print("Error in Calibration. Recalibrating...")
                    recalibration = True
                    time.sleep(1)
                    break
                joystickBackward.append(ADC.read_raw(ADC_pin2))
                print(joystickBackward[i])
                time.sleep(0.05)

            if recalibration:
                continue
            else:
                calibration_flag = False
                break
        #returns the average of the maximum values for the backward direction 
        return sum(joystickBackward)/length

    if index == 3:
        while calibration_flag:
            joystickLeft[:] = []
            recalibration = False
            print("Calibrating Speed threshold. Hold the joystick all the way left")
            input("Press Enter to Continue")
            time.sleep(0.5)
            for i in range(length):
                if abs(joystickLeft[i]-joystickLeft[i-1]) > 10:
                    print("Error in Calibration. Recalibrating...")
                    recalibration = True
                    time.sleep(1)
                    break
                joystickLeft.append(ADC.read_raw(ADC_pin1))
                print(joystickLeft[i])
                time.sleep(0.05)

            if recalibration:
                continue
            else:
                calibration_flag = False
                break
        #returns the average of the maximum values for the left direction
        return sum(joystickLeft)/length

    if index == 4:
        while calibration_flag:
            joystickRight[:] = []
            recalibration = False
            print("Calibratin Speed threshold. Hold the joystick all the way right")
            input("Press Enter to continue")
            time.sleep(0.5)
            for i in range(length):
                if abs(joystickRight[i]-joystickRight[i-1]) > 10:
                    print("Error in Calibration. Recalibrating...")
                    recalibration = True
                    time.sleep(1)
                    break
                joystickRight.append(ADC.read_raw(ADC_pin1))
                print(joystickLeft[i])
                time.sleep(0.05)
            
            if recalibration:
                continue
            else:
                calibration_flag = False
                break
        return sum(joystickRight)/length





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

    
    joystickForwardMax = calib(1)
    joystickBackwardMax = calib(2)
    joystickLeftMax = calib(3)
    joystickRightMax = calib(4) #obtains the maximum value for the Right Direction 
    

    joystickSpeed = ADC.read_raw(ADC_pin1)
    joystickDirection = ADC.read_raw(ADC_pin2)
    
    print(joystickDirection)
    print("")
   
   # this calibrates the center until it is fully calibrated
    while center_calibrated == False:
        clbCenter = calib(0)
        print("Recenter the Joystick")
        time.sleep(3)
        print(joystickDirection)
        print(joystickSpeed)
        input("Press Enter to continue")
        if abs(joystickDirection-clbCenter[0]) > 10 or abs(joystickSpeed-clbCenter[1]) > 10:
            print("Error. Restarting Recentering")
            q=input("Press Enter")
            continue
        else:
            center_calibrated = True
    
    
    joystickSpeed = map_value(joystickSpeed, joystickForwardMax, joystickBackwardMax, 640, 1040)
    joystickDirection = map_value(joystickDirection, joystickLeftMax, joystickRightMax, 640, 1040)
    
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




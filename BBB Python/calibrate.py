import time
import math
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.GPIO as GPIO

cs1 = "P9_23"
cs2 = "P9_27"
ADC_pin1 = "P9_33"
ADC_pin2 = "P9_35"
TX_pin = "P9_41"
ADC.setup()

calib_length = 50
speed_in = [0, 0]
direction_in = [0, 0]
center = [0, 0]

jsCenter1 = []
jsCenter2 = []
jsLeft = []
jsRight = []
jsForward = []
jsBackward = []

def calib_center():
    print("Calibrating Center...")
    raw_input("Center the joystick and press Enter to continue: ")
    time.sleep(0.5)
    for i in range(calib_length):
        jsCenter1.append(ADC.read_raw(ADC_pin1))
        jsCenter2.append(ADC.read_raw(ADC_pin2))
    center[0] = sum(jsCenter1) / len (jsCenter1)
    center[1] = sum(jsCenter2) / len(jsCenter2)

def calib_left():
    print("Calibrating Left...")
    raw_input("Move joystick to Left and press Enter to continue: ")
    time.sleep(0.5)
    for i in range(calib_length):
        jsLeft.append(ADC.read_raw(ADC_pin2))
    direction_in[0] = sum(jsLeft) / len(jsLeft)


def calib_right():
    print("Calibrating Right...")
    raw_input("Move joystick to Right and press Enter to continue: ")
    time.sleep(0.5)
    for i in range(calib_length):
        jsRight.append(ADC.read_raw(ADC_pin2))
    direction_in[1] = sum(jsRight) / len(jsRight)


def calib_forward():
    print("Calibrating Forward..")
    raw_input("Move joystick Forward  and press Enter to continue: ")
    time.sleep(0.5)
    for i in range(calib_length):
        jsForward.append(ADC.read_raw(ADC_pin1))
    speed_in[1] = sum(jsForward) / len(jsForward)


def calib_backward():
    print("Calibrating Backward..")
    raw_input("Move joystick Backward  and press Enter to continue: ")
    time.sleep(0.5)
    for i in range(calib_length):
        jsBackward.append(ADC.read_raw(ADC_pin1))
    speed_in[0] = sum(jsBackward) / len(jsBackward)

def calib():
    print("Entered Calibration Mode")
    calib_center()
    calib_left()
    calib_right()
    calib_forward()
    calib_backward()
    return speed_in, direction_in, center 

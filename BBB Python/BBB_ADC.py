import Adafruit_BBIO.ADC as ADC
import time


ADC_pin1 = "P9_33" 
ADC_pin2 = "P9_35"

def adc_read():
    print "ADC pin 1: {}".format( ADC.read(ADC_pin1))
    print "ADC pin 1 RAW: {}".format( ADC.read_raw(ADC_pin1))
    print("")
    print "ADC pin 2: {} ".format( ADC.read(ADC_pin2))
    print "ADC pin 2 RAW: {}".format( ADC.read_raw(ADC_pin2))
    print("")
    print("")
    time.sleep(1)

def adc_return():
    return (ADC.read(ADC_pin1), ADC.read(ADC_pin2))

def adc_return_raw():
    return (ADC.read_raw(ADC_pin1), ADC.read_raw(ADC_pin2))

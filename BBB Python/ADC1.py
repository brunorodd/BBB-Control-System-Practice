import Adafruit_BBIO.ADC as ADC
import time

ADC_pin1 = "P9_33" 
ADC_pin2 = "P9_35"
ADC.setup()

while True:
    print "ADC pin 1: {}".format(round( ADC.read(ADC_pin1), 4))
    print "ADC pin 1 RAW: {}".format(round( ADC.read_raw(ADC_pin1), 4))
    print ("")
    time.sleep(1)

import Adafruit_BBIO.ADC as ADC
import time

ADC_pin1 = "P9_33" 
ADC_pin2 = "P9_35"
ADC.setup()

while True:
    print "ADC pin 2: {} ".format( ADC.read(ADC_pin2))
    print "ADC pin 2 RAW: {}".format( ADC.read_raw(ADC_pin2))
    print("")
    time.sleep(1)

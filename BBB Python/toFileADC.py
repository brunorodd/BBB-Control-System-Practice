import Adafruit_BBIO.ADC as ADC
import time

ADC_pin1 = "P9_33" 
ADC_pin2 = "P9_35"
ADC.setup()
f = open("adcValues.txt", "w")

for i in range(100):
    f.write( "ADC pin 1: {}".format( ADC.read(ADC_pin1)))
    f.write("\n")
    f.write( "ADC pin 1 RAW: {}".format( ADC.read_raw(ADC_pin1)))
    f.write("\n")
    f.write( "ADC pin 2: {} ".format( ADC.read(ADC_pin2)))
    f.write("\n")
    f.write( "ADC pin 2 RAW: {}".format( ADC.read_raw(ADC_pin2)))
    f.write("\n")
    f.write("\n")
    time.sleep(1)
f.close()

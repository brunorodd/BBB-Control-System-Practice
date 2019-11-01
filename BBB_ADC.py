import Adafruit_BBIO.ADC as ADC
import time

ADC_pin1 = "P9_33" 
ADC_pin2 = "P9_35"
ADC.setup()

while True:
    print(ADC.read(ADC_pin1))
    print(ADC.read_raw(ADC_pin1))
    print("")
    print(ADC.read(ADC_pin2))
    print(ADC.read_raw(ADC_pin2))
    print("")
    print("")
    time.sleep(3)

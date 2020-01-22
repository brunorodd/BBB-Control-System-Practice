import time
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.SPI as SPI
import Adafruit_BBIO.ADC as ADC
from BBB_ADC import adc_return, adc_return_raw
from BBB_SPI import center, spi_write
from calibrate import calib

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


ADC.setup()

center(830)
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

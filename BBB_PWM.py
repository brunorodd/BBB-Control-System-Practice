import Adafruit_BBIO.PWM as PWM
import time

pwm_pin = "P9_16"


PWM.start(pwm_pin, 0, 1000)# EHRPWM1B

while True:
    voltage = input("Enter Voltage Level: ")
    DC_sim = voltage/3.365*100
    if DC_sim > 100:
        DC_sim = 100
    PWM.set_duty_cycle(pwm_pin, DC_sim)

PWM.stop(pwm_pin)
PWM.cleanup()

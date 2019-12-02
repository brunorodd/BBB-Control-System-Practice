import Adafruit_BBIO.PWM as PWM
import time

pwm_pin1 = "P9_16"
pwm_pin2 = "P9_14"
pwm_pin3 = "P9_42"


PWM.start(pwm_pin1, 0, 1000)# EHRPWM1B
PWM.start(pwm_pin2, 0, 1000)
PWM.start(pwm_pin3, 0, 1000)

voltage = 2.6
voltage2 = 2.6

DC_sim = voltage/3.365*100
DC_sim2 = voltage2/3.365*100

PWM.set_duty_cycle(pwm_pin1, DC_sim)
PWM.set_duty_cycle(pwm_pin2, DC_sim2)
while True:
    voltage = input("Enter Voltage Level: ")
    voltage2 = input("Enter 2nd Voltage: ")

    DC_sim2 = voltage2/3.365*100
    DC_sim = voltage/3.365*100

    if DC_sim > 100 or DC_sim2 > 100:
        DC_sim = 100
        DC_sim2 = 100

    PWM.set_duty_cycle(pwm_pin1, DC_sim)
    PWM.set_duty_cycle(pwm_pin2, DC_sim2)
    
PWM.stop(pwm_pin)
PWM.stop(pwm_pin2)
PWM.cleanup()

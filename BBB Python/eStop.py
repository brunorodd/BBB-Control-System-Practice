import Adafruit_BBIO.GPIO as GPIO

def e_stop():
    GPIO.setup("P8_42", GPIO.OUT)
    GPIO.output("P8_42", GPIO.HIGH)

def release():
    GPIO.setup("P8_42", GPIO.OUT)
    GPIO.output("P8_42", GPIO.LOW)

e_stop()

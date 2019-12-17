import Adafruit_BBIO.GPIO as GPIO

#common anode pins
GPIO.setup("P8_46", GPIO.OUT)
GPIO.setup("P8_37", GPIO.OUT)

#the rest of the anode pins
GPIO.setup("P8_38", GPIO.OUT)
GPIO.setup("P8_39", GPIO.OUT)
GPIO.setup("P8_40", GPIO.OUT)
GPIO.setup("P8_41", GPIO.OUT)
GPIO.setup("P8_42", GPIO.OUT)
GPIO.setup("P8_43", GPIO.OUT)
GPIO.setup("P8_44", GPIO.OUT)
GPIO.setup("P8_45", GPIO.OUT)

GPIO.output("P8_46", GPIO.HIGH)
GPIO.output("P8_37", GPIO.HIGH)

# prints out an 8 on the hex display with the decimal point
GPIO.output("P8_38", GPIO.LOW)
GPIO.output("P8_39", GPIO.LOW)
GPIO.output("P8_40", GPIO.LOW)
GPIO.output("P8_41", GPIO.LOW)
GPIO.output("P8_42", GPIO.LOW)
GPIO.output("P8_43", GPIO.LOW)
GPIO.output("P8_44", GPIO.LOW)
GPIO.output("P8_45", GPIO.LOW)
#GPIO.output("P8_37", GPIO.LOW)


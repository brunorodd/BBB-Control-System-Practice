import math
import time
     
import Adafruit_CharLCD as LCD

# BeagleBone Black configuration:
lcd_rs        = 'P8_8'
lcd_en        = 'P8_10'
lcd_d4        = 'P8_18'
lcd_d5        = 'P8_16'
lcd_d6        = 'P8_14'
lcd_d7        = 'P8_12'
lcd_backlight = 'P8_7'

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, [lcd_d4, lcd_d5, lcd_d6, lcd_d7])
lcd.begin(16,2)

lcd.home()
lcd.setCursor(1,2)

lcd.message("Hello")


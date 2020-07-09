import time
import RPi.GPIO as g
import Adafruit_CharLCD as LCD





# Raspberry Pi pin setup

lcd_rs = 25

lcd_en = 24

lcd_d4 = 23

lcd_d5 = 17

lcd_d6 = 18

lcd_d7 = 22

lcd_backlight = 2



# Define LCD column and row size for 16x2 LCD.

lcd_columns = 16

lcd_rows = 2


# setup RPIO

g.setmode(g.BCM)
g.setup(4, g.IN, pull_up_down = g.PUD_DOWN)


lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)



lcd.message('Hello\nworld!')

# Wait 5 seconds
time.sleep(3.0)
lcd.clear()

# count 
count = 0
goal_count = 30
lcd.message("please push \nbutton !")

while True:
    if g.input(4) == g.HIGH:
        lcd.clear()
        count += 1
        if count == goal_count: # Now Count == Goal_count
            break;
        lcd.message(f"Pushed == {count}\n[Goal = {goal_count}]", )
        time.sleep(.3)


# Wait 5 seconds
lcd.clear()

lcd.message('Goodbye\nWorld!')



time.sleep(5.0)

lcd.clear()

g.cleanup()

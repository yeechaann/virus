import RPi.GPIO as GPIO
import time
import numpy as np
import cv2
import Adafruit_CharLCD as LCD

##
GPIO.setmode(GPIO.BCM)



hand_cascade = cv2.CascadeClassifier('haarcascade_hand.xml')
cap = cv2.VideoCapture(0)

Motor = 5
GPIO.setup(Motor, GPIO.OUT)
p = GPIO.PWM(Motor, 50)
CNT = 0

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

lcd_columns = 16
lcd_rows = 2

max_count = 5

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns,
                           lcd_rows, lcd_backlight)

lcd.message("Please Put Your\nHands")

while True:
    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # camera setting

    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
    print(hands)
    
    if type(hands) == np.ndarray:
        lcd.clear()
        CNT = CNT +1
        lcd.set_cursor(3,0)
        lcd.message('0'*(10-((int((CNT / max_count) * 100)//10))))
        lcd.set_cursor(3,1)
        lcd.message('0'*(10-((int((CNT / max_count) * 100)//10))))
        
        
        p.start(2.5)
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        p.ChangeDutyCycle(15)
        time.sleep(0.5)
        

        
        
        
        if CNT >= max_count:
            lcd.clear()
            lcd.message("Please Replace")
            break;
        
        time.sleep(1)
            


GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()
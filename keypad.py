#keypad
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from RPLCD import i2c
import camera
#relay_pin1 = 7 # Relay control pin
lcd = i2c.CharLCD("PCF8574", 0x27)
lcd.clear()
#import camera
#GPIO.setup(relay_pin1, GPIO.OUT)
import time
lcd.clear()
def keypad():
MATRIX = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
ROW = [5, 6, 13, 19]
COL = [16, 20, 21]
for j in range(3):
GPIO.setup(COL[j], GPIO.OUT)

GPIO.output(COL[j], 1)
for i in range(4):
GPIO.setup(ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
password = "2580"
lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string("enter the")
lcd.cursor_pos = (1, 0)
lcd.write_string("password")
print("Enter the password")
max_attempts = 3
current_attempts = 0
entered_password = "" while True:
for j in range(3):
GPIO.output(COL[j], 0)
for i in range(4):
if GPIO.input(ROW[i]) == 0:
entered_password += str(MATRIX[i][j])
time.sleep(0.5)
GPIO.output(COL[j], 1)
if len(entered_password) == len(password):
if entered_password == password:
print("Password accepted!")
#GPIO.output(relay_pin1, GPIO.HIGH)
lcd.clear()
lcd.write_string("password ")
lcd.cursor_pos = (1, 4)
lcd.write_string("accepted")

time.sleep(1)
lcd.clear()
lcd.write_string("door is open")
photo_stream = camera.capture_photo()
camera.send_photo(photo_stream)
return True
break
else:
print("Incorrect password")
lcd.clear()
lcd.write_string("Incorrect")
lcd.cursor_pos = (1, 4)
lcd.write_string("password")
time.sleep(1)
lcd.clear()
lcd.write_string("re-enter the")
lcd.cursor_pos = (1, 4)
lcd.write_string("password")
current_attempts += 1
if current_attempts == max_attempts:
print("Max attempts reached")
photo_stream = camera.capture_photo()
camera.send_photo(photo_stream)
#camera.camera.close()
lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string("Max attempts ")
lcd.cursor_pos = (1, 0)
lcd.write_string("reached ")

#time.sleep(2)
lcd.clear()
lcd.write_string("wait 10 sec")
print("Wait for 10 seconds")
time.sleep(10)
lcd.clear()
lcd.write_string("press the button")
# return False
break
# exit(0)
print("Re-enter the password")
entered_password = ""
#maina

import time
import datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
from RPLCD import i2c
import camera
import keypadsensor
GPIO.setwarnings(False)
# Setup GPIO
GPIO.setmode(GPIO.BCM)
# LCD initialization
lcd = i2c.CharLCD("PCF8574", 0x27)
lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string("Press the button")

# Button setup
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

reset_button_state = True # Variable to keep track of reset button state

def handle_message(msg):
chat_id = msg['chat']['id']
command = msg['text']
print('Received: %s' % command)
if '2580' in command:
telegram_bot.sendMessage(chat_id, 'DOOR IS UNLOCKED')
lcd.clear()
lcd.write_string("door is open")
time.sleep(3)
photo_stream = camera.capture_photo()
camera.send_photo(photo_stream)
telegram_bot = telepot.Bot('7399602712:AAG3gZaeOvNcPiVI9ebsUWUNxzIvLRTwcrQ')
print(telegram_bot.getMe())
MessageLoop(telegram_bot, handle_message).run_as_thread()
print('Up and Running....')
try:
 while True:
# Button states
 button_state1 = GPIO.input(12)


 if button_state1 == GPIO.LOW:
 print("Button 1 pressed")
keypadsensor.keypad() # Call the keypad function

#lcd.clear()
 #lcd.cursor_pos = (0, 0)
 #lcd.write_string("Resetting...")
 #time.sleep(1)
 lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string("Press the button")
 # Additional reset functionality can be added here

 time.sleep(0.1)

except KeyboardInterrupt:
 GPIO.cleanup()
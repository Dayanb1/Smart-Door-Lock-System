#telegrambot
import time
import datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
from RPLCD import i2c
white = 8
lcd = i2c.CharLCD("PCF8574", 0x27)
now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def handle_message(msg):
chat_id = msg['chat']['id']
command = msg['text']

print('Received: %s' % command)
if '2580' in command:
GPIO.output(white, GPIO.HIGH)
lcd.write_string("door is open")
telegram_bot.sendMessage(chat_id, 'DOOR IS UNLOCKED')
time.sleep(3)
GPIO.output(white, GPIO.LOW)
lcd.write_string("press the button")
telegram_bot = telepot.Bot(' 7399602712:AAG3gZaeOvNcPiVI9ebsUWUNxzIvLRTwcrQ ')
print(telegram_bot.getMe())
MessageLoop(telegram_bot, handle_message).run_as_thread()
print('Up and Running....')
while True:
time.sleep(10)
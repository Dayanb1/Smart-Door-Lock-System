#lcd_display
from RPLCD import i2c
import time
def display_messages():
# Initialize I2C connection
lcd = i2c.CharLCD("PCF8574", 0x27)
# Set cursor position and display initial messages
lcd.cursor_pos = (0, 0)
lcd.clear()
lcd.write_string("Press the button")
lcd.cursor_pos = (1, 0)
lcd.write_string("1.Keypad")
# Delay between messages
time.sleep(2)
# Continuously display the two messages
while True:
lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string("Press the button")
lcd.cursor_pos = (1, 0)
lcd.write_string("1.Keypad")
time.sleep(2)
lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string("Press the button")
lcd.cursor_pos = (1, 0)
lcd.write_string("2.Fingerprint")
time.sleep(2)
# Call the display_messages() function
display_messages()
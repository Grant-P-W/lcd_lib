import time
import lcdlib as lcd

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Initialise display on pins and width
lcd.init(25,24,23,17,18,22,16)
 
while True:
 
  # Send some test
  lcd.string("Rasbperry Pi",LCD_LINE_1)
  lcd.string("16x2 LCD Test",LCD_LINE_2)
 
  time.sleep(3) # 3 second delay
 
  # Send some text
  lcd.string("1234567890123456",LCD_LINE_1)
  lcd.string("abcdefghijklmnop",LCD_LINE_2)
 
  time.sleep(3) # 3 second delay

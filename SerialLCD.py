from time import sleep
import serial
#Initialization Commands or Responses

SLCD_INIT   = [0xA3]
SLCD_INIT_ACK   = [0xA5]
SLCD_INIT_DONE  = [0xAA]

#WorkingMode Commands or Responses
SLCD_CONTROL_HEADER = [0x9F]
SLCD_CHAR_HEADER    = [0xFE]
SLCD_CURSOR_HEADER  = [0xFF]
SLCD_CURSOR_ACK     = [0x5A]

SLCD_RETURN_HOME    = [0x61]
SLCD_DISPLAY_OFF    = [0x63]
SLCD_DISPLAY_ON     = [0x64]
SLCD_CLEAR_DISPLAY  = [0x65]
SLCD_CURSOR_OFF     = [0x66]
SLCD_CURSOR_ON      = [0x67]
SLCD_BLINK_OFF      = [0x68]
SLCD_BLINK_ON       = [0x69]
SLCD_SCROLL_LEFT    = [0x6C]
SLCD_SCROLL_RIGHT   = [0x72]
SLCD_NO_AUTO_SCROLL = [0x6A]
SLCD_AUTO_SCROLL    = [0x6D]
SLCD_LEFT_TO_RIGHT  = [0x70]
SLCD_RIGHT_TO_LEFT  = [0x71]
SLCD_POWER_ON       = [0x83]
SLCD_POWER_OFF      = [0x82]
SLCD_INVALIDCOMMAND = [0x46]
SLCD_BACKLIGHT_ON   = [0x81]
SLCD_BACKLIGHT_OFF  = [0x80]

class SerialLCD:
  def __init__(self):
    #Iniciamos serial
    self.port = serial.Serial('/dev/ttyS0', 9600)
    sleep(2)
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_POWER_OFF)
    sleep(1)
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_POWER_ON)
    sleep(1)
    self.write(SLCD_INIT_ACK)
    # Esperamos la respuesta del lcd este listo
    while 1:
      response = self.port.read()
      # print(response)
      if serial.to_bytes(response) == serial.to_bytes(SLCD_INIT_DONE) :
        break
    print('LCD Iniciado Correctamente')
    sleep(1)

  def write(self, data):
    self.port.write(serial.to_bytes(data))
  
  # Clear the display
  def clear(self): 
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_CLEAR_DISPLAY)
  
  # Return to home(top-left corner of LCD)
  def home(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_RETURN_HOME)
    sleep(1)

  # Set Cursor to (Column,Row) Position
  def setCursor(self, column, row):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_CURSOR_HEADER)
    self.write(serial.to_bytes(str(column).encode()))
    self.write(serial.to_bytes(str(row).encode()))

  # Switch the display off without clearing RAM
  def noDisplay(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_DISPLAY_OFF)
  
  # Switch the display on
  def display(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_DISPLAY_ON)

  # Switch the underline cursor off
  def noCursor(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_CURSOR_OFF)

  # Switch the underline cursor on
  def cursor(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_CURSOR_ON)

  # Switch off the blinking cursor
  def noBlink(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_BLINK_OFF)

  # Switch on the blinking cursor
  def blink(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_BLINK_ON)

  # Scroll the display left without changing the RAM
  def scrollDisplayLeft(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_SCROLL_LEFT)

  # Scroll the display right without changing the RAM
  def scrollDisplayRight(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_SCROLL_RIGHT)

  # Set the text flow "Left to Right"
  def leftToRight(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_LEFT_TO_RIGHT)
  
  # Set the text flow "Right to Left"
  def rightToLeft(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_RIGHT_TO_LEFT)
  
  # This will 'right justify' text from the cursor
  def autoscroll(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_AUTO_SCROLL)

  # This will 'left justify' text from the cursor
  def noAutoscroll(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_NO_AUTO_SCROLL)

  def power(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_POWER_ON)
  
  def noPower(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_POWER_OFF)

  # Turn off the backlight
  def noBacklight(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_BACKLIGHT_OFF)
  
  # Turn on the back light
  def backlight(self):
    self.write(SLCD_CONTROL_HEADER)
    self.write(SLCD_BACKLIGHT_ON)
  
  # Print Commands
  def printText(self, text):
    self.write(SLCD_CHAR_HEADER)
    self.write(text.encode())
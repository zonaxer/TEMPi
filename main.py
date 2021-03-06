from SerialLCD import SerialLCD
from time import sleep

ser = SerialLCD()

def setTemperature(temp):
  ser.setCursor(0, 0)
  ser.printText(str("C: "+str(temp)))

def setHumidity(hum):
  ser.setCursor(8,0)
  ser.printText(str("H: "+str(hum)))

for x in range(60):
  print(x)
  setTemperature(x)
  setHumidity(x+5)
  sleep(1)
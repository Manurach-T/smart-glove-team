from machine import Pin
import time

LED_PIN = [2, 3 , 4 , 5] 
button_pin = 9

DELAY = 0.2 

led = [Pin(LED_PIN[0], Pin.OUT),Pin(LED_PIN[1], Pin.OUT),Pin(LED_PIN[2], Pin.OUT),Pin(LED_PIN[3], Pin.OUT)]
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

while True:
  if button.value() == 0 :
    for i in range(len(led)):
        led[i-1].value(1)  
        time.sleep(DELAY)
        led[i-1].value(0) 
        time.sleep(DELAY)
  else:
    for i in range(len(led), 0 , -1):
        led[i-1].value(1)  
        time.sleep(DELAY)
        led[i-1].value(0) 
        time.sleep(DELAY)
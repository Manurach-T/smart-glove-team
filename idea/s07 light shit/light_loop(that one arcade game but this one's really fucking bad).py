from machine import Pin
import time
LED_PIN_G = 2
LED_PIN_R = 3
LED_PIN_B = 4
LED_PIN_Y = 5
buttonpin = 9
DELAY = 0.25
led_g = Pin(LED_PIN_G, Pin.OUT)
led_r = Pin(LED_PIN_R, Pin.OUT)
led_b = Pin(LED_PIN_B, Pin.OUT)
led_y = Pin(LED_PIN_Y, Pin.OUT)
button = Pin(buttonpin, Pin.IN, Pin.PULL_UP)
while True:
    if button.value() == 0:
        led_r.value(0)
        led_y.value(1)
        time.sleep(DELAY)
        led_y.value(0)
        led_b.value(1)
        time.sleep(DELAY)        
        led_b.value(0)
        led_g.value(1)
        time.sleep(DELAY)
        led_g.value(0)
        led_r.value(1)
        time.sleep(DELAY)
    else:
        led_y.value(0)
        led_r.value(1)
        time.sleep(DELAY)
        led_r.value(0)
        led_g.value(1)
        time.sleep(DELAY)        
        led_g.value(0)
        led_b.value(1)
        time.sleep(DELAY)
        led_b.value(0)
        led_y.value(1)
        time.sleep(DELAY)
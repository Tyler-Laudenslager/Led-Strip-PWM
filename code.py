#https://learn.adafruit.com/rgb-led-strips
#Code Below is Based on Tutorial Above
#2022 Tyler Laudenslager
#Circuit Python 7.*

import board
import pwmio
import time

#A3 bin on Metro ESP32-S2
led = pwmio.PWMOut(board.A3)

while True:
    #0 to 99
    for i in range(100):
        #duty cycle is set to percentage of light going up
        #i.e 20 to 30 to 40 percent of 18000 stopping at 100
        led.duty_cycle = int( i / 200 * 18000)
        time.sleep(0.02)
    #99 to 0
    for i in range(100, -1, -1):
        #duty cycle is set to percentage of light going down
        #i.e 80 to 70 to 60 percent of 18000 stopping at 0
        led.duty_cycle = int( i / 200 * 18000)
        time.sleep(0.02)

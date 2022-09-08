import board
import pwmio
import time

led = pwmio.PWMOut(board.A3)

while True:
    for i in range(100):
        led.duty_cycle = int( i / 200 * 18000)
        time.sleep(0.02)
    for i in range(100, -1, -1):
        led.duty_cycle = int( i / 200 * 18000)
        time.sleep(0.02)

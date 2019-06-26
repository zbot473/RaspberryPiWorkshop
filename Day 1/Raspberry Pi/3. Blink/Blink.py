import pigpio
from time import sleep
gpio = pigpio.pi()
gpio.set_mode(25,pigpio.OUTPUT)

while True:
    gpio.write(25, 1)
    sleep(5)
    gpio.write(25, 0)
    sleep(5)

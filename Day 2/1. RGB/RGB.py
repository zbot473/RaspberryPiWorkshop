import pigpio
from time import sleep
gpio = pigpio.pi()
gpio.set_mode(13, pigpio.OUTPUT)
gpio.set_mode(19, pigpio.OUTPUT)
gpio.set_mode(26, pigpio.OUTPUT)


def change_RGB(r, g, b):
    gpio.write(26, r)
    gpio.write(19, g)
    gpio.write(13, b)


while True:
    change_RGB(0, 0, 0)
    sleep(1)
    change_RGB(1, 0, 0)
    sleep(1)
    change_RGB(0, 1, 0)
    sleep(1)
    change_RGB(0, 0, 1)
    sleep(1)
    change_RGB(1, 1, 0)
    sleep(1)
    change_RGB(1, 0, 1)
    sleep(1)
    change_RGB(0, 1, 1)
    sleep(1)
    change_RGB(1, 1, 1)
    sleep(1)

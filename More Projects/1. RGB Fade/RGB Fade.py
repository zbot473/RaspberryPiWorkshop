import colorsys
import pigpio
from time import sleep

gpio = pigpio.pi()
gpio.set_mode(13, pigpio.OUTPUT)
gpio.set_mode(19, pigpio.OUTPUT)
gpio.set_mode(26, pigpio.OUTPUT)


while True:
    for i in range(0,360):
        rgb = colorsys.hsv_to_rgb(i/360,1,1)
        gpio.set_PWM_dutycycle(13, (1-rgb[0])*255)
        gpio.set_PWM_dutycycle(19, (1-rgb[1])*255)
        gpio.set_PWM_dutycycle(26, (1-rgb[2])*255)
        sleep(0.01)
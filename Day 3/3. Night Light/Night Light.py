import colorsys
import pigpio
from time import sleep

gpio = pigpio.pi()
gpio.set_mode(13, pigpio.OUTPUT)
gpio.set_mode(19, pigpio.OUTPUT)
gpio.set_mode(26, pigpio.OUTPUT)
gpio.set_mode(20, pigpio.INPUT)
gpio.set_PWM_frequency(13, 40000)
gpio.set_PWM_frequency(19, 40000)
gpio.set_PWM_frequency(26, 40000)
change_color = True
last_color = 0
while True:
    if change_color:
        if last_color == 360:
            last_color = 0
        for i in range(last_color, 361):
            rgb = colorsys.hsv_to_rgb(i/360, 1, 1)
            gpio.set_PWM_dutycycle(13, (1-rgb[0])*255)
            gpio.set_PWM_dutycycle(19, (1-rgb[1])*255)
            gpio.set_PWM_dutycycle(26, (1-rgb[2])*255)
            if gpio.wait_for_edge(20, pigpio.RISING_EDGE, 0.05):
                change_color = not(change_color)
                last_color = i
                break
            if i == 360:
                last_color = 0
            sleep(0.05)
    else:
        if gpio.wait_for_edge(20, pigpio.RISING_EDGE, 0.01):
            change_color = not(change_color)

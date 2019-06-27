import pigpio
from time import sleep

gpio = pigpio.pi()
gpio.set_mode(13, pigpio.OUTPUT)
gpio.set_mode(19, pigpio.OUTPUT)
gpio.set_mode(26, pigpio.OUTPUT)
while True:
    h = input('Enter hex: ').lstrip('#')
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    gpio.set_PWM_dutycycle(13, rgb[2])
    gpio.set_PWM_dutycycle(19, rgb[1])
    gpio.set_PWM_dutycycle(26, rgb[0])

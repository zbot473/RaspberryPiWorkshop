import pigpio
from time import sleep

gpio = pigpio.pi()
gpio.set_mode(13, pigpio.OUTPUT)
gpio.set_mode(19, pigpio.OUTPUT)
gpio.set_mode(26, pigpio.OUTPUT)
gpio.set_PWM_frequency(13, 40000)
gpio.set_PWM_frequency(19, 40000)
gpio.set_PWM_frequency(26, 40000)
gpio.write(13,0)
gpio.write(19,0)
gpio.write(26,0)

while True:
    h = input('Enter hex: ').lstrip('#')
    if (h.isalnum()):
        rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        gpio.set_PWM_dutycycle(13, 255-rgb[0])
        gpio.set_PWM_dutycycle(19, 255-rgb[1])
        gpio.set_PWM_dutycycle(26, 255-rgb[2])
    else:
        print("Not hex!")

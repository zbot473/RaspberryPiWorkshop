import pigpio
from time import sleep
gpio = pigpio.pi()
gpio.set_mode(20,pigpio.INPUT)
while True:
    if gpio.read(20):
        print("You pressed the button!")
    else:
        print("The button is not pressed.")
    sleep(1)
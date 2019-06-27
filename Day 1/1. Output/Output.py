import pigpio
gpio = pigpio.pi()
gpio.set_mode(25, pigpio.OUTPUT)
gpio.write(25, 0)

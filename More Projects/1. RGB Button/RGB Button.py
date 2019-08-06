import pigpio
gpio = pigpio.pi()
gpio.set_mode(13, pigpio.OUTPUT)
gpio.set_mode(19, pigpio.OUTPUT)
gpio.set_mode(26, pigpio.OUTPUT)
gpio.set_mode(20, pigpio.INPUT)


def change_RGB(r, g, b):
    gpio.write(26, r)
    gpio.write(19, g)
    gpio.write(13, b)


def button_wait():
    while not(gpio.wait_for_edge(20)):
        pass
    

while True:
    change_RGB(0, 0, 0)
    button_wait()
    change_RGB(1, 0, 0)
    button_wait()
    change_RGB(0, 1, 0)
    button_wait()
    change_RGB(0, 0, 1)
    button_wait()
    change_RGB(1, 1, 0)
    button_wait()
    change_RGB(1, 0, 1)
    button_wait()
    change_RGB(0, 1, 1)
    button_wait()
    change_RGB(1, 1, 1)
    button_wait()
    

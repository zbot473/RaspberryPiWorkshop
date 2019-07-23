import pigpio
gpio = pigpio.pi()
gpio.set_mode(25, pigpio.OUTPUT)
while True:
    onOff = input("On or Off? ")
    if onOff == "On":
        gpio.write(25, 1)
    elif onOff =="Off":
        gpio.write(25, 0)
    else:
        print("Please type either \"On\" or \"Off\".")


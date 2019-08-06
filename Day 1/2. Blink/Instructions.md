# Blink

## Materials

* Raspberry Pi
* Breadboard
* LED


## Hardware Setup

![Circuit Setup](circuit.png)

## Software

1. Open up Thonny and create a new file called `blink.py`
2. Import the pigpio module. This allows you to use all of its functions, such as controlling a GPIO pin.
3. Create a new gpio controller using `pigpio.pi()`
4. Setup pin 25 as output using `gpio.set_mode()`
5. Make pin 25 on using `gpio.write()`
6. Run the program with the ▶️button 

[Code](output.py)

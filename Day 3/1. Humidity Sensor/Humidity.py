import Adafruit_DHT
humidity,temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)
temperature = temperature * 1.8 + 32
print(f"It is {temperature}˚F")
print(f"The humidity is {humidity}% ")

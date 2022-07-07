import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Randomising lights
rand = random.randint(0, 2)

for i in range (50):
        rand2 = random.randint(0, 1)
        pins = [18, 23, 24]
        disconnect = pins[rand] # pin set to high impedance mode (input mode in GPIO)
        pins.remove(pins[rand])
        high = pins[rand2]
        low = pins[1-rand2]
        print(low, high)
        GPIO.setup(high, GPIO.OUT)
        GPIO.setup(low, GPIO.OUT)
        GPIO.setup(disconnect, GPIO.IN)
        GPIO.output(low, GPIO.LOW)
        GPIO.output(high, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(high, GPIO.LOW)
        
        temp = rand
        while temp==rand:
                # ensuring a different light on the next run
                rand = random.randint(0, 2)

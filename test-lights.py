# tests combinations of GPIO pins to ensure that each combination of pins lights up a single and unique light 
# running this code ensures that wiring is correct
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
num = int(input())

while num!=0:
        # user can enter a number from 1 to 6, as there are 6 possible combinations on my circuit
        if num==1:
                # output: 18, input: 23, disconnected: 24
                GPIO.setup(18, GPIO.OUT)
                GPIO.setup(23, GPIO.OUT)
                GPIO.setup(24, GPIO.IN)
                GPIO.output(23, GPIO.LOW)
                GPIO.output(18, GPIO.HIGH)
                time.sleep(5)
                GPIO.output(18, GPIO.LOW)
        elif num==2:
                GPIO.setup(18, GPIO.OUT)
                GPIO.setup(24, GPIO.OUT)
                GPIO.setup(23, GPIO.IN)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(18, GPIO.HIGH)
                time.sleep(5)
                GPIO.output(18, GPIO.LOW)
        elif num==3:
                GPIO.setup(24, GPIO.OUT)
                GPIO.setup(18, GPIO.OUT)
                GPIO.setup(23, GPIO.IN)
                GPIO.output(18, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                time.sleep(5)
                GPIO.output(24, GPIO.LOW)
        elif num==4:
                GPIO.setup(24, GPIO.OUT)
                GPIO.setup(23, GPIO.OUT)
                GPIO.setup(18, GPIO.IN)
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.HIGH)
                time.sleep(5)
                GPIO.output(24, GPIO.LOW)
        elif num==5:
                GPIO.setup(23, GPIO.OUT)
                GPIO.setup(18, GPIO.OUT)
                GPIO.setup(24, GPIO.IN)
                GPIO.output(18, GPIO.LOW)
                GPIO.output(23, GPIO.HIGH)
                time.sleep(5)
                GPIO.output(23, GPIO.LOW)
        else:
                GPIO.setup(23, GPIO.OUT)
                GPIO.setup(24, GPIO.OUT)
                GPIO.setup(18, GPIO.IN)
                GPIO.output(23, GPIO.HIGH)
                time.sleep(5)
                GPIO.output(23, GPIO.LOW)
        num = int(input())


         

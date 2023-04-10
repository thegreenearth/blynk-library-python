import RPi.GPIO as GPIO
import time

# set GPIO pinout
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# GPIO 17 or Pin 11
pump1 = 27
pump2 = 22
# setup pins as input
GPIO.setup(pump1, GPIO.OUT)
GPIO.setup(pump2, GPIO.OUT)

while True:
    GPIO.output(pump1, GPIO.LOW)
    GPIO.output(pump2, GPIO.LOW)
    time.sleep(5)
    GPIO.output(pump1, GPIO.HIGH)
    GPIO.output(pump2, GPIO.HIGH)
    time.sleep(5)
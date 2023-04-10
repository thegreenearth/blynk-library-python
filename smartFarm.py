import BlynkLib
import socket
import RPi.GPIO as GPIO

# set GPIO pinout
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# GPIO 17 or Pin 11
pump1 = 27
pump2 = 22
# setup pins as input
GPIO.setup(pump1, GPIO.OUT)
GPIO.setup(pump2, GPIO.OUT)

# cloud server
BLYNK_TEMPLATE_ID = 'TMPL6pd78ZBLT'
BLYNK_DEVICE_NAME = 'SmartFarm'
BLYNK_AUTH = 'zXh5VNnFcGTsCmADGbHTTR1J0n0H8l5d'
#define BLYNK_TEMPLATE_ID "TMPL6pd78ZBLT"
#define BLYNK_TEMPLATE_NAME "SmartFarm"
#define BLYNK_AUTH_TOKEN "zXh5VNnFcGTsCmADGbHTTR1J0n0H8l5d"

blynk = BlynkLib.Blynk(BLYNK_AUTH)

# for data stream Virtual Pin V0


@blynk.on('V0')
def S1_write_handler(value):
    print("value v0 = {}".format(value[0]))
    if int(value[0]) == 1:
        print('Pump1 on')
        GPIO.output(pump1, GPIO.LOW)
    else:
        print('Pump1 off')
        GPIO.output(pump1, GPIO.HIGH)

@blynk.on('V1')
def S1_write_handler(value):
    print("value v0 = {}".format(value[0]))
    if int(value[0]) == 1:
        print('Pump2 on')
        GPIO.output(pump2, GPIO.LOW)
    else:
        print('Pump2 off')
        GPIO.output(pump2, GPIO.HIGH)

@blynk.on("connected")
def blynk_connected():
    print('Updating values from the server...')
# sync virtual pin V0
    blynk.sync_virtual(0)
    blynk.sync_virtual(1)

if __name__ == "__main__":
    while True:
        try:
            blynk.run()
        except socket.error as e:
            print(e)

            blynk.connect()

import RPi.GPIO as GPIO
from time import sleep
import sys
in1 = 20
in2 = 21
BUTTON = 16
SEC = [33,66,99]
mode = 0
before = True



def button_pressed():
    global BUTTON
    global SEC
    global mode
    if mode == 2:
        mode = 0
    else:
        mode+=1
    print(mode)
    sleep(0.1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.output(in2, 0)
pwm = GPIO.PWM(in1, 50)

try:
    while True:
        if(GPIO.input(BUTTON) and before):
            button_pressed()
            before = False
        if(not GPIO.input(BUTTON)):
            before=True
        pwm.start(SEC[mode])
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
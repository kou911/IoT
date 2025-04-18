import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pins = [2,3]
for i in pins:
 GPIO.setup(i, GPIO.OUT)

def opposite(out):
 GPIO.output(2,out)
 if out:
  GPIO.output(3,0)
 else:
  GPIO.output(3,1)

try:
 while True:
  opposite(1)
  time.sleep(0.5)
  opposite(0)
  time.sleep(0.5)
except KeyboardInterrupt:
 GPIO.cleanup()
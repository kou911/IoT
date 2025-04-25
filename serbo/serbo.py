import RPi.GPIO as GPIO
from time import sleep
servo = 20
frequency = 50
angle_0 = 2.5 / 20 * 100 #duty: 12.5%
angle_90 = 1.5 / 20 * 100 #duty: 7.5%
angle_180 = 0.5 / 20 * 100 #duty: 2.5%
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, frequency)
pwm.start(angle_0)
sleep(1)
pwm.ChangeDutyCycle(angle_90)
sleep(1)
pwm.ChangeDutyCycle(angle_180)
sleep(1)
pwm.ChangeDutyCycle(angle_0)
sleep(1)
pwm.stop()
GPIO.cleanup()

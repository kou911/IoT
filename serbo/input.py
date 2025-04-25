import RPi.GPIO as GPIO
from time import sleep
servo = 20
frequency = 50
while True:
    angle = int(input("目標角度を入力："))
    if angle>180:
        print("180以下を入力")
    elif angle<0:
        print("0以上を入力")
    else:
        break
if angle == 0:
    angle = 12.5
else:
    angle = 12.5-angle*10/180
angle_0 = 2.5 / 20 * 100 #duty: 12.5%

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, frequency)
pwm.start(angle_0)
sleep(1)
pwm.ChangeDutyCycle(angle)
sleep(1)
pwm.stop()
GPIO.cleanup()
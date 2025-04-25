import time
import RPi.GPIO as GPIO
import sys
import datetime # pip でインストール

BUTTON = 16
LED = 2
LED_st = 0

# gpio_no: イベントの原因となったGPIOピンの番号
def button_pressed(gpio_no):
    global LED_st
    global BUTTON
    global LED
    if gpio_no == BUTTON:
        if LED_st == 0:
            print(gpio_no)
            LED_st = 1
        else:
            print("LED OFF")
            LED_st = 0
    GPIO.output(LED, LED_st)
    time.sleep(0.1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)
# 立ち下がり（GPIO.FALLING）を検出する（プルアップなので通常時1／押下時0）
GPIO.add_event_detect(BUTTON, GPIO.FALLING, bouncetime=1)
GPIO.add_event_callback(BUTTON, button_pressed)

try:
    while True:
        #別の処理をここに入れる。押されていない間はここの処理を繰り返す。
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()

import time
import RPi.GPIO as GPIO
import sys
import datetime # pip でインストール

BUTTON = 16
LED = 2
LED_st = 0

# BCM(GPIO番号)で指定する設定
GPIO.setmode(GPIO.BCM)

# GPIO2を出力モード設定
GPIO.setup(LED, GPIO.OUT)

# GPIO16の入力モード設定
GPIO.setup(BUTTON, GPIO.IN)

# 内部プルダウン設定 GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
        time.sleep(0.1)
        if GPIO.input(BUTTON) == GPIO.HIGH:
            LED_st = 1
        else:
            LED_st = 0
        GPIO.output(LED, LED_st)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()

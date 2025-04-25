import RPi.GPIO as GPIO
import time
import sys
trig_pin = 14 # GPIO 15
echo_pin = 15 # GPIO 14
speed_of_sound = 34370 # 20℃での音速(cm/s)
GPIO.setmode(GPIO.BCM) # GPIOをBCMモードで使用
# GPIO.setwarnings(False) # BPIO警告無効化
GPIO.setup(trig_pin, GPIO.OUT) # Trigピン出力モード設定
GPIO.setup(echo_pin, GPIO.IN) # Echoピン入力モード設定
t1 = 0
t2 = 0
same = False
count = 0

min = 2
max = 10

while True: # 繰り返し処理
    try:
        #Trigピンを10μsだけHIGHにして超音波の発信開始
        GPIO.output(trig_pin, GPIO.HIGH)
        time.sleep(0.000010)
        GPIO.output(trig_pin, GPIO.LOW)

        while not GPIO.input(echo_pin):
            t1 = time.time() # 超音波発信時刻（EchoピンがHIGHになった時刻）格納

        while GPIO.input(echo_pin):
            t2 = time.time() # 超音波受信時刻（EchoピンがLOWになった時刻）格納

        distance = (t2 - t1) * speed_of_sound / 2
        distance_format = '{:.1f}'.format(distance) # 小数点1までまるめ
        
        if distance>min and distance<max and not same:
            count=count+1
            same = True
            print(f"{count}人")
        if distance<min or distance>max and same:
            same = False

        time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
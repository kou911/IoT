from flask import Flask, request
from flask import render_template
from RPi import GPIO
app = Flask(__name__)

@app.route("/") # 初期設定
def lchikaWeb():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)
    return render_template('onoff.html')

@app.route("/onoff", methods=["GET", "POST"])
def turn_on_off():
    if request.method == "POST":
        if request.form.get('btn') == "ON":
            result = request.form.get('btn')
            GPIO.output(16, GPIO.HIGH)
        else:
            result = request.form.get('btn')
            GPIO.output(16, GPIO.LOW)
        return render_template('onoff.html', tmp=result)
    else:
        return render_template('onoff.html', tmp="INIT")

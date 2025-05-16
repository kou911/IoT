from flask import Flask
from flask import render_template
from RPi import GPIO

app = Flask(__name__)

@app.route("/")
def lchikaWeb():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)
    return render_template('index.html')

@app.route("/on")
def turn_on():
    GPIO.output(16, GPIO.HIGH)
    return render_template('index.html', tmp="on!")

@app.route("/off")
def turn_off():
    GPIO.output(16, GPIO.LOW)
    return render_template('index.html', tmp="off!")

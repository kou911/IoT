from flask import Flask
from flask import render_template
from RPi import GPIO

app = Flask(__name__)

@app.route("/")
def lchikaWeb():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)
    return render_template('index.html')

@app.route("/on1")
def turn_on():
    GPIO.output(16, GPIO.HIGH)
    return render_template('index.html', tmp="on!")

@app.route("/off1")
def turn_off():
    GPIO.output(16, GPIO.LOW)
    return render_template('index.html', tmp="off!")

@app.route("/on2")
def turn_on1():
    GPIO.output(26, GPIO.LOW)
    return render_template('index.html', tmp="on!")

@app.route("/off2")
def turn_off2():
    GPIO.output(26, GPIO.LOW)
    return render_template('index.html', tmp="off!")
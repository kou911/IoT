from flask import Flask, request
from flask import render_template
from RPi import GPIO
import sys
import SDL_Pi_HDC1080
import RPi.GPIO as GPIO
app = Flask(__name__)

@app.route("/") # 初期設定
def lchikaWeb():
    hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()
    hdc1080.turnHeaterOff()
    hdc1080.setTemperatureResolution(SDL_Pi_HDC1080.HDC1080_CONFIG_TEMPERATURE_RESOLUTION_14BIT)
    hdc1080.setHumidityResolution(SDL_Pi_HDC1080.HDC1080_CONFIG_HUMIDITY_RESOLUTION_14BIT)

@app.route("/temp", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        if request.form.get('btn') == "ON":
            result =   "-----------------<br>Temperature =" \
                        + hdc1080.readTemperature()\
                        + "C <br>Humidity ="\
                        + hdc1080.readHumidity()\
                        + "%<br>-----------------"
        return render_template('index.html', tmp=result)
    else:
        return render_template('index.html', tmp="INIT")

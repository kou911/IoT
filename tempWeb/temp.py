from flask import Flask, request
from flask import render_template
from RPi import GPIO
import sys
import SDL_Pi_HDC1080
import RPi.GPIO as GPIO
import datetime
app = Flask(__name__)


@app.route("/") # 初期設定
def temp():

    return render_template('index.html')

@app.route("/temp", methods=["GET", "POST"])
def send():
    hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()
    hdc1080.turnHeaterOff()
    hdc1080.setTemperatureResolution(SDL_Pi_HDC1080.HDC1080_CONFIG_TEMPERATURE_RESOLUTION_14BIT)
    hdc1080.setHumidityResolution(SDL_Pi_HDC1080.HDC1080_CONFIG_HUMIDITY_RESOLUTION_14BIT)
    if request.method == "GET":
        result =    str(datetime.datetime.now()) \
                    + "</br>-----------------<br>Temperature =" \
                    + str(hdc1080.readTemperature())\
                    + "C <br>Humidity ="\
                    + str(hdc1080.readHumidity())\
                    + "%<br>-----------------"
        return render_template('index.html', tmp=result)
    else:
        return render_template('index.html', tmp="INIT")

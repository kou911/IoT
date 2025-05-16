import sys
import time
import datetime
import SDL_Pi_HDC1080
import RPi.GPIO as GPIO

hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()
hdc1080.turnHeaterOff()
hdc1080.setTemperatureResolution(SDL_Pi_HDC1080.HDC1080_CONFIG_TEMPERATURE_RESOLUTION_14BIT)
hdc1080.setHumidityResolution(SDL_Pi_HDC1080.HDC1080_CONFIG_HUMIDITY_RESOLUTION_14BIT)
while True:
    try:
        print ("-----------------")
        print ("Temperature = %3.1f C" % hdc1080.readTemperature())
        print ("Humidity = %3.1f %%" % hdc1080.readHumidity())
        print ("-----------------")
        time.sleep(3.0)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()

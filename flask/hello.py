from flask import Flask
app = Flask(__name__)

@app.route("/japan")
def japan():
    return "<p>Hello, 日本!</p>"

@app.route("/neyagawa")
def neyagawa():
    return "<p>Hello, 寝屋川!</p>"

@app.route("/kousen")
def kousen():
    return "<p>Hello, 高専!</p>"

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Erica, Welcome to this staging of deployment!"

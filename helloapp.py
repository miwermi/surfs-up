#FIRST FLASK APP (FLASK TEST)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"


from flask import Flask

app = Flask(__name__)

@app.route("/api/v1")
def home():
    return "Hello, Flask!"
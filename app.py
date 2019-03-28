from flask import Flask
app = Flask(__name__)

@app.route("/welcomer/hello")
def hello():
    return "Hello World!"

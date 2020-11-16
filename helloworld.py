# import Flask
from flask import Flask

#intialise app varaible
app = Flask(__name__)


#decorate a python fuction with app.route. It associates a web url with a defined function.
@app.route("/")
def home():
    return "This is my home attached to root url /"

@app.route("/hello")
def hello():
    return "Hello world from Python Flask Web Framework!"


if __name__ == ("__main__"):
    app.run()
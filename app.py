from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the flask page.This is a Worderfull WEbsite"


if __name__ =="__main__":
    app.run(debug = True)

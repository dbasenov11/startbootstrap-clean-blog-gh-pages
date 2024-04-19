from flask import Flask
from flask import render_template
from flask import url_for
import requests


response = requests.get("https://api.npoint.io/dadef4e7ab4aa9484d64").json()
print(response)

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html", posts=response)


@app.route("/about.html")
def show_about():
    return render_template("about.html")


@app.route("/contact.html")
def show_contact():
    return render_template("contact.html")


if app.name == "main":
    app.run(debug=True)
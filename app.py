"""
[Aplicación básica del microframework Flask de Python]
Author: margalena
Date: [05/10/2022]
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/servicios")
def servicios():
	return render_template("base.html")

@app.route("/conctacto")
def conctacto():
	return render_template("base.html")

@app.route("/admin")
def admin():
	return render_template("base.html")

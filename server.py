import os

from flask import Flask, render_template, url_for, request, redirect, session



SUBMITS_FILE = "contacts.csv"

app = Flask(__name__)
app.secret_key = ".."

@app.route("/")
def main_page(): 
	return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name): 
	return render_template(page_name)


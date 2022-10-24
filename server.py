import os

from helpers import append_answer
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

@app.route("/submit_form", methods = ["POST", "GET"])
def submit_form(): 
	if request.method == "POST": 
		data = request.form.to_dict()
		if append_answer(SUBMITS_FILE, data): 
			session["name"] = data["name"]
			return redirect("/portfolio/contact_thankyou.html")
	return "what happened?"

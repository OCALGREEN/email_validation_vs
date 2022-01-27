
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.login import LogIn

#home
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["POST"])
def login():
    if not LogIn.validator(request.form): # will check to see if its a valid typo
        return redirect("/")
    else: 
        LogIn.create(request.form) # will add a new email to the db
        return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html", all_emails = LogIn.get_all())

@app.route("/destroy/<int:email_id>")
def destroy(email_id):
    LogIn.destroy({"id": email_id})
    return redirect("/success")
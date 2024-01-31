from flask import redirect, render_template, request, session

from ..db.models import User
from ..extensions import db


def login():
    if request.method == "POST":
        user_name = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(user_name=user_name, password=password).first()
        if user:
            session["logged_in"] = True
            session["user_id"] = user.user_id
            return redirect("/")
        else:
            return "Invalid username or password", 400
    else:
        return render_template("auth/login.html")


def register():
    if request.method == "POST":
        user_name = request.form["username"]
        password = request.form["password"]
        new_user = User(user_name=user_name, password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error: {e}")
            return "There was an issue registering your account"
    else:
        return render_template("auth/register.html")


def logout():
    session.pop("logged_in", None)
    session.pop("user_id", None)
    return redirect("/login")

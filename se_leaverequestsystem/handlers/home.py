from flask import redirect, render_template, session
from werkzeug import Response

from ..db.models import LeaveRequest


def index():
    if "logged_in" not in session or not session["logged_in"]:
        return redirect("/login")

    leaves = LeaveRequest.query.order_by(LeaveRequest.date_created).all()
    return render_template("index.html", leaves=leaves)

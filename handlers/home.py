from datetime import datetime
from flask import session, redirect, request, render_template
from SE_LeaveRequestSystem.extensions import db
from SE_LeaveRequestSystem.db.models import LeaveRequest


def index():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect('/login')

    leaves = LeaveRequest.query.order_by(LeaveRequest.date_created).all()
    return render_template('index.html', leaves=leaves)

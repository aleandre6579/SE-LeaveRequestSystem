from datetime import datetime

from flask import redirect, render_template, request, session

from SE_LeaveRequestSystem.se_leaverequestsystem.db.models import LeaveRequest
from SE_LeaveRequestSystem.src.SE_LeaveRequestSystem.extensions import db


def index():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect('/login')

    leaves = LeaveRequest.query.order_by(LeaveRequest.date_created).all()
    return render_template('index.html', leaves=leaves)

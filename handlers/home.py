from datetime import datetime
from flask import session, redirect, request, render_template
from SE_LeaveRequestSystem.extensions import db
from SE_LeaveRequestSystem.db.models import LeaveRequest


def index():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect('/login')

    user_id = session.get('user_id')

    if request.method == 'POST':
        leave_reason = request.form['reason']
        leave_date_start_str = request.form['date_start']
        leave_date_end_str = request.form['date_end']
        try:
            leave_date_start = datetime.strptime(leave_date_start_str, '%Y-%m-%d')
            leave_date_end = datetime.strptime(leave_date_end_str, '%Y-%m-%d')
        except ValueError:
            return 'Please enter valid dates'

        new_leave = LeaveRequest(
            reason=leave_reason,
            date_start=leave_date_start,
            date_end=leave_date_end,
            user_id=user_id
        )

        try:
            db.session.add(new_leave)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"Error: {e}")
            return 'There was an issue adding your task'
    elif request.method == 'GET':
        leaves = LeaveRequest.query.order_by(LeaveRequest.date_created).all()
        return render_template('index.html', leaves=leaves)
    else:
        print("Request method not recognized")
        return render_template('not_found.html')

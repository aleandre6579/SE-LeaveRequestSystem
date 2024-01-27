from datetime import datetime

from flask import redirect, request, session

from SE_LeaveRequestSystem.se_leaverequestsystem.db.models import LeaveRequest
from SE_LeaveRequestSystem.src.SE_LeaveRequestSystem.db import leave
from SE_LeaveRequestSystem.src.SE_LeaveRequestSystem.extensions import db


def deleteLeave(leave_id: int):
    leave_to_delete = LeaveRequest.query.get_or_404(leave_id)

    # Check if the logged-in user is the owner of the request
    if leave_to_delete.user_id == session.get('user_id'):

        if leave.startDatePassed(leave_to_delete.date_start):
            return 'Cannot delete because the start date has already passed'

        try:
            db.session.delete(leave_to_delete)
            db.session.commit()
            return {'delete_success': True}
        except:
            return 'There was an issue deleting your task'
    else:
        return 'You do not have permission to delete this request'


def postLeave():
    user_id = session.get('user_id')
    leave_reason = request.form['reason']
    leave_date_start_str = request.form['date_start']
    leave_date_end_str = request.form['date_end']

    try:
        leave_date_start = datetime.strptime(leave_date_start_str, '%Y-%m-%d')
        leave_date_end = datetime.strptime(leave_date_end_str, '%Y-%m-%d')
    except ValueError:
        return 'Please enter valid dates'

    if not leave.validatesSameDayConflict(leave_date_start):
        return "There is a day conflict: can't have 2 leaves starting on the same day"

    quota = 10
    if not leave.validatesLeaveQuota(leave_date_start, quota):
        return f"You cannot have more than {quota} leaves in a year!"

    max_days = 60
    if not leave.validatesMaxLeaveDate(leave_date_start, max_days):
        return f"You cannot request leave over {max_days} days from now!"

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

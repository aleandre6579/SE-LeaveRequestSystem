from datetime import datetime
from SE_LeaveRequestSystem.se_leaverequestsystem.extensions import db
from SE_LeaveRequestSystem.se_leaverequestsystem.db.models import LeaveRequest
from flask import session


def validatesSameDayConflict(date: datetime.day) -> bool:
    same_day_leaves = LeaveRequest.query.filter_by(date_start=date, id=session.get('user_id')).all()
    return len(same_day_leaves) == 0


def validatesLeaveQuota(start_date: datetime.day, quota: int) -> bool:
    user_leaves = LeaveRequest.query.filter_by(user_id=session.get('user_id')).all()
    same_year_leaves = list(filter(lambda leave: (leave.date_start.year == start_date.year), user_leaves))
    return len(same_year_leaves) < quota


def validatesMaxLeaveDate(start_date: datetime.day, max_days: int) -> bool:
    today = datetime.now()
    return (start_date - today).days < max_days


def startDatePassed(start_date: datetime.day):
    today = datetime.now()
    return (today - start_date).days >= 0

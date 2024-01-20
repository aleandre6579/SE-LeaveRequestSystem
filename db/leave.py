from datetime import datetime
from SE_LeaveRequestSystem.extensions import db
from SE_LeaveRequestSystem.db.models import LeaveRequest
from flask import session


def hasSameDayConflict(date: datetime.day) -> bool:
    same_day_leaves = LeaveRequest.query.filter_by(date_start=date, id=session.get('user_id')).all()
    return len(same_day_leaves) > 0


def validatesLeaveQuota(date: datetime.day, quota: int) -> bool:
    user_leaves = LeaveRequest.query.filter_by(user_id=session.get('user_id')).all()
    same_year_leaves = list(filter(lambda leave: (leave.date_start.year == date.year), user_leaves))
    return len(same_year_leaves) < quota

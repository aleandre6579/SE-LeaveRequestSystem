from datetime import datetime
from SE_LeaveRequestSystem.extensions import db
from SE_LeaveRequestSystem.db.models import LeaveRequest
from flask import session


def hasSameDayConflict(date: datetime.day) -> bool:
    same_day_leaves = LeaveRequest.query.filter_by(date_start=date, id=session.get('user_id')).all()
    return len(same_day_leaves) > 0


def validatesDayQuota(date: datetime.day) -> bool:
    same_day_leaves = LeaveRequest.query.filter_by(date_start=date).all()
    return len(same_day_leaves) > 0

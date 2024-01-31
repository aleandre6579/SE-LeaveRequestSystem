from datetime import datetime

from flask import session

from .models import LeaveRequest


def validates_same_day_conflict(date: datetime.day) -> bool:
    same_day_leaves = LeaveRequest.query.filter_by(
        date_start=date, id=session.get("user_id")
    ).all()
    return len(same_day_leaves) == 0


def validates_leave_quota(start_date: datetime.day, quota: int) -> bool:
    user_leaves = LeaveRequest.query.filter_by(user_id=session.get("user_id")).all()

    same_year_leaves = list(
        filter(lambda leave: (leave.date_start.year == start_date.year), user_leaves)
    )
    return len(same_year_leaves) < quota


def validates_max_leave_date(start_date: datetime.day, max_days: int) -> bool:
    today = datetime.now()
    return (start_date - today).days < max_days


def start_date_passed(start_date: datetime.day) -> bool:
    today = datetime.now()
    return (today - start_date).days >= 0

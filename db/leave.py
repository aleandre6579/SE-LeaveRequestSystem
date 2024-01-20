from datetime import datetime
from SE_LeaveRequestSystem.extensions import db
from SE_LeaveRequestSystem.db.models import LeaveRequest


def hasSameDayConflict(date: datetime.day) -> bool:
    same_day_leaves = LeaveRequest.query.filter_by(date_start=date).all()
    return len(same_day_leaves) > 0

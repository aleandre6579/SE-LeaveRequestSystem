from flask import (
    session, redirect
)
from SE_LeaveRequestSystem.db.models import (LeaveRequest)
from SE_LeaveRequestSystem.extensions import db


def deleteLeave(id: int):
    leave_to_delete = LeaveRequest.query.get_or_404(id)

    # Check if the logged-in user is the owner of the request
    if leave_to_delete.user_id == session.get('user_id'):
        try:
            db.session.delete(leave_to_delete)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue deleting your task'
    else:
        return 'You do not have permission to delete this request'

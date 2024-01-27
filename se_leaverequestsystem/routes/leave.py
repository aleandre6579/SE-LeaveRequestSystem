from flask import Blueprint, redirect, request

from SE_LeaveRequestSystem.se_leaverequestsystem.handlers import leave

bp = Blueprint('leave', __name__, url_prefix='/leave')


@bp.route('/<int:leave_id>', methods=['DELETE'])
def deleteLeave(leave_id: int):
    return leave.deleteLeave(leave_id)


@bp.route('/', methods=['POST'])
def postLeave():
    return leave.postLeave()

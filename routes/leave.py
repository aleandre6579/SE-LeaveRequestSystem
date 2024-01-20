from flask import (
    Blueprint, request, redirect
)

from SE_LeaveRequestSystem.handlers import leave

bp = Blueprint('leave', __name__, url_prefix='/leave')


@bp.route('/<int:id>', methods=['DELETE'])
def deleteLeave(id: int):
    return leave.deleteLeave(id)


@bp.route('/', methods=['POST'])
def postLeave():
    return leave.postLeave()

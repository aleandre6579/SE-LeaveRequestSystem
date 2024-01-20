from flask import (
    Blueprint
)

from SE_LeaveRequestSystem.handlers import leave

bp = Blueprint('leave', __name__, url_prefix='/leave')


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    return leave.deleteLeave(id)

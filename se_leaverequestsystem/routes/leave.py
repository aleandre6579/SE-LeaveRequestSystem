from flask import Blueprint, Response

from SE_LeaveRequestSystem.se_leaverequestsystem.handlers import leave

bp = Blueprint("leave", __name__, url_prefix="/leave")


@bp.route("/<int:leave_id>", methods=["DELETE"])
def deleteLeave(leave_id: int) -> str | dict[str, bool]:
    return leave.deleteLeave(leave_id)


@bp.route("/", methods=["POST"])
def postLeave() -> str | Response:
    return leave.postLeave()

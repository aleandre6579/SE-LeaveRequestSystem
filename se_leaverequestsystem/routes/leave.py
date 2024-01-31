from flask import Blueprint, Response

from ..handlers import leave

bp = Blueprint("leave", __name__, url_prefix="/leave")


@bp.errorhandler(404)
def not_found():
    return Response(status=404)


@bp.route("", methods=["POST"])
def postLeave():
    return leave.postLeave()


@bp.route("/<int:leave_id>", methods=["DELETE"])
def deleteLeave(leave_id: int) -> str | dict[str, bool]:
    return leave.deleteLeave(leave_id)

from flask import Blueprint

from SE_LeaveRequestSystem.SE_LeaveRequestSystem.handlers import home

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/", methods=["POST", "GET", "DELETE"])
def index():
    return home.index()

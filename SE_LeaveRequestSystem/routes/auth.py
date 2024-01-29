from flask import Blueprint

from SE_LeaveRequestSystem.SE_LeaveRequestSystem.handlers import auth

bp = Blueprint("auth", __name__, url_prefix="/")


@bp.route("/login", methods=["POST", "GET"])
def login():
    return auth.login()


@bp.route("/register", methods=["POST", "GET"])
def register():
    return auth.register()


@bp.route("/logout")
def logout():
    return auth.logout()

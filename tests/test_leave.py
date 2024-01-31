from datetime import datetime
from se_leaverequestsystem.db.models import User, LeaveRequest
from conftest import register, login


def test_register(app, client):
    register(client, "alex", "pass")

    with app.app_context():
        assert User.query.count() == 1
        new_user = User.query.filter_by(user_name="alex").first()
        assert new_user is not None
        assert new_user.password == "pass"
        assert new_user.user_name == "alex"


def test_login(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")

    with client.session_transaction() as session:
        assert session["logged_in"] == True
        assert session["user_id"] == 1


def test_post_leave(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")

    response = client.post(
        "/leave",
        data={"reason": "sick", "date_start": "2023-02-01", "date_end": "2023-02-02"}
    )

    with app.app_context():
        print(LeaveRequest.query.all())
        assert LeaveRequest.query.count() == 1
        new_leave = LeaveRequest.query.filter_by(reason="sick").first()
        assert new_leave is not None
        assert new_leave.reason == "sick"
        assert new_leave.date_start.strftime("%Y-%m-%d") == "2023-02-01"
        assert new_leave.date_end.strftime("%Y-%m-%d") == "2023-02-02"


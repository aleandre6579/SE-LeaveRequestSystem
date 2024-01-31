from conftest import login, post_leave, register

from se_leaverequestsystem.db.models import LeaveRequest


def test_post_leave(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")

    post_leave(client, "sick", "2023-02-01", "2023-02-02")

    with app.app_context():
        assert LeaveRequest.query.count() == 1
        new_leave = LeaveRequest.query.filter_by(reason="sick").first()
        assert new_leave is not None
        assert new_leave.reason == "sick"
        assert new_leave.date_start.strftime("%Y-%m-%d") == "2023-02-01"
        assert new_leave.date_end.strftime("%Y-%m-%d") == "2023-02-02"


def test_post_leave_invalid_date(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")

    response = post_leave(client, "sick", "2023-14-10", "2023-02-01")
    assert response.status_code == 400


def test_post_leave_same_day_conflit(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")

    response = post_leave(client, "sick", "2023-02-01", "2023-02-04")
    response = post_leave(client, "sick", "2023-02-01", "2023-02-06")
    assert response.status_code == 400


def test_post_leave_quota(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")

    for i in range(1, 11):
        post_leave(client, "sick", f"2023-02-{i}", "2023-02-11")

    response = post_leave(client, "sick", "2023-02-11", "2023-02-11")
    assert response.status_code == 400


def test_post_leave_max_leave_date(client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")

    response = post_leave(client, "sick", "2025-02-01", "2025-02-11")
    assert response.status_code == 400

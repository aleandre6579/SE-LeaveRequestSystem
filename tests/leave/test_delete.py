from conftest import delete_leave, login, post_leave, register

from se_leaverequestsystem.db.models import LeaveRequest


def test_delete_leave(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")

    post_leave(client, "sick", "2024-02-01", "2024-02-02")
    delete_leave(client, "1")

    with app.app_context():
        new_leave = LeaveRequest.query.filter_by(reason="sick").first()
        assert new_leave is None


def test_delete_leave_not_found(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")

    post_leave(client, "sick", "2024-02-01", "2024-02-02")
    response = delete_leave(client, "0")

    assert response.status_code == 404


def test_delete_leave_forbidden(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")
    post_leave(client, "sick", "2024-02-01", "2024-02-02")

    register(client, "bob", "pass")
    login(client, "bob", "pass")
    delete_leave(client, "1")

    response = delete_leave(client, "1")

    assert response.status_code == 403


def test_delete_leave_date_passed(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")
    post_leave(client, "sick", "2023-02-01", "2024-02-02")
    delete_leave(client, "1")

    response = delete_leave(client, "1")

    assert response.status_code == 400

from conftest import login, register

from se_leaverequestsystem.db.models import LeaveRequest, User


def test_register_post(app, client):
    register(client, "alex", "pass")

    with app.app_context():
        assert User.query.count() == 1
        new_user = User.query.filter_by(user_name="alex").first()
        assert new_user is not None
        assert new_user.password == "pass"
        assert new_user.user_name == "alex"


def test_register_get(app, client):
    response = client.get("/register")
    assert response.status_code == 200


def test_login_post(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")

    with client.session_transaction() as session:
        assert session["logged_in"] == True
        assert session["user_id"] == 1


def test_login_get(app, client):
    response = client.get("/login")
    assert response.status_code == 200


def test_logout(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")
    client.get("/logout")

    with client.session_transaction() as session:
        assert "logged_in" not in session
        assert "user_id" not in session


def test_login_invalid_input(app, client):
    register(client, "alex", "pass")
    response = login(client, "alex", "wrongpass")

    assert response.status_code == 400

    with client.session_transaction() as session:
        assert "logged_in" not in session
        assert "user_id" not in session
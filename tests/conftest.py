import pytest

from se_leaverequestsystem.app import create_app, db
from se_leaverequestsystem.db.models import LeaveRequest, User


@pytest.fixture()
def app():
    app = create_app("sqlite://")

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


def register(client, username, password):
    response = client.post(
        '/register',
        data={"username": username, "password": password}
    )
    return response


def login(client, username, password):
    response = client.post(
        '/login',
        data={"username": username, "password": password}
    )
    return response


def post_leave(client, reason, date_start, date_end):
    response = client.post(
        "/leave",
        data={"reason": reason, "date_start": date_start, "date_end": date_end}
    )
    return response


def delete_leave(client, leave_id):
    response = client.delete(
        "/leave/"+leave_id
    )
    return response

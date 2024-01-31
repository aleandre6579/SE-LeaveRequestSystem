import pytest
from se_leaverequestsystem.db.models import User, LeaveRequest
from se_leaverequestsystem import create_app, db


@pytest.fixture()
def app():
    app = create_app("sqlite://")

    with app.app_context():
        db.create_all()
    print("CREATE DATABASE")
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


def login(client, username, password):
    response = client.post(
        '/login',
        data={"username": username, "password": password}
    )

from conftest import login, register


def test_home(app, client):
    response = client.get("/")
    assert response.status_code == 302


def test_home_logged_in(app, client):
    register(client, "alex", "pass")
    login(client, "alex", "pass")
    response = client.get("/")
    assert response.status_code == 200

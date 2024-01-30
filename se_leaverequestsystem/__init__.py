from flask import Flask

from .routes import auth, home, leave
from .extensions import db

def create_app(database_uri="sqlite:///leave_request.db") -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SECRET_KEY"] = "myverysecretkey"

    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(leave.bp)
    app.register_blueprint(home.bp)

    with app.app_context():
        db.create_all()

    return app

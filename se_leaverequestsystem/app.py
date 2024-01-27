from flask import Flask

from SE_LeaveRequestSystem.se_leaverequestsystem.extensions import db
from SE_LeaveRequestSystem.se_leaverequestsystem.routes import (auth, home,
                                                                leave)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leave_request.db'
    app.config['SECRET_KEY'] = 'myverysecretkey'

    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(leave.bp)
    app.register_blueprint(home.bp)

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    db.app = app
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, session
from SE_LeaveRequestSystem.src.SE_LeaveRequestSystem.routes import (auth, leave, home)
from SE_LeaveRequestSystem.src.SE_LeaveRequestSystem.extensions import db


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

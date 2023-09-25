import secrets
from flask import Flask
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    token = secrets.token_urlsafe(16)
    app.secret_key = token
    Bootstrap(app)
    CSRFProtect(app)
    return app


app = create_app()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
app.app_context().push()


class Scene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(32), unique=True, nullable=False)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))


with app.app_context():
    db.create_all()

from flask_sqlalchemy import SQLAlchemy
from config import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)


class Scene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(32), unique=True, nullable=False)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)


with app.app_context():
    db.create_all()

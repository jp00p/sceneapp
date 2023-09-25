from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from config import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db: SQLAlchemy = SQLAlchemy(app)


class Scene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=True)
    code = db.Column(db.String(32), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scene_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"{self.name}"


with app.app_context():
    db.create_all()

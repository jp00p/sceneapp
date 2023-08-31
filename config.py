import secrets
from flask import Flask
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
token = secrets.token_urlsafe(16)
app.secret_key = token
# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

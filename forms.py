from config import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerRangeField, FieldList, FormField
from wtforms.validators import DataRequired, Length


class JoinSceneForm(FlaskForm):
    scene_id = StringField("Scene code", validators=[DataRequired()])
    submit = SubmitField("Join")


class NewSceneForm(FlaskForm):
    submit = SubmitField("New scene")


class PersonForm(FlaskForm):
    bondage = ["Blindfolds", "Collar/Lead", "Leather cuffs", "Metal cuffs"]
    name = StringField("Name", validators=[DataRequired()])

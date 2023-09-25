from config import app
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    IntegerRangeField,
    FieldList,
    FormField,
    RadioField,
    Form,
    Field,
    Label,
)
from wtforms.validators import DataRequired, Length
from markupsafe import Markup


class CustomHTMLWidget(object):
    def __init__(self, html_code):
        self.html_code = Markup(html_code)

    def __call__(self, field, **kwargs):
        return self.html_code


class CustomHTMLField(Field):
    def __init__(self, html_code, label=None, **kwargs):
        super(CustomHTMLField, self).__init__(label=None, **kwargs)
        self.html_code = html_code

    def _value(self):
        return ""

    def process(self, formdata, data=None, **kwargs):
        pass


class JoinSceneForm(FlaskForm):
    scene_id = StringField("Scene code", validators=[DataRequired()])
    submit = SubmitField("Join")


class NewSceneForm(FlaskForm):
    name = StringField("Scene name")
    submit = SubmitField("New scene")


def create_kink_slider(label):
    class KinkSliderForm(FlaskForm):
        default_kw = {
            "class": "range-slider",
            "min": 0,
            "max": 4,
            "step": 1,
            "value": 0,
        }
        IntegerRangeField(label, render_kw=default_kw)
        StringField("Notes")

    return KinkSliderForm()


class PersonForm(FlaskForm):
    html_counter = 0
    name = StringField("Name")
    position = RadioField(
        "Today I want to be a",
        choices=["Top", "Bottom", "Switch", "Anything"],
        default="Anything",
    )

    @classmethod
    def add_submit(cls):
        setattr(cls, "Submit", SubmitField("Save details"))

    @classmethod
    def add_html(cls, html):
        setattr(
            cls,
            f"html_{cls.html_counter}",
            Field(label=None, widget=CustomHTMLWidget(f"{html}")),
        )
        cls.html_counter += 1

    @classmethod
    def add_kink(cls, name, label):
        class KinkSliderForm(FlaskForm):
            kink_default_kw = {
                "class": "range-slider",
                "min": 0,
                "max": 4,
                "step": 1,
                "value": 0,
            }
            notes_default_kw = {
                "class": "kink-notes",
                "placeholder": f"add your notes for {label.lower()}",
            }
            level_of_interest = IntegerRangeField(label, render_kw=kink_default_kw)
            kinknotes = StringField(
                label=f"Notes for {label}", render_kw=notes_default_kw
            )

        setattr(cls, name, FormField(KinkSliderForm))
        return cls

    my_partners = StringField("Add any relevant info about your partners")
    my_triggers = StringField("Add any relevant info about your triggers")
    medical_conditions = StringField("Add any relevant medical conditions or concerns")
    good_phrases = StringField("Words and phrases you like to hear")
    bad_phrases = StringField("Words and phrases you don't like hearing")

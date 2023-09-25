from config import app, db, Person
from flask import render_template
from forms import *


def slugify(string: str):
    return string.lower().replace(" ", "_")


@app.route("/", methods=["GET", "POST"])
def index():
    join_form = JoinSceneForm()
    new_form = NewSceneForm()

    kinks = {
        "Bondage": [
            "Blindfolds",
            "Wrist restraints",
            "Foot restraints",
            "Gags",
            "Rope",
        ],
        "Sensation play": [
            "Biting",
            "Edge play",
            "Electricity",
            "Hair pulling",
            "Licking",
            "Nipples",
            "Head petting",
            "Soft touches",
            "Scratching",
            "Sensory deprivation",
            "Tickles",
        ],
        "Impact play": [
            "Spanking",
            "Punching",
            "Paddles",
            "Canes",
            "Floggers",
            "Whips",
            "Stingy",
            "Thuddy",
        ],
        "Intimacy and sex": [
            "Cuddling",
            "Dirty talk",
            "Groping",
            "Kissing",
            "Open mouth kissing",
            "Exhibitionism",
            "Hands on genitals",
            "Orgasms",
            "Giving oral",
            "Receiving oral",
        ],
        "Feelings": [
            "Beautiful",
            "Controlled",
            "Degraded",
            "Dominant",
            "Erotic",
            "Helpless",
            "Overwhelmed",
            "Playful",
            "Sadistic",
            "Submissive",
            "Objectified",
            "Loved",
        ],
        "Aftercare": [
            "Beverages",
            "Snacks",
            "Let me be",
            "Cuddling",
            "Comfort item",
            "Conversation",
            "Socialize",
            "Check in later",
            "Retrospective",
            "Fresh air",
            "Kisses",
            "Affirmation",
        ],
    }
    kink_list = ["Spanking", "Cum play", "Oral sex", "Anal sex", "Banana splits"]

    for heading, kink in kinks.items():
        PersonForm.add_html(f"<h3 style='padding-top:2em'>{heading}</h3><hr>")
        for kink_name in kink:
            PersonForm.add_kink(slugify(kink_name), kink_name)

    PersonForm.add_submit()
    person_form = PersonForm()

    scene_id = 0
    message = ""

    if join_form.validate_on_submit():
        scene_id = join_form.scene_id.data
        message = f"You have joined scene #{scene_id}"
    if new_form.validate_on_submit():
        message = f"Creating new scene"
    if person_form.validate_on_submit():
        message = f"Person created"

    return render_template(
        "index.html",
        join_form=join_form,
        new_form=new_form,
        person_form=person_form,
        message=message,
    )


@app.route("/<string:name>/")
def say_hello(name):
    return f"Hello {name}!"

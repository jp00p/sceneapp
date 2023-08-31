from config import app
from flask import render_template
from forms import *


@app.route("/", methods=["GET", "POST"])
def index():
    # conn = get_db_connection()
    # posts = conn.execute("SELECT * FROM posts").fetchall()
    # conn.close()
    join_form = JoinSceneForm()
    new_form = NewSceneForm()
    person_form = PersonForm()
    scene_id = 0
    message = ""
    if join_form.validate_on_submit():
        scene_id = join_form.scene_id.data
        message = f"You have joined scene #{scene_id}"
    if new_form.validate_on_submit():
        message = f"Creating new scene"

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

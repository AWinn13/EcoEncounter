import os
from flask_app import app
from flask import render_template, request, flash, redirect, session
from werkzeug.utils import secure_filename
from flask_app.models.loginandreg import User
from flask_app.models.pictures import Picture


UPLOAD_FOLDER = "flask_app\\static\\img"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {"txt", "jpg", "jpeg", "gif", "png", "pdf"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/welcome")
def welcome():
    if "user_id" not in session:
        return render_template("welcome.html")
    return render_template("welcome.html", user=User.get_id({"id": session["user_id"]}))


@app.route("/water")
def water():
    if "user_id" not in session:
        return render_template("water.html")
    return render_template("water.html", user=User.get_id({"id": session["user_id"]}))


@app.route("/land")
def land():
    if "user_id" not in session:
        return render_template("land.html")
    return render_template("land.html", user=User.get_id({"id": session["user_id"]}))


@app.route("/animal/game")
def land_game():
    return render_template("animal_quiz.html")


@app.route("/water/game")
def water_game():
    return render_template("water_game.html")


# -------------render passport------------------


@app.route("/passport/upload")
def passport_render():
    if "user_id" not in session:
        flash("You Must Register to access the Eco-Passport")
        return redirect("/")
    return render_template(
        "passport_upload.html", user=User.get_id({"id": session["user_id"]})
    )

# -------------------------Upload passport pic----------------
@app.route("/passport/upload/new", methods=["post"])
def upload_file():
    if "file" not in request.files:
        flash("No file part")
        return redirect("/")

    file = request.files["file"]

    if file.filename == "":
        flash("No selected file")
        return redirect("/")

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        # send filename and rest of the from to the DB
    Picture.create(
        {**request.form, "filename": filename, "user_id": session["user_id"]}
    )
    user_id = session["user_id"]
    return redirect(f"/passport/{user_id}")

# ------------------- View Passport --------------------------------
@app.route("/passport/<int:id>")
def passport_main(id):
    if "user_id" not in session:
        return redirect("/")
    id = session["user_id"]
    return render_template(
        "passport.html",
        id=id,
        user=User.get_id({"id": session["user_id"]}),
        pictures=Picture.get_all({"user_id": session["user_id"]}),
    )





# ------------------- RenderEdit picture --------------------

@app.route("/passport/<int:id>/edit")
def render_pic(id):
    if "user_id" not in session:
        return redirect("/")
    return render_template("edit_upload.html", user=User.get_id({"id": session["user_id"]}),  this_picture = Picture.get_one_picture({"id": id}))


# ------------- Edit Passport --------------------------------    
@app.route("/passport/<int:id>/edit/now", methods=["POST"])
def edit_pic(id):
    Picture.update({**request.form,'id':id})
    return redirect(f"/passport/{id}")

# -------------------Delete-----------------------------------

@app.route("/passport/<int:id>/delete", methods=["POST"])
def delete_pic(id):
    Picture.delete({**request.form,'id':id})
    return redirect(f"/passport/{id}")





@app.route("/flowchart")
def flowchart():
    return render_template("flowchart.html")

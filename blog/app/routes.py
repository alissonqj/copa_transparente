from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Vinicius"}
    posts = [
        {"author": {"username": "Vinicius"}, "body": "Ótimo dia em Florianópolis"},
        {"author": {"username": "Jaiminho"}, "body": "Dia chuvoso em Tamgamandápio"},
    ]
    return render_template("index.html", title="Página Inicial", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login solicitado pelo usuário {}, me lembre={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))

    return render_template("login.html", title="Sign In", form=form)

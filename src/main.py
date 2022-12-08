from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
@login_required
def index():
    print(f'current_user: {current_user.name}')
    return render_template("home.html", user=str(current_user.name))


@main.route("/check_credential")
def check_credential():
    return redirect(url_for('home'))


@main.route("/messi/discussion")
def detail():
    return render_template("detail.html", title='topic')

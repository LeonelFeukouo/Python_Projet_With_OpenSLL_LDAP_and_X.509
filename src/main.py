from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required, current_user
from . import db
from .models import User, Message
from . import socket_server

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
@main.route("/home/<username>")
@login_required
def index(username=None):
    print(f'current_user: {current_user}')
    '''
    included_parts = db.session.query.all(). \
        filter(Message.destination == "our part"). \
        cte(name="included_parts", recursive=True)

    query = sqlalchemy.select([
        BOOKS.c.genre,
        sqlalchemy.func.count(BOOKS.c.genre)
    ]).group_by(BOOKS.c.genre)

    # get all the records
    result = engine.execute(query).fetchall()
    '''
    return render_template("home.html", user=str(current_user.name))


@main.route("/check_credential")
def check_credential():
    return redirect(url_for('home'))


@main.route("/messi/discussion")
def detail():
    return render_template("detail.html", title='topic')

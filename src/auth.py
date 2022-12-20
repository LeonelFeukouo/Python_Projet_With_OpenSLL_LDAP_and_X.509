from flask import Blueprint, render_template, url_for, redirect, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html", title="")


@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    pseudo = request.form.get('pseudo')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(pseudo=pseudo).first()

    if not user or not check_password_hash(user.password, password):
        flash('veillez verifier vos information et recommencer encore !!!', 'danger')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    session['pseudo'] = user.pseudo
    session['room'] = user.pseudo
    session['global_room'] = 'salon'
    return redirect(url_for('main.index'))


@auth.route('/signup')
def signup():
    return render_template("signIn.html", title='inscription')


@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    number = request.form.get('number')
    name = request.form.get('name')
    surname = request.form.get('surname')
    pseudo = request.form.get('pseudo')
    password = request.form.get('password')

    user = User.query.filter_by(pseudo=pseudo).first()
    if user:
        flash(f' le pseudo {user.pseudo} existe deja', 'danger')
        return redirect(url_for('auth.signup'))
    new_user = User(surname=surname, name=name, pseudo=pseudo,
                    password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    flash(f' le pseudo {new_user.pseudo} est bien enregistré', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    session['name'] = ''
    session['room'] = ''
    flash(f' deconnection !!! ', 'success')
    return redirect(url_for('auth.login'))

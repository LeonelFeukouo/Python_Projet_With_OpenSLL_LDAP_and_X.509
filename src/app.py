from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from  flask_socketio import SocketIO, send
from datetime import datetime
from function.mysocket import sio

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tchat.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
socketio = SocketIO(app)
db = SQLAlchemy(app)
db.init_app(app)

user = 0
user_message = db.Table('user_message',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('message_id', db.Integer, db.ForeignKey('message.id'))
)

@socketio.on('message')
def handleMessage(msg):
    print('Message' +msg)
    send(msg,broadcast=True)

@socketio.event()
def connect(auth):
    global user
    user+=1
    print(user, 'connected')


@socketio.event()
def disconnect():
    global user
    user -= 1
    print(user, 'disconnected')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    pseudo = db.Column(db.String(50), unique=True, nullable=False)
    createAt = db.Column(db.TIMESTAMP, default=datetime.now, nullable=False)
    image_file = db.Column(db.String(50), nullable=False, default='default.png')
    password = db.Column(db.String(255), nullable=False)
    author = db.relationship('Message', secondary=user_message, backref='destination')

    def __repr__(self):
        return f"User('{self.username}', '{self.pseudo}', '{self.createAt}', '{self.image_file}')"


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    isRead = db.Column(db.Boolean, default=False, nullable=False)
    createAt = db.Column(db.TIMESTAMP, default=datetime.now, nullable=False)
    deleteAt = db.Column(db.Date)

    def __repr__(self):
        return f"Message('{self.content}', '{self.isRead}', '{self.createAt}')"




@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html", title="")


@app.route("/inscription")
def inscription():
    return render_template("signIn.html", title='inscription')


@app.route("/check_credential")
def check_credential():
    return redirect(url_for('home'))


@app.route("/signin")
def signin():
    return redirect(url_for('login'))


@app.route("/messi/discussion")
def detail():
    return render_template("detail.html", title='topic')


if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True)
    # app.run(debug=True)

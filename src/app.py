from flask import Flask, render_template, url_for, request, redirect, Response, flash

app = Flask(__name__)


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
    app.run(debug=True)

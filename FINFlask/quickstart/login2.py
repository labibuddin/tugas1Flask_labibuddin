from logging import error
from flask import Flask, app, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login-form.html", error=None)

def valid_login(uname, pwd):
    if uname == 'labibuddin' and pwd == 'alfin22':
        return True
    else:
        return False
    
def log_the_user_in(uname):
    return "SELAMAT!<br/>"+uname+" telah berhasil login."

@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
    else:
        error = 'Invalid username/password'
    return render_template("login-form.html", error=None)
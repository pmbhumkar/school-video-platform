from flask import Flask, render_template, url_for, redirect, request, session
from functools import wraps
import json

app = Flask(__name__)

video_data = {}

def setup():
    with open("config/subjects.json") as fd:
        global video_data
        video_data = json.load(fd)


@app.route('/')
def index():
    return render_template('index.html')


def is_logged_in(func):
    @wraps(func)
    def check_loggin_status(*args, **kwargs):
        if 'logged_in' in session:
            print("Logged in")
            return func(*args, **kwargs);
        else:
            return render_template('unauthorized.html'), 401
    return check_loggin_status


@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('dashboard.html', subjects=video_data)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_input = request.form['username']
        password_input = request.form['password']
        password = "admin123"
        username = "admin@gmail.com"
        session['logged_in'] = True
        session['username'] = username
        if username_input == username and password_input == password:
            print("Redirecting to dashboard")
            return redirect(url_for('dashboard'))
        else:
            print("Invalid username password")
            return render_template('index.html')
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear()
    print('Logged out')
	# flash('You are logged out', 'success')
    return render_template('index.html')

@app.route('/videoPlayer', methods=['GET'])
@is_logged_in
def videoPlayer():
    data = {
        "link": request.args['videolink'],
        "subject": request.args['subject'],
        "chapter": request.args['chapter'],
        "desc": request.args['desc']
    }
    
    return render_template('video.html', data=data)


if __name__ == '__main__':
    setup()
    app.secret_key = "secret123"
    app.run(debug=True)
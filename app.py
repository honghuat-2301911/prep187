from flask import Flask, render_template, request, redirect, url_for, session
# from dotenv import load_dotenv
# import os

def create_app():
    #load_dotenv()
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'VerySecure@71password'

    USERNAME = "user"
    PASSWORD = "pass"

    @app.route('/', methods=['GET'])
    def defaultpage():
        return render_template('login.html')
    

    @app.route('/', methods=['POST'])
    def login():
        message = ''
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if username == USERNAME and password == PASSWORD:
                session['user'] = username
                return redirect(url_for('home'))
            else:
                message = "Invalid username or password."
        return render_template('login.html', message=message)

    @app.route('/home')
    def home():
        if 'user' not in session:
            return redirect(url_for('login'))
        return render_template('home.html', user=session['user'])

    @app.route('/logout')
    def logout():
        session.pop('user', None)
        return redirect(url_for('login'))

    return app

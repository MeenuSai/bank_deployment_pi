#!/usr/bin/python
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os,pymysql

app = Flask(__name__)

@app.route('/')
def home():

    if not session.get('logged_in'):
        return render_template('newlogin.html')
    else:
        return render_template('home.html')

@app.route('/mainPage')
def mainPage():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'sheeba99' and request.form['username'] == 'babu':
        session['logged_in'] = True
        return redirect(url_for('mainPage'))
    else:
        flash('Wrong Password!')
        #return redirect(url_for('home'))
        return home()

@app.route('/newgoldloan',methods=['GET','POST'])
def newgoldloan():
    return render_template("newGoldLoan.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(12)


app.run('0.0.0.0',debug=True, port= 1110)

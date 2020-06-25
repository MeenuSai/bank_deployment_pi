#!/usr/bin/python
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os,pymysql

app = Flask(__name__)

@app.route('/')
def home():

    if not session.get('logged_in'):
        return render_template('newLogin.html')
    else:
        return render_template('index.html')

@app.route('/mainPage')
def mainPage():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return redirect(url_for('mainPage'))
    else:
        flash('Wrong Password!')
        #return redirect(url_for('home'))
        return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    flash('Logged Out Successfully')
    return home()


@app.route("/details", methods=['GET','POST'])
def details():
    flash("Details")
    cus_id = request.form['id']
    cus_name = request.form['name']
    data={'cus_id':id,'cus_name':name}

    try:
        conn =sqlite3.connect('bank_s/w_1.db')
        cur=conn.cursor()
        cur.execute('''INSERT INTO personal_details (id, name) VALUES ( ?, ?)''', ( cus_id,cus_name ) )
        conn.commit()
        conn.close()
        flash('Saved Successfully')
    except:
        flash('Error Saving Configurations')
    return redirect(url_for('mainPage'))


if __name__ == "__main__":
    app.secret_key = os.urandom(12)


app.run('0.0.0.0',debug=True, port= 1101)

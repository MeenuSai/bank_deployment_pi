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
    if request.form['password'] == 'sheeba99' and request.form['username'] == 'babu':
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
    cus_name = request.form['name']
    cus_phno = request.form['mobile_number']
    cus_interest = int(request.form['weight'])*3
    cus_address = request.form['address']


#     try:
    data={'name':cus_name,'mobile_number':cus_phno,'weight':cus_interest,'address':cus_address}    
    conn =pymysql.connect(database="bank",user="admin",password="admin",host="localhost")
    cur=conn.cursor()
    cur.execute("INSERT INTO personal_details (name, ph, weight,address) VALUES (%(name)s, %(mobile_number)s, %(weight)s, %(address)s);",data)
    conn.commit()
    conn.close()
    flash('Saved Successfully')
#     except:
#        flash('Error Saving Configurations')
    return redirect(url_for('mainPage'))

if __name__ == "__main__":
    app.secret_key = os.urandom(12)


app.run('0.0.0.0',debug=True, port= 1110)

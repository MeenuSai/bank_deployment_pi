#!python3
from flask import Flask, request, render_template
app =Flask(__name__)

@app.route('/login', methods = ['GET','POST'])
def form():
    name = ''
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        AccNo = request.form.get('userAccNo')
    return render_template("index.html", name=name )

@app.route('/sucess', methods = ['GET','POST'])
def sucess():
    return "Login Successfull"
app.run('0.0.0.0',debug=1,port=1010)

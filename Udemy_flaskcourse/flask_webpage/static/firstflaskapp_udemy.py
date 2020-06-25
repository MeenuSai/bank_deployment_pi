#!python3

from flask import Flask, request, render_template

app =Flask(__name__)
@app.route('/1')
def welcomepage():
    return "This is my first Flask App"
@app.route('/')
def Secondpage():
    return render_template("index.html")
@app.route('/3')
def thirdpage():
    return "This is my third Flask App"

@app.route('/postmethod',methods = ['GET', 'POST'])
def method():
    if request.method == 'POST':
        return "U have used a POST request"
    else:
        return 'I reckon u are probably using GET request'
app.run('0.0.0.0',debug=1,port=1010)



<a class="pure-button" href="#">Submit</a>
<button class="pure-button">Click</button>
<img src="static/Images/SAIRAM.jpg" alt="ShraddhaSaburi" style="width:500px;height:600px;">



border: 10px solid blue;

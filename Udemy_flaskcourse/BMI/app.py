#!python3
from flask import Flask, request, render_template
app =Flask(__name__)

@app.route('/bmi', methods = ['GET','POST'])
def form():
    bmi = '' 
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = bmi_cal(weight,height)
    return render_template("index.html",bmi=bmi)

def bmi_cal(weight,height):
    return round(weight/((height/100)**2), 2)


app.run('0.0.0.0',debug=1,port=1010)

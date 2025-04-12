from flask import Flask, render_template, redirect,request,session
from pymongo import MongoClient
import random

app = Flask(__name__)

app.secret_key = "1123"

client = MongoClient('mongodb://localhost:27017/')
db = client['user_auth_db']
users_collection = db['users']

@app.route('/')
def home():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    Name = request.form.get('name')
    p_number = request.form.get('phone_number')
    session['phone'] = p_number
    if p_number and Name:
        return render_template('otp.html')
    else:
        return render_template('register.html')

@app.route('/otp', methods=['GET','POST'])
def otp():
    phone = session.get('phone')
    #mailed_otp = random.randint(100000,999999)
    #send_otp(phone,mailed_otp)
    mailed_otp = 123456
    otp1=request.form.get('index1')
    otp2=request.form.get('index2')
    otp3=request.form.get('index3')
    otp4=request.form.get('index4')
    otp5=request.form.get('index5')
    otp6=request.form.get('index6')
    otp = [otp1,otp2,otp3,otp4,otp5,otp6]
    mailed_otp_str = str(mailed_otp)
    if ''.join(otp) == mailed_otp_str:
        session['logged_in'] = True
        return render_template('home.html')
    else:
        render_template('otp.html')


if __name__ == '__main__':
    app.run(debug=True)
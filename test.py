#coding=utf-8
from flask import Flask,render_template,request,session,abort,redirect,jsonify,make_response
import sqlite3
from function import hash_code
from flask import flash

app = Flask(__name__)
app.config['SECRET_KEY']='nemo'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/know/')
def know():
    return render_template('know.html')

@app.route('/learn/')
def learn():
    return render_template('learn.html')

@app.route('/gift/')
def gifts():
    return render_template('gift.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@app.route('/login/')
def Login():
    return render_template('login.html')

@app.route('/register/')
def reigister():
    return render_template('register.html')







if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True,port='5000')


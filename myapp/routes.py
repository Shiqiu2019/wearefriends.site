from myapp import app
from flask import Flask, render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Suzhou')
def suzhou_index():
    return render_template('suzhou_index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Suzhou/test')
def suzhou_test():
    return render_template('suzhou_test.html')

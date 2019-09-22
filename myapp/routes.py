from myapp import app
from myapp.forms import LoginForm
from flask import Flask, render_template, flash, redirect, url_for


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Successfully login')
        # flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/Suzhou')
def suzhou_index():
    return render_template('suzhou_index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Suzhou/test')
def suzhou_test():
    return render_template('suzhou_test.html')

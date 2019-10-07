from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'kobi'}
    posts = [{
            'author': {'username': 'John', 'age': 23},
            'body': 'Beautiful day in Portland!'
        },{
            'author': {'username': 'Susan', 'age': 45},
            'body': 'The Avengers movie was so cool!'
        }]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requestd for the user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

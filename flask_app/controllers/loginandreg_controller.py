from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.loginandreg import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

#______Login and Register page_____
@app.route('/')
def index():
    return redirect('/welcome')

@app.route('/user')
def render_login():
    return render_template('index.html')



@app.route('/register', methods=['post'])
def register_user():
    #____Validation______
    if not User.validate_user(request.form):
        return redirect('/user')
    # _____Password hash_____
    pw_hash = bcrypt.generate_password_hash(request.form['password'])    
    user_id = User.create_user({**request.form,"password" : pw_hash})
    session['user_id'] = user_id
    return redirect(f'/passport/{user_id}')




@app.route('/login', methods=['POST'])
def login():
    user_in_db = User.get_email({ "email" : request.form["email"] })
    #____IF the email is not found
    if not user_in_db:
        flash('Invalid Email/Password', 'error')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password', 'error')
        return redirect('/user')
    session['user_id'] = user_in_db.id
    return redirect(f'/passport/{user_in_db.id}')


# @app.route('/welcome')
# def welcome_user():
#     #!------Route Guard--------
#     if 'user_id' not in session:
#         return redirect('/')
#     user = User.get_id({'id': session['user_id']})
#     return render_template('result.html', user = user)

@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')







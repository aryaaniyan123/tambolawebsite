from app import app
from flask import Flask, render_template, flash, redirect, request, session, logging, url_for

from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm, RegisterForm

from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import config
import models,resource



db = SQLAlchemy(app)
jwt = JWTManager(app)
class User(db.Model):

    __tablename__ = 'usertable'

    id = db.Column(db.Integer, primary_key=True)

    name= db.Column(db.String(15), unique=True)

    username = db.Column(db.String(15), unique=True)

    email = db.Column(db.String(50), unique=True)

    password = db.Column(db.String(256), unique=True)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register/', methods = ['GET', 'POST'])
def register():
     form = RegisterForm(request.form)
     if request.method == 'POST' and form.validate():
         hashed_password = generate_password_hash(form.password.data, method='sha256')
         new_user = User(

            name = form.name.data, 

            username = form.username.data, 

            email = form.email.data, 

            password = hashed_password )
            # saving 
         db.session.add(new_user)

         db.session.commit()
         flash('You have successfully registered', 'success')
         return redirect(url_for('login'))

     else:
        return render_template('register.html', form = form)    



@app.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate:
        user = User.query.filter_by(email = form.email.data).first()
        if user:
            
            if check_password_hash(user.password, form.password.data):
                
                flash('You have successfully logged in.', "success")

                session['logged_in'] = True

                session['email'] = user.email 

                session['username'] = user.username
        
                return redirect(url_for('home'))

            else:

                flash('Username or Password Incorrect', "Danger")

                return redirect(url_for('login'))
        return render_template('login.html', form = form)
  
                
@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))


@app.before_first_request
def create_tables():
    db.create_all()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):

    jti = decrypted_token['jti']

    return models.RevokedTokenModel.is_jti_blacklisted(jti)



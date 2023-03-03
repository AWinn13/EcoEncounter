from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB, app
import re
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*\W).{8,}$')

class User:
    def __init__(self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        


    #!Iterate over the db results and create instances of results with cls.*******
    @classmethod
    def get_all_results(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DB).query_db(query)
        users= []
        for i in results:
            users.append(cls(i) )
        return users


    #!--------------create user----------------
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DB).query_db(query, data)
    
    #!---------------login email validation----------------
    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
        

#!--------------USER validation--------------
    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['first_name']) < 3:
            flash("First name must be at least 3 characters.", 'reg_error')
            is_valid = False
        if len(data['last_name']) < 3:
            flash("Last name must be at least 3 characters.", 'reg_error')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash(u"Invalid email address!", 'reg_error')
            is_valid = False
        if  User.get_email({ "email" : data["email"]}):
            flash('Email already taken', 'reg_error')
            is_valid = False
        if not PASSWORD_REGEX.match(data['password']):
            flash("password must be at least 8 characters and include 1 symbol !@#$%^&*()", 'reg_error')
            is_valid = False
        elif not data['password'] == data['confirm_password']:
            flash("passwords don't match", 'reg_error')
            is_valid = False
        return is_valid
    


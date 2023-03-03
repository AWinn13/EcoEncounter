from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DB
from flask import flash
from flask_app.models import loginandreg

class Picture:

    def __init__(self,data):
        self.id = data['id']
        self.filename = data['filename']
        self.location = data['location']
        self.caption = data['caption']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.taker = None

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO pictures (filename, location, caption, user_id) values (%(filename)s, %(location)s, %(caption)s, %(user_id)s);
        """
        print('=============================', data)
        return connectToMySQL(DB).query_db( query , data )
    
    @classmethod
    def get_all(cls, data):
        query = """ Select * from pictures where user_id = %(user_id)s;
        """
        results = connectToMySQL(DB).query_db(query, data)
        pictures= []
        for i in results:
            pictures.append(cls(i))
        return pictures
    
    @classmethod
    def get_one_picture(cls, data):
        query = "SELECT * FROM pictures LEFT JOIN users ON users.id = pictures.user_id WHERE pictures.id= %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if results:
            this_picture = cls(results[0])
            row = results[0]
            user_data= {
                    **row,
                    "id" : row["users.id"],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at'],
                }
                
            this_user = loginandreg.User(user_data)
            this_picture.taker = this_user
            return this_picture
        return False


    @classmethod
    def update(cls, data):
        query = "UPDATE pictures SET filename=filename,location=%(location)s, caption=%(caption)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db( query, data )
    
    @classmethod
    def delete(cls, data):
        query  = "DELETE FROM pictures WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)
    
    @staticmethod
    def validate_pic(data):
        is_valid = True
        if len(data['file']) < 1:
            flash("file can't be blank.", 'reg_error')
            is_valid = False
        if len(data['location']) < 3:
            flash("Location must be at least 3 letters.", 'reg_error')
            is_valid = False
        if len(data['caption']) < 1:
            flash("Must select an ecosystem.", 'reg_error')
            is_valid = False
        return is_valid

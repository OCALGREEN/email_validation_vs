
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class LogIn:
    def __init__(self, data): # data is a dictionary that hold data from the database
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        result = connectToMySQL("email_validation_schema").query_db(query, data) # query here is the id from the table
        return result
    
    @staticmethod
    def validator(login):
        is_valid = True
        if not EMAIL_REGEX.match(login["email"]):
            flash("Invalid Email Adress")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;" # create query
        result = connectToMySQL("email_validation_schema").query_db(query) # receive or send data from db
        emails = []
        for row in result:
            emails.append(cls(row))
        return emails 

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        connectToMySQL("email_validation_schema").query_db(query, data)
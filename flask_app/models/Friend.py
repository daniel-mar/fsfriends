from flask_app.config.mysqlconnection import connectToMySQL
# from flask import flash
# import re

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, occupation, age, updated_at, created_at) VALUES(%(first_name)s, %(last_name)s, %(occupation)s, %(created_at)s, %(updated_at)s, NOW(), NOW() )"
        return connectToMySQL('friend_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # config file connection
        results = connectToMySQL('friend_schema').query_db(query)
        users = []
        # Row = User
        for row in results:
            users.append(cls(row))
        return users
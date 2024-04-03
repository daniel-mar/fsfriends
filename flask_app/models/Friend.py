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
        self.age = data['age']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, age, updated_at, created_at) VALUES(%(first_name)s, %(last_name)s, %(occupation)s, %(age)s, NOW(), NOW() )"

        return connectToMySQL('friend_shema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # config file connection
        results = connectToMySQL('friend_shema').query_db(query)
        users = []
        # Row = User
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def get_one_friend(cls, data):
        query = "SELECT * FROM friends WHERE id = %(friend_id)s;"
        results = connectToMySQL('friend_shema').query_db(query, data)
        return cls(results[0])
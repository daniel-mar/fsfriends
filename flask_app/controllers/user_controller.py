from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.friend import Friend

@app.route("/")
def index():
    friends = Friend.get_all()
    return render_template("index.html", all_friends = friends)

@app.route("/friend/<int:friend_id>")
def one_friend(friend_id):
    friend_data = {
        "friend_id": friend_id
    }
    one_friend = Friend.get_one_friend(friend_data)

    return render_template("showone.html", friend = one_friend)


@app.route("/friend/new")
def new_friend():
    return render_template('addFriend.html')

@app.route("/friend/create", methods=["POST"])
def create_friend():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "occupation": request.form["occupation"],
        "age": request.form["age"]
    }
    Friend.save(data)

    return render_template("index.html")
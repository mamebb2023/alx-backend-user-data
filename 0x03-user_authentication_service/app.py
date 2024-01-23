#!/usr/bin/env python3
""" Flask API
"""
from flask import Flask, jsonify

from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", strict_slashes=False)
def index():
    """ index page
    """
    return jsonify(message="Bienvenue")


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """ Register user
    """
    email = request.form.get("email")
    pwd = request.form.get("password")

    if email is None or pwd is None:
        return

    try:
        AUTH.register_user(email, pwd)
        return jsonfy(email=email, message="user created")
    except ValueError:
        return jsonfy(message="email already registered"), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

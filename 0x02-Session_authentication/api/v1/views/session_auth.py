#!/usr/bin/env python3
""" Session View
"""
from os import getenv
from flask import jsonify, request

from api.v1.views import app_views
from models.user import User


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def usr_login():
    """ User Session Login
    """
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not pwd:
        return jsonify({"error": "password missing"}), 400

    valid_user = User.search({"email": email})
    if not valid_user:
        return jsonify({"error": "no user found for this email"}), 401

    valid_user = valid_user[0]
    if not valid_user.is_valid_password(pwd):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    s_id = auth.create_session(valid_user.id)
    r = jsonify(valid_user.to_json())
    r.set_cookie(getenv("SESSION_NAME"), s_id)
    return r

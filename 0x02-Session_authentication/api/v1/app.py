#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

if getenv("AUTH_TYPE") == "session_auth":
    auth = SessionAuth()
elif getenv("AUTH_TYPE") == "basic_auth":
    auth = BasicAuth()
else:
    auth = Auth()


@app.before_request
def check_auth():
    """ Authorization Checker
    """
    excluded_list = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/', '/api/v1/auth_session/login/']  # nopep8
    requires_auth = auth.require_auth(request.path, excluded_list)

    if not requires_auth:
        return None
    if not auth.authorization_header(request) and not auth.session_cookie(request):  # nopep8
        abort(401)

    user = auth.current_user(request)
    if not user:
        abort(403)
    request.current_user = user


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized error handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(errro) -> str:
    """ Forbidden error handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)

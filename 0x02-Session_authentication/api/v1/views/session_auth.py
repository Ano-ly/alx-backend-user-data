#!/usr/bin/env python3
"""Authorization class for API"""
from api.v1.views import app_views
from api.v1.app import auth
from flask import request, session, jsonify
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def session_authentication() -> str:
    """Session authentication"""
    email = request.form.get('email')
    if email is None:
        return (jsonify({"error": "email missing"}), 400)
    password = request.form.get('password')
    if password is None:
        return (jsonify({"error": "password missing"}), 400)
    result = User.search({'email': email})
    if len(result) == 0:
        return (jsonify({"error": "no user found for this email"}), 404)
    else:
        the_user = result[0]
        if the_user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(the_user.id)
            my_return = jsonify(the_user.to_json())
            my_return.set_cookie(os.getenv('SESSION_NAME'), session_id)
            return (my_return)
        return (jsonify({"error": "wrong password"}), 401)


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """Destroy session and logout"""
    ret_val = auth.destroy_session(request)
    if ret_val is False:
        abort(404)
    return (jsonify({}), 200)

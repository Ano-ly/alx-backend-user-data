#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

if os.getenv('AUTH_TYPE') == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
if os.getenv('AUTH_TYPE') == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.before_request
def auth_b_r():
    """Check for unauthorized paths
    """
    if auth is not None:
        blacklist = ['/api/v1/status/',
                     '/api/v1/unauthorized/',
                     '/api/v1/forbidden/']
        req_auth = auth.require_auth(request.path, blacklist)
        if req_auth is True:
            if auth.authorization_header(request) is None:
                abort(401)
            if auth.current_user(request) is None:
                abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return (jsonify({"error": "Not found"}), 404)


@app.errorhandler(401)
def not_auth(error) -> str:
    """ Not authorized handler
    """
    return (jsonify({"error": "Unauthorized"}), 401)


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden route  handler
    """
    return (jsonify({"error": "Forbidden"}), 403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)

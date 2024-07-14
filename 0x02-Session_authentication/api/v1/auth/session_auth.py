#!/usr/bin/env python3
"""Authorization class for API"""
import base64
from api.v1.auth.auth import Auth
from flask import request
from models.user import User
from typing import List, TypeVar


class SessionAuth(Auth):
    """SessionAuth class definition
    """

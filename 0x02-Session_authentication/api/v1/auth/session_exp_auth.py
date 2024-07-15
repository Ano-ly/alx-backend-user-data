#!/usr/bin/env python3
"""Authorization class for API"""
import base64
from api.v1.auth.auth import Auth
from flask import request
from models.user import User
from typing import List, TypeVar

class SessionExpAuth(SessionAuth):
    """Expiration for a session"""
    def __init__(self):
        dur = os.getenv('SESSION_DURATION')
        if dur is None:
            self.session_duration = 0
        else:
            self.session_duration = dur

    def create_session(self, user_id=None):
        """Create an expirable session""" 


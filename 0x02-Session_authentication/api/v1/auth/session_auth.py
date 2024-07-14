#!/usr/bin/env python3
"""Authorization class for API"""
import base64
from api.v1.auth.auth import Auth
from flask import request
from models.user import User
from typing import List, TypeVar
import uuid


class SessionAuth(Auth):
    """SessionAuth class definition
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a new session fo a user"""
        if user_id is None:
            return (None)
        if type(user_id) != str:
            return (None)
        new_id = uuid4()
        user_id_by_session_id.update({new_id: user_id})
        return (new_id)

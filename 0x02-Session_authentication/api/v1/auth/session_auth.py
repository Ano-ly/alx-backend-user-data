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
        new_id = str(uuid.uuid4())
        self.user_id_by_session_id.update({new_id: user_id})
        return (new_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Obtain the user_id attached to a session id"""
        if session_id is None:
            return (None)
        if type(session_id) != str:
            return (None)
        return (self.user_id_by_session_id.get(session_id))

    def current_user(self, request=None):
        """Return a user instance based on a cookie value"""
        ses_kie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(ses_kie)
        print(User.get(user_id))
        return (User.get(user_id))

    def destroy_session(self, request=None):
        """Destroy the session"""
        if request is None:
            print("1, I returned false")
            return (False)
        session_id = self.session_cookie(request)
        if session_id is None:
            print("1, I returned false")
            return (False)
        if self.user_id_for_session_id(session_id) is None:
            print("1, I returned false")
            return (False)
        del self.user_id_by_session_id[session_id]
        print("1, I returned ")
        return (True)

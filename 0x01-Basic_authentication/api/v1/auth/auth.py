#!/usr/bin/env python3
"""Authorization class for API"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class for API"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if path requires authentication for access
        """
        if path is None or excluded_paths is None:
            return (True)
        if len(excluded_paths) == 0:
            return (True)
        if path[-1] != '/':
            path = path + '/'
        if path in excluded_paths:
            return (False)
        if path not in excluded_paths:
            return (True)
        for ex_path in excluded_paths:
            if ex_path[-1] == '*':
                if ex_path[:-1] in path:
                    return (False)

    def authorization_header(self, request=None) -> str:
        """Authorisation header
        """
        if request is None:
            return (None)
        if 'Authorization' not in request.headers:
            return (None)
        else:
            return (request.headers.get('Authorization'))

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user
        """
        return (None)

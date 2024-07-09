#!/usr/bin/env python3
"""Authorization class for API"""
import request from Flask


class Auth:
    """Authentication class for API"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if path requires authentication for access
        """
        return (False)

    def authorization_header(self, request=None) -> str:
        """Authorisation header
        """
        return (None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user
        """
        return (None)

#!/usr/bin/env python3
"""Authorization class for API"""
import base64
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class definition
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract base64 authorization header"""
        if authorization_header is None:
            return (None)
        if type(authorization_header) != str:
            return (None)
        if authorization_header.startswith('Basic ') is False:
            return (None)
        return (authorization_header[6:])

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Base64 decoding
        """
        if base64_authorization_header is None:
            return (None)
        if type(base64_authorization_header) != str:
            return (None)
        try:
            decoded = base64.decodebytes(
                    base64_authorization_header.encode('utf-8'))
        except Exception:
            return (None)
        else:
            return (decoded.decode('utf-8'))

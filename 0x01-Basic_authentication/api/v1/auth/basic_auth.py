#!/usr/bin/env python3
"""Authorization class for API"""
from flask import request
from typing import List, TypeVar
from api.vi.auth.auth import Auth


class BasicAuth(Auth):
    pass

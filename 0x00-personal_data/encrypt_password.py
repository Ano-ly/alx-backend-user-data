#!/usr/bin/env python3
"""Encrypt user password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password"""
    password = password.encode("utf-8")

    new_hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return (new_hashed)

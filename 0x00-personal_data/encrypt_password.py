#!/usr/bin/env python3
"""Encrypt user password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password"""
    password = password.encode("utf-8")

    new_hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return (new_hashed)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if a password is valid"""
    if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
        return (True)
    else:
        return (False)

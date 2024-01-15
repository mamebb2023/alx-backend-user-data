#!/usr/bin/env python3
""" Encrypt Password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashes a users password
    """
    b_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return b_hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks if hashed password and password matches
    """
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    return False

#!/usr/bin/env python3
""" Authuntication
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Password encrypt
    """
    if not password:
        return None

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

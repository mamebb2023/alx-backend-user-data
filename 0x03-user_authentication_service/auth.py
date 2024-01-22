#!/usr/bin/env python3
""" Authuntication
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import Base, User


def _hash_password(password: str) -> bytes:
    """ Password encrypt
    """
    if not password:
        return None

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """ Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ User Registeration
        """
        found = True
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            found = False
        if found:
            raise ValueError(f"User {email} already exists")
        return self._db.add_user(email, _hash_password(password))

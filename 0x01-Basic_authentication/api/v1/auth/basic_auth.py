#!/usr/bin/env python3
""" Basic Authorization
"""
from base64 import b64decode as decode
from typing import TypeVar

from api.v1.auth.auth import Auth
from models.user import User
from models.base import Base


class BasicAuth(Auth):
    """ Basic Authorization class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:  # nopep8
        """ Extract Base64 Authorization
        """
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:  # nopep8
        """ Decode Base64 Authorization Header
        """
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return decode(base64_authorization_header).decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):  # nopep8
        """ Extract User Info
        """
        if not decoded_base64_authorization_header:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        crd = decoded_base64_authorization_header.split(":")
        email = crd[0]
        pwd = crd[1]

        return (email, pwd)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):  # nopep8
        """ User Object from Credentials
        """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None
        try:
            if User.count() == 0:
                return None
        except BaseException:
            return None

        user = User.search({"email": user_email})
        if not user:
            return None
        if not user[0].is_valid_password(user_pwd):
            return None
        return user[0]

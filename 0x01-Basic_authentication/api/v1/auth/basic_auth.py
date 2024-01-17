#!/usr/bin/env python3
""" Basic Authorization
"""
from base64 import b64decode as decode

from api.v1.auth.auth import Auth


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

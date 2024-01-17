#!/usr/bin/env python3
""" Basic Authorization
"""
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

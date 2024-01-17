#!/usr/bin/env python3
""" Auth API
"""
from flask import requests


class Auth():
    """ Authentication Object
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require Auth
        """
        return False


    def authorization_header(self, request=None) -> str:
        """ Authorization Header
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User
        """
        return None

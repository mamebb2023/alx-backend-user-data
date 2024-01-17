#!/usr/bin/env python3
""" Auth API
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ Authentication Object
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require Auth
        """
        if not path or not excluded_paths:
            return True
        p_path = path + '/' if path[-1] != '/' else path
        for p_path in excluded_paths:
            t_path = path[:-1] if path[-1] != '*' else path
            if p_path.startswith(t_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Authorization Header
        """
        if not request:
            return None
        req_header = request.headers.get('Authorization')
        if not req_header:
            return None
        return req_header

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User
        """
        return None

class BasicAuth():
    """ Basic Authorization
    """
    None

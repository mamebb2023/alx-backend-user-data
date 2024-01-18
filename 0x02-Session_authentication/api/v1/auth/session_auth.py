#!/usr/bin/env python3
""" Session Authentication
"""
import uuid
from typing import TypeVar

from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """ Session Authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a session for user_id
        """
        if not user_id or not isinstance(user_id, str):
            return None
        s_id = str(uuid.uuid4())
        self.user_id_by_session_id[s_id] = user_id
        return s_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Return user_id based on session_id
        """
        if not session_id or not isinstance(session_id, str):
            return None

        u_id = self.user_id_by_session_id.get(session_id)
        return u_id

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns a user instance based on a cookie value
        """
        if not request:
            return None
        s_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(s_id)
        return User.get(user_id)

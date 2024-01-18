#!/usr/bin/env python3
""" Session Authentication
"""
import uuid

from api.v1.auth.auth import Auth


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

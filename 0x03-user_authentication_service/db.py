#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """ DB class
    """

    def __init__(self) -> None:
        """ Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """ Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ User Registration
        """
        new_user = User(email=email, hashed_password=hashed_password)
        try:
            self._session.add(new_user)
            self._session.commit()
        except Exception as e:
            print(f"Error adding user to database: {e}")
            self._session.rollback()
            raise
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Find a user by arguments
        """
        for arg in kwargs.keys():
            if not hasattr(User, arg):
                raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Update User
        """
        user = None
        try:
            user = self.find_user_by(id=user_id)
        except NoReslutFound:
            return

        for k, v in kwargs.items():
            if k not in user.__dict__:
                raise ValueError
            setattr(user, k, v)
        self._session.add(user)
        self._session.commit()

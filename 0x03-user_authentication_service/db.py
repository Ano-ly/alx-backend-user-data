"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email, hashed_password) -> User:
        """Adds a user to the database"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return (new_user)

    def find_user_by(self, **kwargs):
        """Find a user by certain attributes"""
        user_found = self._session.query(User).filter_by(**kwargs).first()
        if user_found is None:
            raise NoResultFound
        return (user_found)

    def update_user(self, user_id, **kwargs) -> None:
        """Update user details"""
        valid_attr = ['id',
                      'email',
                      'hashed_password',
                      'session_id',
                      'reset_token']
        for key in kwargs.keys():
            if key not in valid_attr:
                raise ValueError
            user = self.find_user_by(id=user_id)
            for k, v in kwargs.items():
                setattr(user, k, v)
            self._session.add(user)
            self._session.commit()
        return (None)

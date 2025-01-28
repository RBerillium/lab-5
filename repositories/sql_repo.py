from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from repositories.db_models import Base, UserModel
from models import User
from repositories.base import BaseRepository
from typing import List


class SQLAlchemyUserRepository(BaseRepository[User]):
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        Base.metadata.create_all(self.engine)

    def add(self, obj: User) -> None:
        with self.Session() as session:
            user = UserModel(**obj.__dict__)
            session.add(user)
            session.commit()

    def get_all(self) -> List[User]:
        with self.Session() as session:
            users = session.query(UserModel).all()
            return [User(**user.__dict__) for user in users]

    def find_by_id(self, obj_id: int) -> User:
        with self.Session() as session:
            user = session.query(UserModel).filter(UserModel.user_id == obj_id).first()
            if user:
                return User(**user.__dict__)
            return None

    def delete(self, obj_id: int) -> None:
        with self.Session() as session:
            user = session.query(UserModel).filter(UserModel.user_id == obj_id).first()
            if user:
                session.delete(user)
                session.commit()

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from repositories.sql_repo import SQLAlchemyUserRepository
from repositories.db_models import Base


class UnitOfWork:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine = create_engine(self.database_url)
        self.session = None

    def __enter__(self):
        self.session = Session(bind=self.engine)
        self.user_repository = SQLAlchemyUserRepository(self.session)  # Репозиторий с текущей сессией
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.session.commit()  # Подтверждаем изменения
        else:
            self.session.rollback()  # Откатываем, если есть ошибка
        self.session.close()  # Закрываем сессию

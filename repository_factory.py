from repositories.sql_repo import SQLAlchemyUserRepository
from repositories.json_repo import JSONRepository
from repositories.xml_repo import XMLRepository  # Предполагается, что есть XMLRepository
from typing import Union


class RepositoryFactory:
    @staticmethod
    def create_repository(storage_type: str, *args, **kwargs):
        """
        Фабричный метод для создания репозитория.
        
        :param storage_type: Тип хранилища ('sql', 'json', 'xml')
        :param args: Позиционные аргументы для конструктора репозитория
        :param kwargs: Именованные аргументы для конструктора репозитория
        :return: Экземпляр репозитория
        """
        if storage_type == "sql":
            return SQLAlchemyUserRepository(*args, **kwargs)
        elif storage_type == "json":
            return JSONRepository(*args, **kwargs)
        elif storage_type == "xml":
            return XMLRepository(*args, **kwargs)
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")

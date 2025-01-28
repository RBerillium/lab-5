from case_layer import *
from models import *
from repositories.xml_repo import *


'''if __name__ == "__main__":
    # Создаём репозиторий
    user_repo = UserXMLRepository("users.xml")
    workout_repo = ...  # Аналогично создать репозиторий для тренировок
    goal_repo = ...  # Аналогично создать репозиторий для целей

    # Создаём сервис
    service = TrainingDiaryService(user_repo, workout_repo, goal_repo)

    # Добавляем пользователя
    user = User(1, "John Doe", 30, "Male", 80.0, 180.0)
    service.add_user(user)

    # Получаем всех пользователей
    users = service.user_repo.get_all()
    for user in users:
        print(user.name)

        from repository_factory import RepositoryFactory

# Пример: JSON хранилище
json_repo = RepositoryFactory.create_repository("json", "users.json")
json_repo.add({"id": 1, "name": "John Doe", "age": 30})
print(json_repo.get_all())

# Пример: SQL хранилище
sql_repo = RepositoryFactory.create_repository("sql", "sqlite:///users.db")
sql_repo.add({"id": 2, "name": "Jane Doe", "age": 25})
print(sql_repo.get_all())
'''

import asyncio
from user_fsm import *

async def main():
    # Запуск конечного автомата
    await user_state_machine("registered")

if __name__ == "__main__":
    asyncio.run(main())
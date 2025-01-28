from case_layer import *
from models import *
from xml_repo import *


if __name__ == "__main__":
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
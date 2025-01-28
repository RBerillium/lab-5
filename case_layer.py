from datetime import date
from typing import List
from models import User, Workout, UserGoal, has_overlapping_workouts, workout_has_exercises, goals_are_unique

class TrainingDiaryService:
    def __init__(self, user_repo, workout_repo, goal_repo):
        self.user_repo = user_repo
        self.workout_repo = workout_repo
        self.goal_repo = goal_repo

    def add_user(self, user: User):
        self.user_repo.add(user)

    def add_workout(self, workout: Workout):
        # Проверяем пересечения тренировок перед добавлением
        existing_workouts = self.workout_repo.get_all()
        if has_overlapping_workouts(existing_workouts + [workout]):
            raise ValueError("Workout overlaps with an existing workout.")
        self.workout_repo.add(workout)

    def add_goal(self, goal: UserGoal):
        # Проверяем уникальность целей
        existing_goals = self.goal_repo.get_all()
        if not goals_are_unique(existing_goals + [goal]):
            raise ValueError("Goal descriptions must be unique.")
        self.goal_repo.add(goal)

    def get_user_workouts(self, user_id: int) -> List[Workout]:
        # Получаем тренировки конкретного пользователя
        return [workout for workout in self.workout_repo.get_all() if workout.user_id == user_id]

    def check_user_goals_validity(self, current_date: date) -> bool:
        # Проверяем все цели на валидность сроков
        goals = self.goal_repo.get_all()
        return all(goal.deadline >= current_date for goal in goals)

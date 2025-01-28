from dataclasses import dataclass
from datetime import date, time, datetime, timedelta
from typing import List, Optional

# === Объекты-значения ===
@dataclass(frozen=True)
class Exercise:
    exercise_id: int
    name: str
    description: str
    exercise_type: str

@dataclass(frozen=True)
class UserGoal:
    goal_id: int
    user_id: int
    goal_description: str
    deadline: date

@dataclass
class WorkoutLog:
    log_id: int
    user_id: int
    workout_id: int
    notes: Optional[str] = None

@dataclass
class ExerciseResult:
    result_id: int
    workout_id: int
    exercise_id: int
    repetitions: Optional[int] = None
    weight_used: Optional[float] = None
    duration: Optional[int] = None

# === Классы-сущности ===
class User:
    def __init__(self, user_id: int, name: str, age: int, gender: str, weight: float, height: float):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.user_id == other.user_id

    def __str__(self):
        return f"User(id={self.user_id}, name='{self.name}', age={self.age}, gender='{self.gender}', weight={self.weight}, height={self.height})"

class Workout:
    def __init__(self, workout_id: int, user_id: int, date: date, start_time: time, duration: int, workout_type: str):
        self.workout_id = workout_id
        self.user_id = user_id
        self.date = date
        self.start_time = start_time
        self.duration = duration
        self.workout_type = workout_type

    def __eq__(self, other):
        if not isinstance(other, Workout):
            return False
        return (
            self.workout_id == other.workout_id and
            self.date == other.date and
            self.start_time == other.start_time
        )

    def __str__(self):
        return (f"Workout(id={self.workout_id}, user_id={self.user_id}, date={self.date}, "
                f"start_time={self.start_time}, duration={self.duration}, type='{self.workout_type}')")

# === Классы-функции бизнес-логики ===
def has_overlapping_workouts(workouts: List[Workout]) -> bool:
    # Группируем тренировки по user_id
    workouts_by_user = {}
    for workout in workouts:
        if workout.user_id not in workouts_by_user:
            workouts_by_user[workout.user_id] = []
        workouts_by_user[workout.user_id].append(workout)

    # Проверяем пересечения отдельно для каждого пользователя
    for user_workouts in workouts_by_user.values():
        # Сортируем тренировки пользователя по дате и времени начала
        sorted_workouts = sorted(user_workouts, key=lambda w: (w.date, w.start_time))
        
        for i in range(len(sorted_workouts) - 1):
            current = sorted_workouts[i]
            next_workout = sorted_workouts[i + 1]

            # Преобразуем в datetime для проверки пересечения
            current_start = datetime.combine(current.date, current.start_time)
            current_end = current_start + timedelta(minutes=current.duration)
            
            next_start = datetime.combine(next_workout.date, next_workout.start_time)

            # Если конец текущей тренировки позже начала следующей, есть пересечение
            if current_end > next_start:
                return True
    return False


def workout_has_exercises(workout_id: int, exercise_results: List[ExerciseResult]) -> bool:
    return any(result.workout_id == workout_id for result in exercise_results)

def goals_are_unique(goals: List[UserGoal]) -> bool:
    descriptions = [goal.goal_description for goal in goals]
    return len(descriptions) == len(set(descriptions))

def goals_have_valid_deadlines(goals: List[UserGoal], current_date: date) -> bool:
    return all(goal.deadline >= current_date for goal in goals)

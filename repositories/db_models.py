from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# SQLAlchemy модель для пользователя
class UserModel(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Float, nullable=False)

# SQLAlchemy модель для тренировки
class WorkoutModel(Base):
    __tablename__ = 'workouts'

    workout_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    duration = Column(Integer, nullable=False)
    workout_type = Column(String, nullable=False)

# SQLAlchemy модель для результата упражнения
class ExerciseResultModel(Base):
    __tablename__ = 'exercise_results'

    result_id = Column(Integer, primary_key=True, autoincrement=True)
    workout_id = Column(Integer, ForeignKey('workouts.workout_id'), nullable=False)
    exercise_id = Column(Integer, nullable=False)
    repetitions = Column(Integer)
    weight_used = Column(Float)
    duration = Column(Integer)

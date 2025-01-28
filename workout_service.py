from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Workout(BaseModel):
    id: int
    user_id: int
    date: str
    start_time: str
    duration: int
    workout_type: str

# Временное хранилище данных
workouts = []

@app.post("/workouts")
def create_workout(workout: Workout):
    workouts.append(workout)
    return {"message": "Workout created successfully"}

@app.get("/workouts/{id}")
def get_workout(id: int):
    for workout in workouts:
        if workout.id == id:
            return workout
    return {"error": "Workout not found"}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from repositories.json_repo import JSONRepository
from models import User

app = FastAPI()
user_repo = JSONRepository[User]("users.json")


class UserInput(BaseModel):
    user_id: int
    name: str
    age: int
    gender: str
    weight: float
    height: float


@app.post("/users/", response_model=UserInput)
def create_user(user: UserInput):
    user_repo.add(user)
    return user


@app.get("/users/", response_model=List[UserInput])
def get_users():
    return user_repo.get_all()


@app.get("/users/{user_id}", response_model=UserInput)
def get_user(user_id: int):
    user = user_repo.find_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user_repo.delete(user_id)
    return {"message": f"User with ID {user_id} has been deleted"}

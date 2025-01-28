import json
from typing import Generic, TypeVar, List
from repositories.base import BaseRepository

T = TypeVar('T')


class JSONRepository(BaseRepository[T]):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _load_data(self) -> List[T]:
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_data(self, data: List[T]) -> None:
        with open(self.file_path, 'w') as file:
            json.dump(data, file, default=lambda o: o.__dict__, indent=4)

    def add(self, obj: T) -> None:
        data = self._load_data()
        data.append(obj)
        self._save_data(data)

    def get_all(self) -> List[T]:
        return self._load_data()

    def find_by_id(self, obj_id: int) -> T:
        data = self._load_data()
        for item in data:
            if item['id'] == obj_id:
                return item
        return None

    def delete(self, obj_id: int) -> None:
        data = self._load_data()
        filtered_data = [item for item in data if item['id'] != obj_id]
        self._save_data(filtered_data)

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')

class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    def add(self, obj: T) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def find_by_id(self, obj_id: int) -> T:
        pass

    @abstractmethod
    def delete(self, obj_id: int) -> None:
        pass

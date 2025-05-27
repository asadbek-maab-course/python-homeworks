from abc import ABC, abstractmethod
from typing import List
from task import Task

class BaseStorage(ABC):
    @abstractmethod
    def load_tasks(self) -> List[Task]:
        pass

    @abstractmethod
    def save_tasks(self, tasks: List[Task]):
        pass

import json
from typing import List
from task import Task
from storage.base_storage import BaseStorage

class JSONStorage(BaseStorage):
    def __init__(self, filename: str):
        self.filename = filename

    def load_tasks(self) -> List[Task]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Task.from_dict(task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self, tasks: List[Task]):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

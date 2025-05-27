import csv
from typing import List
from task import Task
from storage.base_storage import BaseStorage

class CSVStorage(BaseStorage):
    def __init__(self, filename: str):
        self.filename = filename

    def load_tasks(self) -> List[Task]:
        tasks = []
        try:
            with open(self.filename, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    tasks.append(Task.from_dict(row))
        except FileNotFoundError:
            pass
        return tasks

    def save_tasks(self, tasks: List[Task]):
        with open(self.filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=Task.__annotations__.keys())
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

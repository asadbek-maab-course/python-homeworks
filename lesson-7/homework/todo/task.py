from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Task:
    task_id: str
    title: str
    description: str
    due_date: Optional[str]
    status: str

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data: dict):
        return Task(**data)

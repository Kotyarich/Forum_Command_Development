from datetime import datetime
from typing import List


class Task:
    def __init__(self, service: str, link: str, description: str,
                 labels: List[str], priority: str, deadline: datetime,
                 difficulty: str, repository: str,
                 number: int):
        self.service = service
        self.link = link
        self.description = description
        self.labels = labels
        self.priority = priority
        self.deadline = deadline
        self.difficulty = difficulty
        self.repository = repository
        self.number = number

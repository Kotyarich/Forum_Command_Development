from datetime import datetime


class Task:
    def __init__(self, service: str, link: str, description: str, label: str,
                 priority: str, deadline: datetime, difficulty: str):
        self.service = service
        self.link = link
        self.description = description
        self.label = label
        self.priority = priority
        self.deadline = deadline
        self.difficulty = difficulty

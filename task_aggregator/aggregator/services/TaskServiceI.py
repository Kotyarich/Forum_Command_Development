import abc
from typing import List

from aggregator.models import Token
from aggregator.services.Task import Task


class TaskServiceI(abc.ABC):

    def __init__(self, token: Token):
        self.token = token
        self.base_url = token.service.domain + '/'

    @abc.abstractmethod
    def get_tasks(self) -> List[Task]:
        """
        Returns list of assigned to user tasks.
        """
        pass

    @abc.abstractmethod
    def move_task(self, src: str, task_id: int, repository: str):
        pass

    @abc.abstractmethod
    def close_task(self, task_id: int, repository: str):
        pass

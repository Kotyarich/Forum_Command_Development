import abc
from typing import List

from task_aggregator.aggregator.models import *
from task_aggregator.aggregator.services.Task import Task


class TaskServiceI(abc.ABC):

    @abc.abstractmethod
    def get_tasks(self, token: Token) -> List[Task]:
        """
        Returns list of assigned to user tasks.
        :param token: user's token.
        :return:
        """
        pass

    @abc.abstractmethod
    def move_task(self, token: Token, task_id: int):
        pass

    @abc.abstractmethod
    def close_task(self, token: Token, task_id: int):
        pass

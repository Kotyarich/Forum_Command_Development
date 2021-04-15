from typing import List
import requests

from aggregator.models import Token
from .Task import Task
from .TaskServiceI import TaskServiceI


class GitHubService(TaskServiceI):

    def __init__(self, token: Token):
        super().__init__(token)

    def _call_api(self, method, url, body=None):
        github_token = self.token.token
        url = self.base_url + url

        headers = {'Accept': 'application/vnd.github.v3+json'}
        response = requests.request(method, url,
                                    auth=('username', github_token),
                                    headers=headers, json=body)

        return response.json(), response.status_code

    def convert_task(self, task) -> Task:
        labels = [label['name'] for label in task['labels']]

        deadline = None
        if 'milestone' in task:
            milestone = task['milestone']
            if milestone is not None and 'due_on' in milestone:
                deadline = milestone['due_on']

        task = Task('GitHub', task['url'], task['body'],
                    labels, None, deadline, None,
                    task['repository']['full_name'], task['number'])
        return task

    def get_tasks(self) -> List:
        res, status = self._call_api('get', 'issues')
        if status != 200:
            raise Exception(res['message'])

        issues = [self.convert_task(task) for task in res]
        return issues

    def move_task(self, task_id: int, dst: str, repository: str):
        url = 'repos/{}/issues/{}'.format(repository, task_id)

        res, status = self._call_api('get', url)
        if status != 200:
            raise Exception(res['message'])
        labels = [label['name'] for label in res['labels']]

        labels_map = self.token.map
        current = None
        for label in labels:
            if label in labels_map.todo or label in labels_map.doing \
                    or label in labels_map.review:
                current = label
                break

        if current is None:
            delete_url = 'repos/{}/issues/{}/labels/{}'.format(repository,
                                                               task_id,
                                                               current)
            res, status = self._call_api('delete', delete_url)
            if status != 200:
                raise Exception(res['message'])

        add_url = 'repos/{}/issues/{}/labels'.format(repository, task_id)
        res, status = self._call_api('post', add_url, {'labels': [dst]})
        if status != 200:
            raise Exception(res['message'])

    def close_task(self, task_id: int, repository: str):
        url = 'repos/{}/issues/{}'.format(repository, task_id)
        res, status = self._call_api('patch', url, {'state': 'closed'})
        if status != 200:
            raise Exception(res['message'])

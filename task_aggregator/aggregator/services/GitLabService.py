from typing import List
import requests

from aggregator.models import Token
from .Task import Task
from .TaskServiceI import TaskServiceI


class GitLabService(TaskServiceI):

    def __init__(self, token: Token):
        super().__init__(token)
        self.base_url += 'api/v4/'

    def _call_api(self, method, url, body=None):
        private_token = self.token.token
        url = self.base_url + url

        headers = {'PRIVATE-TOKEN': private_token}
        response = requests.request(method, url, headers=headers, json=body)

        return response.json(), response.status_code

    def _get_project_id(self, repository):
        url = 'projects/membership=True'
        res, status = self._call_api('get', url)
        if status != 200:
            raise Exception(res['message'])

        project = list(filter(lambda p: p['name'] == repository, res))[0]

        return project['id']

    def convert_task(self, task) -> Task:
        project_url = '/projects/{}'.format(task['project_id'])
        res, status = self._call_api('get', project_url)
        if status != 200:
            raise Exception(res['message'])

        task = Task('GitLab', task['web_url'], task['description'],
                    task['labels'], None, task['due_date'], None,
                    res['name'], task['iid'])
        return task

    def get_tasks(self) -> List:
        url = 'issues/scope=assigned_to_me&state=open'
        res, status = self._call_api('get', url)
        if status != 200:
            raise Exception(res['message'])

        issues = [self.convert_task(task) for task in res]
        return issues

    def move_task(self, task_id: int, dst: str, repository: str):
        project_id = self._get_project_id(repository)

        url = 'projects/{}/issues/{}'.format(project_id, task_id)
        res, status = self._call_api('get', url)
        if status != 200:
            raise Exception(res['message'])
        labels = res['labels']

        labels_map = self.token.map
        current = None
        for label in labels:
            if label in labels_map.todo or label in labels_map.doing \
                    or label in labels_map.review:
                current = label
                break

        if current is not None:
            labels.remove(current)

        labels.append(dst)
        labels_str = ','.join(labels)
        add_url = 'projects/{}/issues/{}?labels={}'.format(repository, task_id,
                                                           labels_str)
        res, status = self._call_api('put', add_url)
        if status != 200:
            raise Exception(res['message'])

    def close_task(self, task_id: int, repository: str):
        project_id = self._get_project_id(repository)
        url = 'projects/{}/issues/{}?state_event=close'.format(project_id,
                                                               task_id)
        res, status = self._call_api('put', url)
        if status != 200:
            raise Exception(res['message'])

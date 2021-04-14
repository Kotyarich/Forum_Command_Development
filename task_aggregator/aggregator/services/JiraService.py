from typing import List
import requests

from aggregator.models import Token
from .Task import Task
from .TaskServiceI import TaskServiceI


class JiraService(TaskServiceI):

    def __init__(self, token: Token):
        super().__init__(token)
        self.base_url += 'rest/api/2/'

    def _call_api(self, method, url, body=None, no_response=False):
        private_token = self.token.token
        url = self.base_url + url
        auth = (self.token.in_service_username, private_token)
        response = requests.request(method, url, auth=auth, json=body)

        if no_response:
            return response.status_code
        return response.json(), response.status_code

    def convert_task(self, task) -> Task:
        task = Task('Jira', task['self'],
                    task['description'] if 'description' in task else '',
                    task['labels'] + [task['status']['name']],
                    task['priority']['name'], task['due_date'],
                    None, task['project']['name'], task['id'])
        return task

    def get_tasks(self) -> List:
        url = 'search?jql=assignee=currentuser()'
        res, status = self._call_api('get', url)
        if status != 200:
            raise Exception(res['message'])
        print(res)

        issues = [self.convert_task(task) for task in res['issues']]
        return issues

    def get_transitions(self, id):
        res, st = self._call_api('get', 'issue/{}/transitions'.format(id))
        if st != 200:
            raise Exception(st)
        return res['transitions']

    def make_transition(self, task_id, transition_id):
        st = self._call_api('post',
                            'issue/{}/transitions'.format(task_id),
                            {'transition': {'id': transition_id}},
                            no_response=True)
        return st

    def move_task(self, task_id: int, dst: str, repository: str):
        transitions = self.get_transitions(task_id)
        transition = list(filter(lambda tr: tr['name'] == dst, transitions))[0]
        status = self.make_transition(task_id, transition['id'])
        if status != 204:
            raise Exception(status)

    def close_task(self, task_id: int, repository: str):
        url = 'issue/{}?deleteSubtasks=true'.format(task_id)
        status = self._call_api('delete', url, no_response=True)
        if status != 204:
            raise Exception(status)

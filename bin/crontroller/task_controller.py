from typing import Any

from crontroller._base_controller import BaseController
from service.task_service import TaskService


class TasksBaseController(BaseController):
    task_service = TaskService()


class TasksController(TasksBaseController):

    def get(self):
        return self.task_service.find_ability_task()

    def clean_get_response(self, res: Any):
        return self._resp(res)

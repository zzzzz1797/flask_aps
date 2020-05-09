from typing import Callable

from crontroller import job_controller, task_controller


def load_controller(app: Callable):
    app.api.add_resource(task_controller.TasksController, "/tasks")

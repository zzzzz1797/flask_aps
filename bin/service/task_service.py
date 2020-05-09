from typing import List, Dict

from service._base_service import BaseService
from service.tasks import load_tasks


class TaskService(BaseService):

    def find_ability_task(self) -> List[Dict[str, str]]:
        """
            获取可用的任务（也就是service/tasks里面的任务）
        """
        return load_tasks()

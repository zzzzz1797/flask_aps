from typing import List, Dict

from flask import current_app

from service._base_service import BaseService


class JobService(BaseService):

    def find_all_jobs(self) -> List[Dict[str, str]]:
        """
            获取可用的任务（也就是service/tasks里面的任务）
        """
        return current_app.apscheduler.get_jobs()

    def add_jobs(self, params: Dict):
        return current_app.apscheduler.add_job(**params)

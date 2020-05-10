from typing import Any

from crontroller._base_controller import BaseController
from service.job_service import JobService


class JobBaseController(BaseController):
    job_service = JobService()


class JobsController(JobBaseController):

    def get(self):
        return self.job_service.find_all_jobs()

    def clean_get_response(self, res: Any):
        return self._resp(res)

    def post(self):
        return self.job_service.add_jobs()

    def post_validate(self):
        pass

    def get_validate(self):
        pass

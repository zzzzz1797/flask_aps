from typing import List

from crontroller.validates._base_validate import BaseReqParser


class JobAddValidate(BaseReqParser):
    """
    func, trigger=None, args=None, kwargs=None, id=None, name=None,
                misfire_grace_time=undefined, coalesce=undefined, max_instances=undefined,
                next_run_time=undefined, jobstore='default', executor='default',
                replace_existing=False

    """

    def need_check_fields(self) -> List[str]:
        return ["func", "trigger", "args", "kwargs", "id", "name"]

    def __validate_func(self):
        self.parser.add_argument("func", type="str", help="任务名称格式无效", required=True)

import logging
import traceback
from typing import Any, Callable

from flask import request, jsonify
from flask_restful import Resource

log = logging.getLogger()
from util.exception import RequestParamsValidateException


class BaseController(Resource):

    def __init__(self):
        self.request_params = {}
        self.method = request.method.lower()
        self._check_handler = None
        self._clean_handler = None

    def dispatch_request(self, *args, **kwargs):
        # 0. 系统内部的预检
        self.server_pre_check()
        # 1. 请求参数的校验
        self.request_params_check()
        # 2. 业务逻辑处理
        res = super().dispatch_request(*args, **kwargs)
        # 3. 格式化响应参数
        return self.response_clean(res)

    def server_pre_check(self):
        self._check_handler = getattr(self, f"{self.method}_request_check", "")
        self._clean_handler = getattr(self, f"{self.method}_response_clean", "") or (lambda i: i)

        if self._check_handler:
            if not isinstance(self._check_handler, Callable):
                return self._resp(flag=False, msg="参数校验方法加载失败")
        if not isinstance(self._clean_handler, Callable):
            return self._resp(flag=False, msg="系统异常")

    def request_params_check(self) -> None:

        try:
            self.request_params = self._check_handler()
        except RequestParamsValidateException as e:
            return self._resp(flag=False, msg=e.message)
        except Exception as e:
            log.error(traceback.format_exc())
            return self._resp(flag=False, msg="未知错误")

    def response_clean(self, res: Any) -> Any:
        return self._resp(res=self._clean_handler(res))

    @staticmethod
    def _resp(res: Any = None, flag: bool = True, msg: str = ""):
        return jsonify({"data": res, "code": flag, "msg": msg})

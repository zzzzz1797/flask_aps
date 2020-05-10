import logging
import traceback
from types import MethodType
from typing import List, Dict

from flask_restful.reqparse import RequestParser

from util.exception import ComposeValidateCodeException, RequestParamsValidateException

log = logging.getLogger()


class BaseReqParser:
    def __init__(self):
        self.parser = RequestParser()

    def __call__(self) -> Dict:
        try:
            for field_name in self.need_check_fields():
                # 获取这个field的校验方法
                validate_func = getattr(self, f"_validate_{field_name}", "")
                assert isinstance(validate_func, MethodType)
                validate_func()
            request_data = self.parser.parse_args()
        except ValueError as e:
            raise RequestParamsValidateException(e.message)
        except Exception:
            log.warning(traceback.format_exc())
            raise ComposeValidateCodeException("系统内部异常")
        return request_data

    def need_check_fields(self) -> List[str]:
        raise NotImplementedError

from flask import request, jsonify
from flask_restful import Resource, reqparse


class BaseController(Resource):
    _checker = None

    def __init__(self):
        self.request_params = {}

    def dispatch_request(self, *args, **kwargs):
        method = request.method.lower()
        validate_instance = getattr(self, f"find_{method}_validate", "")
        clean_response = getattr(self, f"clean_{method}_response", "") or (lambda i: i)

        assert clean_response

        if validate_instance:
            if callable(validate_instance):
                self.request_params = validate_instance()
            else:
                assert "Validate Format Error"

        # 2. 业务逻辑处理
        res = super().dispatch_request(*args, **kwargs)

        # 3. 格式化响应参数
        return clean_response(res)

    def _resp(self, res):
        return jsonify({"data": res})


class BaseReqParser(reqparse.RequestParser):
    pass

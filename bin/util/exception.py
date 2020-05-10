class MyException(BaseException):
    def __init__(self, message: str):
        self.message = message


class RequestParamsValidateException(MyException):
    pass


class ComposeCodeException(MyException):
    pass


class InnerServiceException(MyException):
    pass

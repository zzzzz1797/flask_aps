import logging
import time
from typing import Any

from flask import request, Response

log = logging.getLogger()


def init_hook(app: Any):
    @app.before_request
    def before_request():
        request.start_time = time.time()

    @app.after_request
    def after_request(response: Response):
        log_record = [
            request.remote_addr,
            request.url,
            request.user_agent,
            (time.time() - request.start_time) * 1000,  # 精确到毫秒
            response.status_code,
            response.mimetype,
            response.content_length,
        ]
        log_record_detail = "|".join(map(str, log_record))
        log.debug(f"{log_record_detail}")
        return response

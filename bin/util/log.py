import logging
from logging.handlers import TimedRotatingFileHandler

import config

DEFAULT_FORMAT = "%(asctime)s %(process)d,%(threadName)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s"
DEFAULT_HANDLER = logging.StreamHandler


def init_log():
    """
        从config.py 加载日志配置，现在只支持控制台或者文件（文件按天切分）
    """
    for log_name, log_cnf in config.LOGFILE.items():
        logger = logging.getLogger(log_name)
        formatter = log_cnf.get("formatter", DEFAULT_FORMAT)
        logger.setLevel(logging.DEBUG)
        for level, path in log_cnf["filename"].items():
            if path == "stdout":
                handler = logging.StreamHandler()
            else:
                handler = TimedRotatingFileHandler(path, when="midnight")
            handler.setFormatter(logging.Formatter(formatter))
            handler.setLevel(getattr(logging, level))
            logger.addHandler(handler)

from types import FunctionType

from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from flask import Flask
from flask_apscheduler import APScheduler
from flask_restful import Api

import config
from crontroller import load_controller
from util import log, hook

app = Flask(__name__)


def init():
    for prop_name, prop in globals().items():
        if isinstance(prop, FunctionType) and prop_name.startswith("init_"): prop()


def init_api():
    api = Api(app)
    app.api = api


def init_controller():
    load_controller(app)


def init_log():
    log.init_log()


def init_scheduler():
    app.config.update({
        "SCHEDULER_JOBSTORES": {
            "default": SQLAlchemyJobStore(config.DB_URL),
        },
        "executors": {
            "default": AsyncIOExecutor,
        }
    })
    scheduler = APScheduler(AsyncIOScheduler())
    scheduler.init_app(app)
    scheduler.start()


def init_hook():
    hook.init_hook(app)


init()

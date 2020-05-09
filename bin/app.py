from types import FunctionType

from flask import Flask
from flask_restful import Api

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


def init_hook():
    hook.init_hook(app)


init()

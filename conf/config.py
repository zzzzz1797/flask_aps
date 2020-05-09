from pathlib import Path

HOME = Path(__file__).parent.parent

PRO_NAME = "flask_aps"

PORT = 3306

HOST = "0.0.0.0"

LOGFILE = {
    None: {
        "filename": {
            "DEBUG": HOME / "log" / "root.debug.log",
            "ERROR": HOME / "log" / "root.debug.log",
        },
    },
    "apscheduler": {
        "filename": {
            "DEBUG": HOME / "log" / "apscheduler.debug.log",
            "ERROR": HOME / "log" / "apscheduler.debug.log",
        },
    },
}

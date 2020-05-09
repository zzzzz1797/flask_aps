from functools import lru_cache
from pathlib import Path
from types import FunctionType

from util.load import load_module_with_absolute_path


@lru_cache
def load_tasks():
    path = Path(__file__).parent

    res = []
    for p in path.glob("*task.py"):
        module = load_module_with_absolute_path(str(p))
        for prop_name in dir(module):
            prop = getattr(module, prop_name, "")
            if isinstance(prop, FunctionType) and prop_name.endswith("_task"):
                task_description = getattr(prop, "description", "")
                res.append({
                    "task_description": task_description,
                    "task_module": f"{p.name.split('.py')[0]}.{prop_name}",
                })
    return res


if __name__ == '__main__':
    load_tasks()
    print(TASKS)

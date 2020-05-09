import importlib
from importlib import util
from pathlib import Path
from typing import Callable


def load_module_with_absolute_path(file_path: str) -> Callable:
    """
        根据模块的绝对路径加载模块
    """
    assert Path(file_path).exists()
    file_path_object = Path(file_path)
    module_spec = util.spec_from_file_location(file_path_object.name, file_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module

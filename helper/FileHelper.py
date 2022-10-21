import os
from io import TextIOWrapper

selfPyName = os.path.basename(__file__)


class TextFile(TextIOWrapper):
    pass


def create_dir_of_path(path: str):
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def open_file(path: str, mode='a+'):
    create_dir_of_path(path)
    f = open(file=path, mode=mode, encoding="utf8")
    return f

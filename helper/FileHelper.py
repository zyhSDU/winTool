import os
from io import TextIOWrapper
from logging import Logger

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


def re_name_of_files(
        now_file,
        old_str,
        new_str,
        max_deep,
        now_deep,
        log: Logger,
):
    if now_deep > max_deep:
        return
    if os.path.isdir(now_file):
        for f in os.listdir(now_file):
            re_name_of_files(
                f"{now_file}{os.sep}{f}",
                old_str,
                new_str,
                max_deep,
                now_deep + 1,
                log,
            )
    new_file = f"{os.path.dirname(now_file)}{os.sep}{os.path.basename(now_file).replace(old_str, new_str)}"
    os.rename(now_file, new_file)
    log.info(f"{now_file}\t{new_file}")

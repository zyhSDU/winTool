from typing import List, Callable

from helper.ChineseEnglishHelper import change_chinese_punctuation_to_english


def change_ascii_to_blank(string: str) -> str:
    string = string.replace(chr(2), " ")
    return string.strip()


def split_to_per_line_one_cite(string: str, ) -> str:
    string = change_ascii_to_blank(string)
    re_list = []
    ss = string.split("\n")
    i_begin = 1
    for s in ss:
        if s.startswith(f"{i_begin} ") or s.startswith(f"[{i_begin}] "):
            re_list.append("\n")
            i_begin += 1
        re_list.append(s)
        re_list.append(" ")
    return "".join(re_list).strip()


def split_by_sep(string: str, ) -> str:
    string = change_chinese_punctuation_to_english(string)
    re_list = []
    ss = []
    seps = [";", ","]
    for i in seps:
        if string.__contains__(i):
            ss = string.split(i)
            break
    for s in ss:
        re_list.append(s.strip())
        re_list.append("\n")
    return "".join(re_list).strip()


def emerge_blank(string: str) -> str:
    string = string.strip()
    for i in range(2, 8).__reversed__():
        string.replace(" " * i, " ")
    return string.strip()


def emerge_lines(string: str) -> str:
    string = string.replace("\n", " ").strip()
    string = emerge_blank(string)
    # 处理来自pdf的麻烦
    string = string.replace("- ", "")
    string = string.replace("Fig. ", "Fig.")
    return string.strip()


def emerge_lines_and_split_by_dot(string: str) -> str:
    string = emerge_lines(string)
    seps = [".", "。", "！", "!"]
    for i in seps:
        string = string.replace(i, f"{i}\n")
    re_list = []
    ss = string.split("\n")
    # 去除换行前后的空格
    for s in ss:
        re_list.append(s.strip())
        re_list.append("\n")
    string = "".join(re_list)
    # 处理来自pdf的麻烦
    string = string.replace("Fig.\n", "Fig.")
    return string.strip()


def test_b1(
        read_file_name: str,
        write_file_name: str,
        fun: Callable[[str], List[str]],
):
    re1 = open(read_file_name, mode="r", encoding="utf8").read()
    re_list = fun(re1)
    re2 = open(write_file_name, mode="w", encoding="utf8")
    re_str = "".join(re_list).strip()
    re2.write(re_str)

from typing import List, Callable


def split_to_per_line_one_cite(string: str, ) -> List[str]:
    re_list = []
    ss = string.strip().split("\n")
    i_begin = 1
    for s in ss:
        if s.startswith(f"{i_begin} ") or s.startswith(f"[{i_begin}] "):
            re_list.append("\n")
            i_begin += 1
        re_list.append(s)
        re_list.append(" ")
    return re_list


def split_by_sep(string: str, ):
    re_list = []
    ss = string.strip().replace("；", ";").split(";")
    for s in ss:
        re_list.append(s.strip())
        re_list.append("\n")
    return re_list


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

from typing import List, Union

from helper.FileHelper import TextFile
from helper.ObjectHelper import Object
from helper.coder.Replacer import bs
from helper.LoggingHelper import get_logger1

log = get_logger1()


class StrLine(object):
    def __init__(
            self,
            _n: bool = False,
            _t: bool = False,
            string: str = "",
    ):
        self._n: bool = _n
        self._t: bool = _t
        self.string: str = string


class CodeBlock(Object):
    def __init__(
            self,
            content: str,
            *replace_list,
    ):
        self.content: str = content
        self.replace_list: List[Union[str, CodeBlock]] = []
        for i in replace_list:
            self.replace_list.append(i)

    def add_block(self, b):
        self.replace_list.append(b)

    def add_line_block(self):
        self.add_block("\n")

    def get_str(
            self,
            tab_num: int = 0,
            if_l_strip: bool = True,
    ) -> str:
        now_tab_str = "\t" * tab_num
        res = self.content
        res = res.replace(f"\n", f"\n{now_tab_str}")
        if_begin_not_contains = False
        for i, v in enumerate(self.replace_list):
            if if_begin_not_contains:
                if_contain_i = False
            else:
                if_contain_i = self.if_contain_i(i)
                if not if_contain_i:
                    if_begin_not_contains = True
            v_str = ""
            if isinstance(v, str):
                v_str = v.replace(f"\n", f"\n{now_tab_str}")
            elif isinstance(v, CodeBlock):
                v_str = v.get_str(
                    tab_num=tab_num + if_contain_i,
                    if_l_strip=False,
                )
            if if_contain_i:
                res = res.replace(bs[i], v_str)
            else:
                res += v_str
        if if_l_strip:
            res = res.lstrip("\n")
        return res

    def print_code(
            self,
            text_file: TextFile = None,
            if_l_strip: bool = True,
    ):
        print(
            f"{self.get_str(if_l_strip=if_l_strip, )}",
            end="",
            file=text_file,
        )

    def if_contain_i(self, index: int):
        return self.content.__contains__(f"{bs[index]}")


def get_empty_block(
        *replace_list,
):
    return CodeBlock(
        "",
        *replace_list,
    )

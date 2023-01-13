from typing import List, Union

from helper.coder.Replacer import bs
from helper.FileHelper import TextFile
from helper.ObjectHelper import Object


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
    ) -> str:
        now_tab_str = "\t" * tab_num
        if self.content == "":
            res = ""
            for i, v in enumerate(self.replace_list):
                res += f"{bs[i]}"
        else:
            res = self.content
        res = res.replace(f"\n", f"\n{now_tab_str}")
        for i, v in enumerate(self.replace_list):
            if_contain_i = self.if_contain_i(i)
            fb = bs[i]
            v_str = ""
            if isinstance(v, str):
                v_str += v.replace(f"\n", f"\n{now_tab_str}")
            elif isinstance(v, CodeBlock):
                v_str += v.get_str(tab_num + if_contain_i)
            if res.__contains__(fb):
                res = res.replace(fb, f"{v_str}")
        return res

    def print_code(
            self,
            text_file: TextFile = None,
    ):
        print(f"{self.get_str()}", end="", file=text_file, )

    def if_contain_i(self, index: int):
        return int(self.content.__contains__(f"\t{bs[index]}"))


def get_empty_block(
        *replace_list,
):
    return CodeBlock(
        "",
        *replace_list,
    )

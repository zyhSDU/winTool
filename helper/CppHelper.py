from typing import List, Callable

from helper.CallableHelper import call_none


class StrListListUnit(object):
    def __init__(
            self,
            str_list_list: List[List[str]] = None,
    ):
        if str_list_list is None:
            str_list_list = []
        self.str_list_list = str_list_list

    def append(
            self,
            *vs: str,
    ):
        vs2 = []
        for v in vs:
            vs2.append(v)
        self.str_list_list.append(vs2)

    def trace(
            self,
            c: Callable[[List[str]], None] = call_none,
    ):
        for vs in self.str_list_list:
            c(vs)

    def extend(self, s):
        # print("extend")
        assert isinstance(s, StrListListUnit)
        for vs in s.str_list_list:
            # print(vs)
            vs2 = []
            for v in vs:
                vs2.append(v)
            self.str_list_list.append(vs2)


def get_str_list_list_unit_1(
        *str_list: str,
) -> StrListListUnit:
    vss = []
    for v in str_list:
        vss.append([v])
    return StrListListUnit(vss)

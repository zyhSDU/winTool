from typing import List, Union

from helper.FileHelper import TextFile
from helper.ObjectHelper import Object

str_b = "b"


def get_b(i_int: int):
    return f"__{str_b}{i_int}__"


def python_b_list_block_print():
    bs_size = 16
    for i in range(bs_size):
        print(f"b{i} = get_b({i})")
    bs_str = "bs = ["
    for i in range(bs_size):
        bs_str += f"b{i}, "
    bs_str += "]"
    print(bs_str)


# python_b_list_block_print()

b0 = get_b(0)
b1 = get_b(1)
b2 = get_b(2)
b3 = get_b(3)
b4 = get_b(4)
b5 = get_b(5)
b6 = get_b(6)
b7 = get_b(7)
b8 = get_b(8)
b9 = get_b(9)
b10 = get_b(10)
b11 = get_b(11)
b12 = get_b(12)
b13 = get_b(13)
b14 = get_b(14)
b15 = get_b(15)
bs = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, ]


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
            content: str = "",
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
        print(f"{self.get_str()}", file=text_file)

    def if_contain_i(self, index: int):
        return int(self.content.__contains__(f"\t{bs[index]}"))


def get_c_include_block(
        lib_name: str,
):
    return CodeBlock(
        f"\n#include {b0}",
        lib_name,
    )


def get_c_arg_block(
        arg_type: str,
        arg_name: str,
):
    return CodeBlock(
        f"{b0} {b1}",
        arg_type,
        arg_name,
    )


def get_c_args_block(
        *replace_list,
):
    return CodeBlock(
        ", ".join(bs[:len(replace_list)]),
        *replace_list,
    )


def get_c_arg_declare_block(
        arg_type: str,
        arg_name: str,
):
    return CodeBlock(
        f"\n{b0} {b1};",
        arg_type,
        arg_name,
    )


def get_c_define_block(
        arg_k: str,
        arg_v: str,
):
    return CodeBlock(
        f"\n#define {b0} {b1}",
        arg_k,
        arg_v,
    )


def get_c_method_block(
        return_type: str,
        method_name: str,
        args_block: CodeBlock,
        content_block: CodeBlock,
):
    return CodeBlock(
        f"\n{b0} {b1}({b2}){{"
        f"\t{b3}"
        f"\n}}",
        return_type,
        method_name,
        args_block,
        CodeBlock("", content_block),
    )


def get_c_for_block_1(
        block0: CodeBlock,
        block1: CodeBlock,
        block2: CodeBlock,
        block3: CodeBlock,
):
    return CodeBlock(
        f"\nfor({b0}; {b1}; {b2}){{"
        f"\t{b3}"
        f"\n}}",
        block0,
        block1,
        block2,
        CodeBlock("", block3),
    )


def test1():
    c_includes_block = CodeBlock()
    for i in range(3):
        c_includes_block.add_block(get_c_include_block(f"a{i}.h"))
    c_includes_block.add_line_block()
    return c_includes_block


def test2():
    c_b = CodeBlock()
    c_b.add_block(get_c_arg_declare_block("XTime", "tEnd"))
    c_b.add_block(get_c_arg_declare_block("XTime", "tCur"))
    c_b.add_block(get_c_arg_declare_block("u32", "tUsed"))
    c_b.add_line_block()
    return c_b


def test3():
    c_b = CodeBlock()
    c_b.add_block(get_c_define_block("input", "0"))
    c_b.add_block(get_c_define_block("output", "1"))
    c_b.add_line_block()
    return c_b


def test4():
    c_b = CodeBlock()
    c_method_block = get_c_method_block(
        "void",
        "delay",
        get_c_args_block(
            get_c_arg_block("uint16_t", "time"),
        ),
        CodeBlock(
            "",
            get_c_arg_declare_block("uint16_t", "i"),
            get_c_arg_declare_block("uint16_t", "j"),
            get_c_for_block_1(
                CodeBlock("i = 0"),
                CodeBlock("i < time"),
                CodeBlock("i++"),
                get_c_for_block_1(
                    CodeBlock("j = 0"),
                    CodeBlock("i < 100"),
                    CodeBlock("j++"),
                    CodeBlock("", "\n1"),
                ),
            ),
            get_c_arg_declare_block("uint16_t", "time2"),
        ),
    )
    c_b.add_block(c_method_block)
    c_b.add_line_block()
    return c_b


def tests1():
    c_b = CodeBlock()
    c_b.add_block(test1())
    c_b.add_block(test2())
    c_b.add_block(test3())
    c_b.add_block(test4())
    c_b.print_code()


if __name__ == '__main__':
    tests1()

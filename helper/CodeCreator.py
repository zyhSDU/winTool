from typing import List, Union

from helper.FileHelper import TextFile

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


class CodeBlock(object):
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
    ) -> str:
        res = self.content
        ss = []
        for v in self.replace_list:
            if isinstance(v, CodeBlock):
                inner_s = v.get_str()
            elif isinstance(v, str):
                inner_s = v
            else:
                inner_s = ""
            ss.append(inner_s)
        for i, v in enumerate(ss):
            fb = bs[i]
            if res.__contains__(fb):
                res = res.replace(fb, v)
            else:
                res += v
        return res

    def print_code(
            self,
            text_file: TextFile = None,
    ):
        print(f"{self.get_str()}", file=text_file)


def get_c_include_block(
        *replace_list,
):
    return CodeBlock(
        f"#include {b0}\n",
        *replace_list,
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


def get_c_declare_block(
        *replace_list,
):
    return CodeBlock(
        f"{b0} {b1};\n",
        *replace_list,
    )


def get_c_define_block(
        *replace_list,
):
    return CodeBlock(
        f"#define {b0} {b1}\n",
        *replace_list,
    )


def get_c_method_block(
        return_type: str,
        method_name: str,
        args_block: CodeBlock,
        content_block: CodeBlock,
):
    return CodeBlock(
        f"{b0} {b1}({b2}){{\n"
        f"{b3}"
        f"}}",
        return_type,
        method_name,
        args_block,
        content_block,
    )


def test1():
    c_includes_block = CodeBlock()
    for i in range(3):
        c_includes_block.add_block(get_c_include_block(f"a{i}.h"))
    c_includes_block.add_line_block()
    return c_includes_block


def test2():
    c_b = CodeBlock()
    c_b.add_block(get_c_declare_block("XTime", "tEnd"))
    c_b.add_block(get_c_declare_block("XTime", "tCur"))
    c_b.add_block(get_c_declare_block("u32", "tUsed"))
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
        get_c_args_block(get_c_arg_block("uint16_t", "time")),
        CodeBlock(""),
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

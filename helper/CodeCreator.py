from typing import List, Union, Set

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


class CodeTemplate(object):
    def __init__(
            self,
            content: str,
            *add_tab_block_index: int,
    ):
        self.content: str = content
        self.add_tab_block_index_set: Set[int] = set()
        self.add_index(*add_tab_block_index)

    def add_index(
            self,
            *add_tab_block_index: int,
    ):
        for i in add_tab_block_index:
            self.add_tab_block_index_set.add(i)

    def if_contain_i(self, index: int):
        return int(self.add_tab_block_index_set.__contains__(index))


class CodeBlock(object):
    def __init__(
            self,
            content: str = "",
            *replace_list,
    ):
        self.code_template: CodeTemplate = CodeTemplate(content)
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
            if_father_block_add_tab: int = 0,
    ) -> str:
        res = self.code_template.content
        for i, v in enumerate(self.replace_list):
            fb = bs[i]
            if_contain_i = self.if_contain_i(i)
            new_tab_num = tab_num + if_contain_i
            tab_str = "\t" * (new_tab_num * if_father_block_add_tab)
            v_str = ""
            if isinstance(v, str):
                v_str = v
            elif isinstance(v, CodeBlock):
                v_str = v.get_str(new_tab_num, if_contain_i)
            v_tab_str = f"{tab_str}{v_str}"
            if res.__contains__(fb):
                res = res.replace(fb, v_tab_str)
            else:
                res += v_tab_str
        return res

    def print_code(
            self,
            text_file: TextFile = None,
    ):
        print(f"{self.get_str()}", file=text_file)

    def add_index(
            self,
            *add_tab_block_index: int,
    ):
        self.code_template.add_index(*add_tab_block_index)

    def if_contain_i(self, index: int):
        return self.code_template.if_contain_i(index)


def get_c_include_block(
        lib_name: str,
):
    return CodeBlock(
        f"#include {b0}\n",
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
        f"{b0} {b1};\n",
        arg_type,
        arg_name,
    )


def get_c_define_block(
        arg_k: str,
        arg_v: str,
):
    return CodeBlock(
        f"#define {b0} {b1}\n",
        arg_k,
        arg_v,
    )


def get_c_method_block(
        return_type: str,
        method_name: str,
        args_block: CodeBlock,
        content_block: CodeBlock,
):
    cb = CodeBlock(
        f"{b0} {b1}({b2}){{\n"
        f"{b3}"
        f"}}",
        return_type,
        method_name,
        args_block,
        content_block,
    )
    cb.add_index(3)
    return cb


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
        get_c_args_block(get_c_arg_block("uint16_t", "time")),
        CodeBlock(
            "",
            get_c_arg_declare_block("uint16_t", "i"),
            get_c_arg_declare_block("uint16_t", "j"),
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

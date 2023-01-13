from typing import Union

from helper.coder.CodeCreator import CodeBlock, get_empty_block
from helper.coder.Coder import get_args_block, get_assign_block, get_bool_le_block
from helper.coder.Replacer import b0, b1, b2, b3


def get_c_include_block(
        lib_name: str,
):
    return CodeBlock(
        f"\n#include {b0}",
        lib_name,
    )


def get_c_arg_block(
        arg_type: str,
        arg_name: Union[str, CodeBlock],
):
    return CodeBlock(
        f"{b0} {b1}",
        arg_type,
        arg_name,
    )


def get_c_arg_declare_block(
        arg_type: str,
        arg_name: Union[str, CodeBlock],
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
        args_block: Union[str, CodeBlock],
        *replace_list,
):
    return CodeBlock(
        f"\n{b0} {b1}({b2}){{"
        f"\t{b3}"
        f"\n}}",
        return_type,
        method_name,
        args_block,
        CodeBlock("", *replace_list),
    )


def get_c_return_block(
        arg: Union[str, CodeBlock],
):
    return CodeBlock(
        f"\nreturn {b0};",
        arg,
    )


def get_c_arg_add_add_block(
        arg: str,
):
    return CodeBlock(
        f"{b0}++",
        arg,
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


def get_c_for_block_1_1(
        arg_i: str,
        i_min: Union[str, int],
        i_max: Union[str, int],
        block3: CodeBlock,
):
    return get_c_for_block_1(
        get_assign_block(arg_i, f"{i_min}"),
        get_bool_le_block(arg_i, f"{i_max}"),
        get_c_arg_add_add_block(arg_i),
        block3,
    )


def c_test1():
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
        arg_type_int = "uint16_t"
        arg_time = "time"
        arg_i = "i"
        arg_j = "j"
        c_b = CodeBlock()
        c_method_block = get_c_method_block(
            "void",
            "delay",
            get_args_block(
                get_c_arg_block(arg_type_int, arg_time),
            ),
            get_empty_block(
                get_c_arg_declare_block(arg_type_int, get_args_block(arg_i, arg_j)),
                get_c_for_block_1_1(
                    arg_i,
                    0,
                    arg_time,
                    get_c_for_block_1_1(
                        arg_j,
                        0,
                        100,
                        get_empty_block(),
                    ),
                ),
            ),
        )
        c_b.add_block(c_method_block)
        c_b.add_line_block()
        return c_b

    def test5():
        arg_type_int = "unsigned int"
        method_name = "systemMs"
        arg_type_void = "void"
        cb = get_c_method_block(
            arg_type_int,
            method_name,
            arg_type_void,
            "\nXTime_GetTime(&tEnd);",
            get_c_return_block("((tEnd) * 1000) / (COUNTS_PER_SECOND)"),
        )
        return cb

    cb = CodeBlock()
    cb.add_block(test1())
    cb.add_block(test2())
    cb.add_block(test3())
    cb.add_block(test4())
    cb.add_block(test5())
    cb.print_code()


if __name__ == '__main__':
    c_test1()

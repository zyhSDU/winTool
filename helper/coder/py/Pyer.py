from typing import Union

from helper.coder.Coder import get_a_block, get_assign_line_block, get_args_block
from helper.coder.CodeCreator import CodeBlock, get_empty_block
from helper.coder.Replacer import b0


def get_py_arr_block(
        v: Union[str, CodeBlock],
):
    return CodeBlock(
        f"[{b0}]",
        v
    )


def fun1_print_b_list_block(
        bs_size: int = 16,
):
    def get_assign_b_block(index: int):
        return get_assign_line_block(
            f"b{index}",
            f"get_b({index})"
        )

    for i in range(bs_size):
        get_assign_b_block(i).print_code(if_l_strip=False, )

    bs_str = []
    for i in range(bs_size):
        bs_str.append(f"b{i}")

    args_block = get_args_block(*bs_str)
    get_assign_line_block(
        f"bs",
        get_py_arr_block(args_block),
    ).print_code(if_l_strip=False, )

    get_a_block().print_code()
    get_a_block(get_empty_block(
        "# from helper.coder.Replacer import bs, ",
        args_block,
    )).print_code(if_l_strip=False, )


if __name__ == '__main__':
    fun1_print_b_list_block()

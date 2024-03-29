from typing import Union

from helper.coder.CodeCreator import CodeBlock, get_empty_block
from helper.coder.Coder import get_a_block, get_assign_block, get_bool_le_block
from helper.coder.Replacer import b0, b1, b2, b3


def get_c_include_block(
        lib_name: str,
        remark: Union[str, CodeBlock] = "",
):
    return get_a_block(
        CodeBlock(
            f"#include {b0}",
            lib_name,
        ),
        remark,
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
        remark: Union[str, CodeBlock] = "",
):
    return get_a_block(
        CodeBlock(
            f"{b0} {b1};",
            arg_type,
            arg_name,
        ),
        remark,
    )


def get_c_define_block(
        arg_k: str,
        arg_v: str,
        remark: Union[str, CodeBlock] = "",
):
    return get_a_block(
        CodeBlock(
            f"#define {b0} {b1}",
            arg_k,
            arg_v,
        ),
        remark,
    )


def get_c_arg_add_add_block(
        arg: str,
):
    return CodeBlock(
        f"{b0}++",
        arg,
    )


def get_c_return_block(
        arg: Union[str, CodeBlock],
        remark: Union[str, CodeBlock] = "",
):
    return get_a_block(
        CodeBlock(
            f"return {b0};",
            arg,
        ),
        remark,
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
        get_empty_block(*replace_list),
    )


def get_c_main_method_block(
        *replace_list,
):
    return get_c_method_block(
        "int",
        "main",
        get_empty_block(),
        *replace_list,
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
        get_empty_block(block3),
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

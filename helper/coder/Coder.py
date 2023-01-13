from typing import Union

from helper.coder.CodeCreator import CodeBlock
from helper.coder.Replacer import bs, b0, b1, b2


def get_line_block(
        v: Union[str, CodeBlock] = "",
        remark: Union[str, CodeBlock] = "",
):
    if remark == "":
        return CodeBlock(
            f"\n{b0}",
            v,
        )
    else:
        return CodeBlock(
            f"\n{b0} //{b1}",
            v,
            remark,
        )


def get_args_block(
        *replace_list,
):
    return CodeBlock(
        ", ".join(bs[:len(replace_list)]),
        *replace_list,
    )


def get_assign_block(
        k: Union[str, CodeBlock],
        v: Union[str, CodeBlock],
):
    return CodeBlock(
        f"{b0} = {b1}",
        k,
        v,
    )


def get_assign_line_block(
        k: Union[str, CodeBlock],
        v: Union[str, CodeBlock],
):
    return get_line_block(get_assign_block(k, v))


def get_bool_block(
        k: Union[str, CodeBlock],
        e: Union[str, CodeBlock],
        v: Union[str, CodeBlock],
):
    return CodeBlock(
        f"{b0} {b1} {b2}",
        k,
        e,
        v,
    )


def get_bool_le_block(
        k: Union[str, CodeBlock],
        v: Union[str, CodeBlock],
):
    return CodeBlock(
        f"{b0} < {b1}",
        k,
        v,
    )

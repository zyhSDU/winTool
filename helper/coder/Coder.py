from typing import Union

from helper.coder.CodeCreator import CodeBlock, get_empty_block
from helper.coder.Language import Language, language_none
from helper.coder.Replacer import bs, b0, b1, b2



def get_a_block(
        v: Union[str, CodeBlock] = "",
        remark: Union[str, CodeBlock] = "",
        if_line=True,
):
    content = ""
    if if_line:
        content += "\n"
    content += b0
    if remark != "":
        content += f"{b1}"
    return CodeBlock(
        content,
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
    return get_a_block(get_assign_block(k, v))


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

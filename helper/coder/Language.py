from helper.coder.CodeCreator import CodeBlock, get_empty_block
from helper.coder.Replacer import b0


class Language(object):
    def __init__(
            self,
            name: str = "",
            remark_prefix: str = "",
    ):
        self.name: str = name
        self.remark_prefix: str = remark_prefix

    def get_remark_block(
            self,
            *replace_list,
    ):
        list_len = len(replace_list)
        if list_len == 0:
            return ""
        if list_len == 1 and replace_list[0] == "":
            return ""
        cb = get_empty_block()
        for i in replace_list:
            cb.add_block(CodeBlock(
                f"{self.remark_prefix}{b0}",
                i,
            ))
        return cb

    def get_empty_remark_block(
            self,
    ):
        return self.get_remark_block(self, " ", )


language_none = Language()
language_c = Language("c", "// ", )
language_cpp = Language("cpp", "// ", )
language_py = Language("py", "# ", )

languages = [
    language_none,
    language_c,
    language_cpp,
    language_py,
]

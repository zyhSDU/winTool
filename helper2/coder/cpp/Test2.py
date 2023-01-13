from helper.coder.CodeCreator import CodeBlock, get_empty_block
from helper.coder.Coder import get_args_block
from helper.coder.c.Cer import get_c_include_block, get_c_arg_declare_block, get_c_define_block, \
    get_c_method_block, get_c_arg_block, get_c_for_block_1_1, get_c_return_block


def test():
    cb = get_empty_block()
    includes_block = get_empty_block()
    includes = [
        "<stdio.h>",
        '"platform.h"',
        '"xgpiops.h"',
        '"xgpiops_hw.h"',
        '"sleep.h"',
    ]
    for i in includes:
        includes_block.add_block(get_c_include_block(i))
    cb.add_block(includes_block)


    cb.print_code()


if __name__ == '__main__':
    test()

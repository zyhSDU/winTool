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

    defines_in = [
        ["EMIOKEY1", "54", "PL_KEY1"],
        ["EMIOKEY2", "55", "PL_KEY2"],
    ]
    defines_out = [
        ["EMIO1PUL", "56", "1"],
        ["EMIO2", "57", "2"],
        ["EMIO3", "58", "3"],
        ["EMIO4ENA", "59", "4"],
        ["EMIOLED1", "60", "PL_LED1"],
        ["EMIOLED2", "61", "PL_LED2"],
    ]
    defines = []
    defines.extend(defines_in)
    defines.extend(defines_out)

    cb.add_line_block()
    for i in defines:
        cb.add_block(get_c_define_block(i[0], i[1], i[2]))

    cb.print_code()


if __name__ == '__main__':
    test()

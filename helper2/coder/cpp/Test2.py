from helper.coder.CodeCreator import get_empty_block
from helper.coder.Coder import get_a_block
from helper.coder.c.Cer import get_c_remark_block, get_c_include_block, get_c_arg_declare_block, get_c_define_block


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

    defines_in_pin = [
        ["EMIOKEY1", "54", "PL_KEY1"],
        ["EMIOKEY2", "55", "PL_KEY2"],
    ]
    defines_out_pin = [
        ["EMIO1PUL", "56", "1"],
        ["EMIO2", "57", "2"],
        ["EMIO3", "58", "3"],
        ["EMIO4ENA", "59", "4"],
        ["EMIOLED1", "60", "PL_LED1"],
        ["EMIOLED2", "61", "PL_LED2"],
    ]
    defines_io = [
        ["input", "0", ""],
        ["output", "1", ""],
    ]
    defines = [
        defines_in_pin,
        defines_out_pin,
        defines_io,
    ]

    for i in defines:
        cb.add_line_block()
        for j in i:
            cb.add_block(get_c_define_block(j[0], j[1], get_c_remark_block(j[2])))

    cb.add_line_block()
    cb.add_block(get_c_arg_declare_block("XGpioPs", "xGpios"))

    def get_set_in_pin():
        return get_a_block(

        )

    cb.print_code()


if __name__ == '__main__':
    test()

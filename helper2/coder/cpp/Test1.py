from helper import CppHelper
from helper import FileHelper
from helper.FileHelper import TextFile
from helper.CppHelper import StrListListUnit


def out_all(
        text_file: TextFile = None,
):
    def print_to_file(s: str = ""):
        print(s, file=text_file)

    include_list = CppHelper.get_str_list_list_unit_1(
        "<stdio.h>",
        '"platform.h"',
        '"xgpiops.h"',
        '"xgpiops_hw.h"',
        '"sleep.h"',
    )

    def out_include():
        def c(s):
            print_to_file(
                f"#include {s[0]}",
            )

        include_list.trace(c)
        print_to_file()

    pin_in_list_unit = StrListListUnit()
    pin_in_list_unit.append("EMIOKEY1", "54", "PL_KEY1")
    pin_in_list_unit.append("EMIOKEY2", "55", "PL_KEY2")

    pin_out_list_unit = StrListListUnit()
    pin_out_list_unit.append("EMIO1PUL", "56", "1")
    pin_out_list_unit.append("EMIO2", "57", "2")
    pin_out_list_unit.append("EMIO3", "58", "3")
    pin_out_list_unit.append("EMIO4ENA", "59", "4")
    pin_out_list_unit.append("EMIOLED1", "60", "PL_LED1")
    pin_out_list_unit.append("EMIOLED2", "61", "PL_LED2")

    io_list_unit = StrListListUnit()
    io_list_unit.append("input", "0")
    io_list_unit.append("output", "1")

    define_list_unit = StrListListUnit()
    define_list_unit.extend(pin_in_list_unit)
    define_list_unit.extend(pin_out_list_unit)

    def out_define():
        def c(s):
            print_to_file(
                f"#define {s[0]} {s[1]} //{s[2]}",
            )

        define_list_unit.trace(c)
        print_to_file()

    def in_pin(
            tab_num: int,
    ):
        tab_str = "\t" * tab_num

        def c(s):
            print_to_file(
                f"{tab_str}XGpioPs_SetDirectionPin(&xGpios, {s[0]}, {io_list_unit.str_list_list[0][0]});\n"
            )

        print_to_file(f"{tab_str}//")
        pin_in_list_unit.trace(c)

    def out_pin(
            tab_num: int,
    ):
        tab_str = "\t" * tab_num

        def c(s):
            print_to_file(
                f"{tab_str}XGpioPs_SetDirectionPin(&xGpios, {s[0]}, {io_list_unit.str_list_list[1][0]});\n"
                f"{tab_str}XGpioPs_SetOutputEnablePin(&xGpios, {s[0]}, 1);\n"
            )

        print_to_file(f"{tab_str}//")
        pin_out_list_unit.trace(c)

    def out_main(
            tab_num: int,
    ):
        tab_str = "\t" * tab_num
        next_tab_num = tab_num + 1

        print_to_file("XGpioPs xGpios;")
        print_to_file(f"{tab_str}int main() {{")
        in_pin(next_tab_num, )
        out_pin(next_tab_num, )
        print_to_file(f"{tab_str}}}")

    out_include()
    out_define()
    out_main(0)


if __name__ == '__main__':
    out_file = FileHelper.open_file("./data/temp.txt", mode="w")
    out_all(out_file)

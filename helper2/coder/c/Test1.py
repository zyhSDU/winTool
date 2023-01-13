from helper.coder.CodeCreator import get_empty_block
from helper.coder.Coder import get_args_block
from helper.coder.c.Cer import get_c_include_block, get_c_arg_declare_block, get_c_define_block, \
    get_c_method_block, get_c_arg_block, get_c_for_block_1_1, get_c_return_block


def c_test1():
    def test1():
        c_includes_block = get_empty_block()
        for i in range(3):
            c_includes_block.add_block(get_c_include_block(f"a{i}.h"))
        c_includes_block.add_line_block()
        return c_includes_block

    def test2():
        c_b = get_empty_block()
        c_b.add_block(get_c_arg_declare_block("XTime", "tEnd"))
        c_b.add_block(get_c_arg_declare_block("XTime", "tCur"))
        c_b.add_block(get_c_arg_declare_block("u32", "tUsed"))
        c_b.add_line_block()
        return c_b

    def test3():
        c_b = get_empty_block()
        c_b.add_block(get_c_define_block("input", "0"))
        c_b.add_block(get_c_define_block("output", "1"))
        c_b.add_line_block()
        return c_b

    def test4():
        arg_type_int = "uint16_t"
        arg_time = "time"
        arg_i = "i"
        arg_j = "j"
        c_b = get_empty_block()
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

    cb = get_empty_block()
    cb.add_block(test1())
    cb.add_block(test2())
    cb.add_block(test3())
    cb.add_block(test4())
    cb.add_block(test5())
    cb.print_code()


if __name__ == '__main__':
    c_test1()

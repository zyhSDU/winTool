from typing import Callable

from helper.CallableHelper import call_none


class FunDecorator(object):
    def __init__(
            self,
            before_fun: Callable[[], None] = call_none,
            init_fun: Callable[[], None] = call_none,
            after_fun: Callable[[], None] = call_none,
    ):
        self.before_fun = before_fun
        self.init_fun = init_fun
        self.after_fun = after_fun

    def fun(self):
        self.before_fun()
        self.init_fun()
        self.after_fun()

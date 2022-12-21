import sys
from typing import Callable

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from helper.DecoratorHelper import FunDecorator


def get_signal(*args, **kwargs):
    return QtCore.pyqtSignal(args, kwargs)


class QWidgetWrapper(object):
    def __init__(self, view: QWidget = QWidget()):
        self.view: QWidget = view
        self.show_view_fun_decorator = FunDecorator()

    def show_view(self):
        self.show_view_fun_decorator.fun()


class QtController(object):
    def __init__(self, start_view: QMainWindow):
        self.start_view: QMainWindow = start_view

    def show_start_view(self):
        self.start_view.show()


class QApplicationWrapper(object):
    def __init__(self, app: QApplication, controller: QtController):
        self.app = app
        self.controller: QtController = controller

    def app_exit(self):
        sys.exit(self.app.exec_())

    def app_go(self, ):
        self.controller.show_start_view()
        self.app_exit()


def get_app_wrapper_1(
        get_controller: Callable[[], QtController],
) -> QApplicationWrapper:
    return QApplicationWrapper(QtWidgets.QApplication(sys.argv), get_controller())


def app_go_1(
        get_controller: Callable[[], QtController],
):
    app_wrapper = get_app_wrapper_1(get_controller)
    app_wrapper.app_go()


def get_main_view_2(
        init_main_view: Callable[[QMainWindow], None],
) -> QMainWindow:
    main_window = QMainWindow()
    init_main_view(main_window)
    return main_window


def get_controller_2(
        init_main_view: Callable[[QMainWindow], None],
):
    return QtController(get_main_view_2(init_main_view))


def get_app_wrapper_2(
        init_main_view: Callable[[QMainWindow], None],
) -> QApplicationWrapper:
    return QApplicationWrapper(QtWidgets.QApplication(sys.argv), get_controller_2(init_main_view))


def app_go_2(
        init_main_view: Callable[[QMainWindow], None],
):
    app_wrapper = get_app_wrapper_2(init_main_view)
    app_wrapper.app_go()

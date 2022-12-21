import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class QtController(object):
    def __init__(self, start_view: QMainWindow):
        self.start_view: QMainWindow = start_view

    def show_start_view(self):
        self.start_view.show()


class QApplicationWrapper(object):
    def __init__(self, app: QApplication, controller):
        self.app = app
        self.controller = controller

    def app_exit(self):
        sys.exit(self.app.exec_())

    def app_go(self, ):
        self.controller.show_start_view()
        self.app_exit()


def get_app_wrapper(get_controller) -> QApplicationWrapper:
    return QApplicationWrapper(QtWidgets.QApplication(sys.argv), get_controller())


def app_go(get_controller):
    app_wrapper = get_app_wrapper(get_controller)
    app_wrapper.app_go()

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication


class QApplicationWrapper(object):
    def __init__(self, app: QApplication):
        self.app = app

    def app_exit(self):
        sys.exit(self.app.exec_())


def get_app_wrapper() -> QApplicationWrapper:
    return QApplicationWrapper(QtWidgets.QApplication(sys.argv))

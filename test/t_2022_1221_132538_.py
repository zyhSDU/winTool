from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from helper import QtAppHelper
from helper.QtAppHelper import QtController
from helper.ObjectHelper import print_object

class MainWindow(QWidget):
    switch_window = QtAppHelper.get_signal(str)

    def __init__(
            self,
    ):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Main Window')

        layout = QtAppHelper.get_layout()

        self.line_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.line_edit)

        self.button = QtAppHelper.get_button('Switch Window', self.switch)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit(self.line_edit.text())



class WindowTwo(QWidget):
    def __init__(self, text):
        super(WindowTwo, self).__init__()
        self.setWindowTitle('Window Two')

        layout = QtAppHelper.get_layout()

        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)

        self.button = QtAppHelper.get_button('Close', self.close)
        layout.addWidget(self.button)

        self.setLayout(layout)


class Login(QWidget):
    switch_window = QtAppHelper.get_signal()

    def __init__(self):
        super(Login, self).__init__()
        self.setWindowTitle('Login')

        layout = QtWidgets.QGridLayout()

        self.button = QtAppHelper.get_button('Login', self.login)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def login(self):
        self.switch_window.emit()


class Controller(QtController):
    def __init__(self, start_view):
        super(Controller, self).__init__(start_view)
        self.start_view.switch_window.connect(self.show_main)

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_window_two)
        self.start_view.close()
        self.window.show()

    def show_window_two(self, text):
        self.window_two = WindowTwo(text)
        self.window.close()
        self.window_two.show()


def get_controller():
    return Controller(Login())


def main():
    QtAppHelper.app_go_1(get_controller)


if __name__ == '__main__':
    main()

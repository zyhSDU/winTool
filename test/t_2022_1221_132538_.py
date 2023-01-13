from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from helper.qt import QtAppHelper
from helper.qt.QtAppHelper import QtController


class MainWindow(QWidget):
    switch_window = QtAppHelper.get_signal(str)

    def __init__(
            self,
    ):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Main Window')

        layout = QtAppHelper.get_layout()

        line_edit = QtWidgets.QLineEdit()
        layout.addWidget(line_edit)
        self.line_edit = line_edit

        button = QtAppHelper.get_button('Switch Window', self.switch)
        layout.addWidget(button)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit(self.line_edit.text())


class WindowTwo(QWidget):
    def __init__(self, text):
        super(WindowTwo, self).__init__()
        self.setWindowTitle('Window Two')

        layout = QtAppHelper.get_layout()

        label = QtWidgets.QLabel(text)
        layout.addWidget(label)

        button = QtAppHelper.get_button('Close', self.close)
        layout.addWidget(button)

        self.setLayout(layout)


class Login(QWidget):
    switch_window = QtAppHelper.get_signal()

    def __init__(self):
        super(Login, self).__init__()
        self.setWindowTitle('Login')

        layout = QtWidgets.QGridLayout()

        button = QtAppHelper.get_button('Login', self.login)
        layout.addWidget(button)

        self.setLayout(layout)

    def login(self):
        self.switch_window.emit()


class Controller(QtController):
    def __init__(
            self,
    ):
        super(Controller, self).__init__(Login())
        assert isinstance(self.start_view, Login)
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
    return Controller()


def main():
    QtAppHelper.app_go_1(get_controller)


if __name__ == '__main__':
    main()

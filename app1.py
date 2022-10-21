import sys
from functools import partial
from typing import Callable

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from helper import ClipboardHelper
from helper import RegularExpressionHelper
from ui import main1
from ui.main1 import Ui_MainWindow


def paste_to_edit1(ui: main1.Ui_MainWindow):
    text1 = ClipboardHelper.get_text()
    ui.textEdit.setText(text1)


def copy_from_edit2(ui: main1.Ui_MainWindow):
    text1 = ui.textEdit_2.toPlainText()
    ClipboardHelper.copy_text(text1)


def action1(ui: main1.Ui_MainWindow):
    string = ui.textEdit.toPlainText()
    string = RegularExpressionHelper.split_to_per_line_one_cite(string)
    ui.textEdit_2.setText(string)


def action2(ui: main1.Ui_MainWindow):
    string = ui.textEdit.toPlainText()
    string = RegularExpressionHelper.split_by_sep(string)
    ui.textEdit_2.setText(string)


def action3(ui: main1.Ui_MainWindow):
    string = ui.textEdit.toPlainText()
    string = RegularExpressionHelper.emerge_lines(string)
    ui.textEdit_2.setText(string)


def action4(ui: main1.Ui_MainWindow):
    string = ui.textEdit.toPlainText()
    string = RegularExpressionHelper.emerge_lines_and_split_by_dot(string)
    ui.textEdit_2.setText(string)


def action_wrap_type(ui: main1.Ui_MainWindow, action: Callable[[Ui_MainWindow], None], btn_name: str):
    if ui.checkBox_1.isChecked():
        paste_to_edit1(ui)
    action(ui)
    if ui.checkBox_2.isChecked():
        copy_from_edit2(ui)
    assert isinstance(ui.pushButton_action_last, QPushButton)
    ui.pushButton_action_last.clicked.disconnect()
    ui.pushButton_action_last.setText(btn_name)
    fun_arg(ui, ui.pushButton_action_last, action, )


def fun_arg(ui, btn, action, ):
    btn.clicked.connect(partial(action_wrap_type, ui, action, btn.text()))


class MainUI(main1.Ui_MainWindow):
    def __init__(self, w: QMainWindow):
        self.setupUi(w)
        self.pushButton_left1.clicked.connect(partial(paste_to_edit1, self))
        self.pushButton_left2.clicked.connect(partial(copy_from_edit2, self))

        fun_arg(self, self.pushButton_action1, action1)
        fun_arg(self, self.pushButton_action2, action2)
        fun_arg(self, self.pushButton_action3, action3)
        fun_arg(self, self.pushButton_action4, action4)

        fun_arg(self, self.pushButton_action_last, action1)

        self.checkBox_1.setChecked(True)
        self.checkBox_2.setChecked(True)


class MyMainForm(QMainWindow):
    def __init__(self):
        # noinspection PyArgumentList
        super(MyMainForm, self).__init__()
        ui = MainUI(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MyMainForm()
    main_form.show()
    sys.exit(app.exec_())

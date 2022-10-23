import sys
from functools import partial
from logging import handlers as logging_handlers
from typing import Callable

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from helper import ClipboardHelper
from helper import RegularExpressionHelper
from helper.ConfigHelper import IniConfig
from helper.FileHelper import create_dir_of_path
from helper.LoggingHelper import get_logger2
from helper.TranslateHelper import baidu_translate
from ui import main1
from ui.main1 import Ui_MainWindow

file_name = "app1_logs/log"
create_dir_of_path(file_name)
app1_handler = logging_handlers.TimedRotatingFileHandler(file_name, when='D', encoding="utf-8")
log = get_logger2(handlers=[app1_handler])


def paste_to_edit1(ui: main1.Ui_MainWindow):
    text1 = ClipboardHelper.get_text()
    ui.textEdit.setText(text1)


def copy_from_edit2(ui: main1.Ui_MainWindow):
    text1 = ui.textEdit_2.toPlainText()
    ClipboardHelper.copy_text(text1)


def copy_from_edit3(ui: main1.Ui_MainWindow):
    text1 = ui.textEdit_3.toPlainText()
    ClipboardHelper.copy_text(text1)


def action1(ui: main1.Ui_MainWindow):
    string = ui.textEdit.toPlainText()
    string = RegularExpressionHelper.split_to_per_line_one_cite(string, log)
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


def action5(ui: main1.Ui_MainWindow):
    string = ui.textEdit.toPlainText()
    ui.textEdit_2.setText(string)


def action_wrap_type(ui: main1.Ui_MainWindow, action: Callable[[Ui_MainWindow], None], btn_name: str):
    try:
        if ui.checkBox_1.isChecked():
            paste_to_edit1(ui)
        log.info(f"\n框1内容：\n{ui.textEdit.toPlainText()}")
        action(ui)
        if ui.checkBox_2.isChecked():
            copy_from_edit2(ui)
        string2 = ui.textEdit_2.toPlainText()
        log.info(f"\n框2内容\n{string2}")
        if ui.checkBox_3.isChecked():
            ini = IniConfig("app1.ini")
            appid = ini.get("translate", "appid")
            secretKey = ini.get("translate", "secretKey")
            string3 = baidu_translate(
                appid=appid,
                secretKey=secretKey,
                translate_text=string2,
            )
            ui.textEdit_3.setText(string3)
            log.info(f"\n框3内容\n{string3}")
        assert isinstance(ui.pushButton_action_last, QPushButton)
        ui.pushButton_action_last.clicked.disconnect()
        ui.pushButton_action_last.setText(btn_name)
        fun_arg(ui, ui.pushButton_action_last, action, )
    except Exception as e:
        log.debug(e)


def fun_arg(ui, btn, action, ):
    btn.clicked.connect(partial(action_wrap_type, ui, action, btn.text()))


class MainUI(main1.Ui_MainWindow):
    def __init__(self, w: QMainWindow):
        self.setupUi(w)
        self.pushButton_left1.clicked.connect(partial(paste_to_edit1, self))
        self.pushButton_left2.clicked.connect(partial(copy_from_edit2, self))
        self.pushButton_left3.clicked.connect(partial(copy_from_edit3, self))

        fun_arg(self, self.pushButton_action1, action1)
        fun_arg(self, self.pushButton_action2, action2)
        fun_arg(self, self.pushButton_action3, action3)
        fun_arg(self, self.pushButton_action4, action4)
        fun_arg(self, self.pushButton_action5, action5)

        self.pushButton_action_last.setText(self.pushButton_action1.text())
        fun_arg(self, self.pushButton_action_last, action1)

        self.checkBox_1.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)


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

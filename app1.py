import sys
from functools import partial

from PyQt5.QtWidgets import QApplication, QMainWindow

from helper import ClipboardHelper
from helper import RegularExpressionHelper
from ui import main1


def paste_to_edit1(ui: main1.Ui_MainWindow):
    text1 = ClipboardHelper.get_text()
    ui.textEdit.setText("")
    ui.textEdit.setText(text1)


def copy_from_edit2(ui: main1.Ui_MainWindow):
    text1 = ui.textEdit_2.toPlainText()
    ClipboardHelper.copy_text(text1)


def action1(ui: main1.Ui_MainWindow):
    text1 = ui.textEdit.toPlainText()
    text2 = RegularExpressionHelper.split_to_per_line_one_cite(text1)
    text3 = "".join(text2).strip()
    ui.textEdit_2.setText(text3)


def action2(ui: main1.Ui_MainWindow):
    text1 = ui.textEdit.toPlainText()
    text2 = RegularExpressionHelper.split_by_sep(text1)
    text3 = "".join(text2).strip()
    ui.textEdit_2.setText(text3)


class MainUI(main1.Ui_MainWindow):
    def __init__(self, w: QMainWindow):
        self.setupUi(w)
        self.pushButton_left1.clicked.connect(partial(paste_to_edit1, self))
        self.pushButton_left2.clicked.connect(partial(copy_from_edit2, self))
        self.pushButton_action1.clicked.connect(partial(action1, self))
        self.pushButton_action2.clicked.connect(partial(action2, self))


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

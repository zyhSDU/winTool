# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 801)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 10, 471, 221))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 240, 471, 221))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_action1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_action1.setGeometry(QtCore.QRect(570, 120, 181, 28))
        self.pushButton_action1.setObjectName("pushButton_action1")
        self.pushButton_left1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left1.setGeometry(QtCore.QRect(520, 10, 41, 221))
        self.pushButton_left1.setObjectName("pushButton_left1")
        self.pushButton_left2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left2.setGeometry(QtCore.QRect(520, 240, 41, 221))
        self.pushButton_left2.setObjectName("pushButton_left2")
        self.pushButton_action2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_action2.setGeometry(QtCore.QRect(570, 150, 181, 28))
        self.pushButton_action2.setObjectName("pushButton_action2")
        self.pushButton_action3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_action3.setGeometry(QtCore.QRect(570, 180, 181, 28))
        self.pushButton_action3.setObjectName("pushButton_action3")
        self.pushButton_action4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_action4.setGeometry(QtCore.QRect(570, 210, 181, 28))
        self.pushButton_action4.setObjectName("pushButton_action4")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(570, 30, 231, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(570, 10, 211, 31))
        self.checkBox_1.setObjectName("checkBox_1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 290, 171, 21))
        self.label.setObjectName("label")
        self.pushButton_action_last = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_action_last.setGeometry(QtCore.QRect(570, 310, 181, 28))
        self.pushButton_action_last.setObjectName("pushButton_action_last")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 70, 501, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 31, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 470, 181, 21))
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 490, 471, 221))
        self.textEdit_3.setObjectName("textEdit_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(570, 50, 151, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_action5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_action5.setGeometry(QtCore.QRect(570, 240, 181, 28))
        self.pushButton_action5.setObjectName("pushButton_action5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(570, 270, 501, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(570, 90, 171, 21))
        self.label_8.setObjectName("label_8")
        self.pushButton_left3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left3.setGeometry(QtCore.QRect(520, 490, 41, 221))
        self.pushButton_left3.setObjectName("pushButton_left3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1087, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_action1.setText(_translate("MainWindow", "参考文献.多行格式化"))
        self.pushButton_left1.setText(_translate("MainWindow", "粘贴"))
        self.pushButton_left2.setText(_translate("MainWindow", "复制"))
        self.pushButton_action2.setText(_translate("MainWindow", "摘要.按分号分隔"))
        self.pushButton_action3.setText(_translate("MainWindow", "合并行"))
        self.pushButton_action4.setText(_translate("MainWindow", "合并行后按点分隔"))
        self.checkBox_2.setText(_translate("MainWindow", "自动将框2内容粘贴到剪切板"))
        self.checkBox_1.setText(_translate("MainWindow", "自动将剪切板粘贴到框1"))
        self.label.setText(_translate("MainWindow", "上一次使用："))
        self.pushButton_action_last.setText(_translate("MainWindow", "参考文献.多行格式化"))
        self.label_2.setText(_translate("MainWindow", "==================================================================="))
        self.label_3.setText(_translate("MainWindow", "框1"))
        self.label_4.setText(_translate("MainWindow", "框2"))
        self.label_5.setText(_translate("MainWindow", "框3，翻译为中文"))
        self.checkBox_3.setText(_translate("MainWindow", "是否翻译框2"))
        self.pushButton_action5.setText(_translate("MainWindow", "无处理"))
        self.label_7.setText(_translate("MainWindow", "==================================================================="))
        self.label_8.setText(_translate("MainWindow", "处理框1内容后输出到框2"))
        self.pushButton_left3.setText(_translate("MainWindow", "复制"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))


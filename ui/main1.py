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
        MainWindow.resize(1087, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 501, 261))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 280, 501, 261))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_action1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_action1.setGeometry(QtCore.QRect(570, 110, 181, 28))
        self.pushButton_action1.setObjectName("pushButton_action1")
        self.pushButton_left1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left1.setGeometry(QtCore.QRect(520, 10, 41, 261))
        self.pushButton_left1.setObjectName("pushButton_left1")
        self.pushButton_left2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left2.setGeometry(QtCore.QRect(520, 280, 41, 261))
        self.pushButton_left2.setObjectName("pushButton_left2")
        self.pushButton_action2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_action2.setGeometry(QtCore.QRect(570, 140, 181, 28))
        self.pushButton_action2.setObjectName("pushButton_action2")
        self.pushButton_action3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_action3.setGeometry(QtCore.QRect(570, 170, 181, 28))
        self.pushButton_action3.setObjectName("pushButton_action3")
        self.pushButton_action4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_action4.setGeometry(QtCore.QRect(570, 200, 181, 28))
        self.pushButton_action4.setObjectName("pushButton_action4")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(700, 10, 151, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(570, 10, 131, 31))
        self.checkBox_1.setObjectName("checkBox_1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 40, 171, 21))
        self.label.setObjectName("label")
        self.pushButton_action_last = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_action_last.setGeometry(QtCore.QRect(570, 60, 181, 28))
        self.pushButton_action_last.setObjectName("pushButton_action_last")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 90, 501, 21))
        self.label_2.setObjectName("label_2")
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
        self.checkBox_2.setText(_translate("MainWindow", "直接粘贴到剪切板"))
        self.checkBox_1.setText(_translate("MainWindow", "直接处理剪切板"))
        self.label.setText(_translate("MainWindow", "上一次使用："))
        self.pushButton_action_last.setText(_translate("MainWindow", "参考文献.多行格式化"))
        self.label_2.setText(_translate("MainWindow", "==================================================================="))
        self.menu.setTitle(_translate("MainWindow", "菜单"))


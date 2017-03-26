# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Help.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(300, 400)
        Help.setMinimumSize(QtCore.QSize(300, 400))
        Help.setMaximumSize(QtCore.QSize(300, 400))
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Help)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 301, 341))
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Help)
        self.pushButton.setGeometry(QtCore.QRect(100, 360, 99, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Help)
        self.pushButton.clicked.connect(Help.close)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "帮助"))
        self.plainTextEdit.setPlainText(_translate("Help", "这里是产品的帮助文档。\n"
"blablablabla"))
        self.pushButton.setText(_translate("Help", "确定"))


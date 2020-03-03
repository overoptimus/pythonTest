# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zuci.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 300)
        self.a = QtWidgets.QLineEdit(dialog)
        self.a.setGeometry(QtCore.QRect(40, 30, 113, 21))
        self.a.setObjectName("a")
        self.b = QtWidgets.QLineEdit(dialog)
        self.b.setGeometry(QtCore.QRect(40, 80, 113, 21))
        self.b.setObjectName("b")
        self.c = QtWidgets.QLineEdit(dialog)
        self.c.setGeometry(QtCore.QRect(220, 30, 113, 21))
        self.c.setObjectName("c")
        self.d = QtWidgets.QLineEdit(dialog)
        self.d.setGeometry(QtCore.QRect(220, 80, 113, 21))
        self.d.setObjectName("d")
        self.resoult = QtWidgets.QLineEdit(dialog)
        self.resoult.setGeometry(QtCore.QRect(120, 170, 113, 21))
        self.resoult.setObjectName("resoult")
        self.resoult.setEnabled(False)
        self.shengcheng = QtWidgets.QPushButton(dialog)
        self.shengcheng.setGeometry(QtCore.QRect(150, 240, 93, 28))
        self.shengcheng.setObjectName("shengcheng")
        self.shengcheng.clicked.connect(self.shengcheng_onclick)
        self.copy = QtWidgets.QPushButton(dialog)
        self.copy.setGeometry(QtCore.QRect(260, 240, 93, 28))
        self.copy.setObjectName("copy")
        self.copy.clicked.connect(self.copy_onclick)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "组词"))
        self.shengcheng.setText(_translate("dialog", "生成"))
        self.copy.setText(_translate("dialog", "复制"))

    @pyqtSlot()
    def shengcheng_onclick(self):
        a = self.a.text()
        b = self.b.text()
        c = self.c.text()
        d = self.d.text()
        self.resoult.setText(a + b + c + d)
        print('a:' + a + ', b:' + b + ', c:' + c + ', d:' +d)

    @pyqtSlot()
    def copy_onclick(self):
        copy_text = QApplication.clipboard()
        copy_text.setText(self.resoult.text())
        print('拷贝成功')

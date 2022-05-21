# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zad3_formtjAMPM.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(799, 652)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 20, 701, 591))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 30, 461, 411))
        self.label.setStyleSheet(u"background-color: #2b3038;\n"
"border-radius: 30px;")
        self.speakButton = QPushButton(self.widget)
        self.speakButton.setObjectName(u"speakButton")
        self.speakButton.setGeometry(QRect(270, 330, 191, 41))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(13)
        self.speakButton.setFont(font)
        self.speakButton.setStyleSheet(u"QPushButton{\n"
"background-color:  rgb(212, 192, 169);\n"
"color: #20242a;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #837c73;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-position: calc(100% - 10px)center;\n"
"background-color: #ff662b;;\n"
"}")
        self.commandEdit = QLineEdit(self.widget)
        self.commandEdit.setObjectName(u"commandEdit")
        self.commandEdit.setGeometry(QRect(150, 260, 441, 40))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        self.commandEdit.setFont(font1)
        self.commandEdit.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.commandEdit.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 60, 461, 81))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(34)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.nameLabel = QLabel(self.widget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(140, 120, 461, 31))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.nameLabel.setFont(font3)
        self.nameLabel.setStyleSheet(u"color: rgb(212, 192, 169);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.nameLabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.speakButton.setText(QCoreApplication.translate("Form", u"Speak", None))
        self.commandEdit.setText("")
        self.commandEdit.setPlaceholderText(QCoreApplication.translate("Form", u"type text here...", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Virtual assistant</p><p><br/></p></body></html>", None))
        self.nameLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">created by ...</span></p></body></html>", None))
    # retranslateUi


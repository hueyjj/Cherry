# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/CherryDesigner/home.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(700, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(Home)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Home)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 680, 480))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.urlLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.urlLabel.setObjectName("urlLabel")
        self.horizontalLayout.addWidget(self.urlLabel)
        self.userInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.userInput.setObjectName("userInput")
        self.horizontalLayout.addWidget(self.userInput)
        self.download = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.download.setObjectName("download")
        self.horizontalLayout.addWidget(self.download)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.title = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.image.setObjectName("image")
        self.verticalLayout_2.addWidget(self.image)
        self.description = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.description.setMinimumSize(QtCore.QSize(662, 194))
        self.description.setObjectName("description")
        self.verticalLayout_2.addWidget(self.description)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Form"))
        self.urlLabel.setText(_translate("Home", "Input url:"))
        self.download.setText(_translate("Home", "Download"))
        self.title.setText(_translate("Home", "Title here"))
        self.image.setText(_translate("Home", "Image here"))
        self.description.setHtml(_translate("Home", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">More information here....</p></body></html>"))


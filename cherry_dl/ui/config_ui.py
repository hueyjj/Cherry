# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/CherryDesigner/configuration.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Configuration(object):
    def setupUi(self, Configuration):
        Configuration.setObjectName("Configuration")
        Configuration.resize(700, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(Configuration)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(Configuration)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 666, 498))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dirInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.dirInput.setObjectName("dirInput")
        self.horizontalLayout.addWidget(self.dirInput)
        self.browse = QtWidgets.QPushButton(self.scrollAreaWidgetContents_5)
        self.browse.setObjectName("browse")
        self.horizontalLayout.addWidget(self.browse)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.formatGroup = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_5)
        self.formatGroup.setObjectName("formatGroup")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.formatGroup)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mp3 = QtWidgets.QRadioButton(self.formatGroup)
        self.mp3.setObjectName("mp3")
        self.horizontalLayout_4.addWidget(self.mp3)
        self.m4a = QtWidgets.QRadioButton(self.formatGroup)
        self.m4a.setObjectName("m4a")
        self.horizontalLayout_4.addWidget(self.m4a)
        self.mp4 = QtWidgets.QRadioButton(self.formatGroup)
        self.mp4.setObjectName("mp4")
        self.horizontalLayout_4.addWidget(self.mp4)
        self.gridLayout_9.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.formatGroup)
        self.videoGroup = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_5)
        self.videoGroup.setObjectName("videoGroup")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.videoGroup)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.videoAndAudio = QtWidgets.QRadioButton(self.videoGroup)
        self.videoAndAudio.setObjectName("videoAndAudio")
        self.horizontalLayout_5.addWidget(self.videoAndAudio)
        self.videoOnly = QtWidgets.QRadioButton(self.videoGroup)
        self.videoOnly.setObjectName("videoOnly")
        self.horizontalLayout_5.addWidget(self.videoOnly)
        self.audioOnly = QtWidgets.QRadioButton(self.videoGroup)
        self.audioOnly.setObjectName("audioOnly")
        self.horizontalLayout_5.addWidget(self.audioOnly)
        self.gridLayout_10.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.videoGroup)
        spacerItem = QtWidgets.QSpacerItem(20, 314, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.ok = QtWidgets.QPushButton(Configuration)
        self.ok.setObjectName("ok")
        self.horizontalLayout_6.addWidget(self.ok)
        self.apply = QtWidgets.QPushButton(Configuration)
        self.apply.setObjectName("apply")
        self.horizontalLayout_6.addWidget(self.apply)
        self.cancel = QtWidgets.QPushButton(Configuration)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_6.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Configuration)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        _translate = QtCore.QCoreApplication.translate
        Configuration.setWindowTitle(_translate("Configuration", "Form"))
        self.label.setText(_translate("Configuration", "Save directory"))
        self.browse.setText(_translate("Configuration", "Browse"))
        self.formatGroup.setTitle(_translate("Configuration", "Format:"))
        self.mp3.setText(_translate("Configuration", ".mp3"))
        self.m4a.setText(_translate("Configuration", ".m4a"))
        self.mp4.setText(_translate("Configuration", ".mp4"))
        self.videoGroup.setTitle(_translate("Configuration", "Video:"))
        self.videoAndAudio.setText(_translate("Configuration", "Video and audio"))
        self.videoOnly.setText(_translate("Configuration", "Video (only)"))
        self.audioOnly.setText(_translate("Configuration", "Audio (only)"))
        self.ok.setText(_translate("Configuration", "OK"))
        self.apply.setText(_translate("Configuration", "Apply"))
        self.cancel.setText(_translate("Configuration", "Cancel"))


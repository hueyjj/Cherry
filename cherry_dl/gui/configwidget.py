from PyQt5 import (
    QtCore,
    QtWidgets,
)

from PyQt5.QtCore import (
    pyqtSignal,
    pyqtSlot,
)

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QRadioButton,
    QFileDialog,
)

from ..ui.config_ui import Ui_Configuration
from ..core.utils import Config

class ConfigWidget(QWidget, Ui_Configuration):
    configChanged = pyqtSignal()
    configCancelled = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)

        self.setupUi(self)

        self.config = Config()

        self.initGuiOptions()

        # File dialog for path to save directory
        self.browse.clicked.connect(self.openFileDialog)
    
    def initGuiOptions(self):
        c = self.config.getConfig()
        self.dirInput.setText(c["saveDirectory"])

        # Enable format radio button
        f = c["format"]
        if f == "mp3":
            self.mp3.setChecked(True)
        elif f == "m4a":
            self.m4a.setChecked(True)
        elif f == "mp4":
            self.mp4.setChecked(True)

        # Enable video radio button
        v = c["video"]
        if v == "best":
            self.videoAndAudio.setChecked(True)
        elif v == "bestvideo":
            self.videoOnly.setChecked(True)
        elif v == "bestaudio":
            self.audioOnly.setChecked(True)

        # Connect format signals to options
        for formatOption in self.formatGroup.children():
            if isinstance(formatOption, QRadioButton):
                formatOption.clicked.connect(self.setFormat)
            
        for videoOption in self.videoGroup.children():
            if isinstance(videoOption, QRadioButton):
                videoOption.clicked.connect(self.setVideo)
        
        self.apply.clicked.connect(self.saveConfig)
        self.cancel.clicked.connect(self.cancelConfig)
        self.ok.clicked.connect(self.okConfig)
    
    def openFileDialog(self):
        dialog = QFileDialog(caption="Save folder", directory=self.config.homeDir, filter='')
        dialog.setFileMode(QFileDialog.Directory)
        dialog.directoryEntered.connect(self.setFileDialogSaveURL)
        dialog.finished.connect(self.setSaveDir)
        dialog.exec()

    @pyqtSlot(str)
    def setFileDialogSaveURL(self, path):
        self.fileDialogSaveURL = path

    @pyqtSlot() 
    def setSaveDir(self):
        print(self.fileDialogSaveURL)
        self.dirInput.setText(self.fileDialogSaveURL)
        self.config.setSaveDir(self.fileDialogSaveURL)

    def getConfig(self):
        return self.config.getConfig()
    
    def setFormat(self):
        sender = self.sender()
        if sender is self.mp3:
            self.config.setFormat("mp3")
        elif sender is self.m4a:
            self.config.setFormat("m4a")
        elif sender is self.mp4:
            self.config.setFormat("mp4")
        
    def setVideo(self):
        sender = self.sender()
        if sender is self.videoAndAudio:
            self.config.setVideo("best")
        elif sender is self.videoOnly:
            self.config.setVideo("bestvideo")
        elif sender is self.audioOnly:
            self.config.setVideo("bestaudio")

    def saveConfig(self):
        self.config.saveConfig()
        self.configChanged.emit()
    
    def cancelConfig(self):
        # FIXME Reset configs back to original

        self.configCancelled.emit()
    
    def okConfig(self):
        self.saveConfig()
        self.cancelConfig()
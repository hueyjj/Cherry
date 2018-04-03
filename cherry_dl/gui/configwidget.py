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
)

from ..ui.config_ui import Ui_Configuration
from ..core.utils import Config

class ConfigWidget(QWidget, Ui_Configuration):
    formatChanged = pyqtSignal()
    configCancelled = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)

        self.setupUi(self)

        self.config = Config()
        self.initGuiOptions()
    
    def initGuiOptions(self):
        c = self.config.getConfig()
        self.dirInput.setText(c["saveDirectory"])

        # Enable format radio button
        f = c["youtubedl"]["format"]
        if f == "mp3":
            self.mp3.setChecked(True)
        elif f == "m4a":
            self.m4a.setChecked(True)
        elif f == "mp4":
            self.mp4.setChecked(True)

        # Enable video radio button

        # Connect signals to options
        for formatOption in self.formatGroup.children():
            if isinstance(formatOption, QRadioButton):
                formatOption.clicked.connect(self.setFormat)
        
        self.apply.clicked.connect(self.saveConfig)
        self.cancel.clicked.connect(self.cancelConfig)
    
    def setFormat(self):
        sender = self.sender()
        if sender is self.mp3:
            self.config.setFormat("mp3")
        elif sender is self.m4a:
            self.config.setFormat("m4a")
        elif sender is self.mp4:
            self.config.setFormat("mp4")

    def saveConfig(self):
        self.config.saveConfig()
    
    def cancelConfig(self):
        # FIXME Unset configs back to original

        self.configCancelled.emit()
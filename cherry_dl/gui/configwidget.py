from PyQt5 import (
    QtWidgets,
)

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
)

from ..ui.config_ui import Ui_Configuration
from ..core.utils import Config

class ConfigWidget(QWidget, Ui_Configuration):

    def __init__(self, parent):
        super().__init__(parent)

        self.setupUi(self)

        self.config = Config()
        self.initGuiOptions()
    
    def initGuiOptions(self):
        c = self.config.getConfig()
        self.dirInput.setText(c["saveDirectory"])


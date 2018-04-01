from PyQt5 import (
    QtWidgets,
)

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
)

from ..ui.config_ui import Ui_Configuration

class ConfigWidget(QWidget, Ui_Configuration):

    def __init__(self, parent):
        super().__init__(parent)

        self.setupUi(self)

from PyQt5 import (
    QtWidgets,
)

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
)

from ..ui.config_ui import Ui_Configuration

class Config(QWidget, Ui_Configuration):

    def __init__(self, parent=None):
        super().__init__()

        self.setupUi(self)

    def setupConfig(self):
        for child in self.widget.children():
            if child.objectName() == "pushButton_3":
                print("foo")
                print(type(child))
                child.clicked.connect(self.foo)
    
    def foo(self):
        print("Button 3 clicked")


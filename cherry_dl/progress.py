from PyQt5 import (
    QtCore, 
    QtWidgets, 
    QtGui
)
from PyQt5.QtCore import (
    Qt, 
    QCoreApplication, 
    QThread, 
    pyqtSignal
)
from PyQt5.QtWidgets import (
    QApplication, 
    QComboBox, 
    QDialog,
    QDialogButtonBox, 
    QFormLayout, 
    QGridLayout, 
    QGroupBox, 
    QHBoxLayout,
    QLabel, 
    QLineEdit, 
    QMenu, 
    QMenuBar, 
    QPushButton, 
    QSpinBox, 
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QStackedWidget,
    QListWidget,
    QRadioButton,
    QCheckBox,
)

from PyQt5.QtGui import (
    QIcon, 
    QCursor, 
    QWindow, 
    QGuiApplication
)

class Progress(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"), sex)
        layout.addRow("Date of Birth", QLineEdit())

        self.setLayout(layout)

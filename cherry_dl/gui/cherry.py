import sys
import os

from PyQt5 import (
    QtCore, 
    QtWidgets, 
    QtGui
)
from PyQt5.QtCore import (
    Qt, 
    QCoreApplication, 
    QThread, 
    QThreadPool,
    pyqtSignal,
    pyqtSlot,
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
    QToolButton,
    QMainWindow,
    QAction,
    QSizePolicy,
)

from PyQt5.QtGui import (
    QIcon, 
    QCursor, 
    QWindow, 
    QGuiApplication,
    QPixmap,
)

from ..ui.main_ui import Ui_MainWindow
from .sidebar import Sidebar
from .home import Home
from .progress import Progress
from .history import History
from .config import Config
from ..core.downloader import (
    MetaInformation,
    Downloader,
)


class Cherry(QMainWindow, Ui_MainWindow):
    """ Main window that holds the main layout """

    def __init__(self, parent=None):
        super().__init__()

        self.setupUi(self)

        # Create sidebar
        self.sidebar = Sidebar(self.centralwidget)
        self.sidebar.actionChanged.connect(self.changeDisplay)

        self.stackedWidget = QStackedWidget()

        # Create separate widgets (views) for stacked widget
        self.home = Home(self.stackedWidget)
        self.progress = Progress(self.stackedWidget)
        self.history = History(self.stackedWidget)
        self.config = Config(self.stackedWidget)

        self.stackedWidget.addWidget(self.home)
        self.stackedWidget.addWidget(self.progress)
        self.stackedWidget.addWidget(self.history)
        self.stackedWidget.addWidget(self.config)

        self.horizontalLayout.addWidget(self.sidebar)
        self.horizontalLayout.addWidget(self.stackedWidget)

        # Apparently not needed anymore
        #self.setMinimumWidth(self.stackedWidget.width() + self.sidebar.width() + 10)

        self.setWindowTitle("cherry-dl")

    @pyqtSlot(int)
    def changeDisplay(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def closeEvent(self, closeEvent):
        QCoreApplication.exit()

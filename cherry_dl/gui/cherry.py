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
from .sidebarwidget import SidebarWidget
from .homewidget import HomeWidget
from .progresswidget import ProgressWidget
from .historywidget import HistoryWidget
from .configwidget import ConfigWidget
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
        self.sidebar = SidebarWidget(self.centralwidget)
        self.sidebar.actionChanged.connect(self.changeDisplay)

        self.stackedWidget = QStackedWidget()

        # Create separate widgets (views) for stacked widget
        self.configWidget = ConfigWidget(self.stackedWidget)
        self.configWidget.configCancelled.connect(self.changeDisplayToHome)
        self.configWidget.configChanged.connect(self.changeConfigInHome)

        self.homeWidget = HomeWidget(self.stackedWidget)
        self.homeWidget.setConfig(self.configWidget.getConfig())

        self.progressWidget = ProgressWidget(self.stackedWidget)
        self.historyWidget = HistoryWidget(self.stackedWidget)

        self.stackedWidget.addWidget(self.homeWidget)
        self.stackedWidget.addWidget(self.progressWidget)
        self.stackedWidget.addWidget(self.historyWidget)
        self.stackedWidget.addWidget(self.configWidget)

        self.horizontalLayout.addWidget(self.sidebar)
        self.horizontalLayout.addWidget(self.stackedWidget)

        # Apparently not needed anymore
        #self.setMinimumWidth(self.stackedWidget.width() + self.sidebar.width() + 10)

        dirname = os.path.dirname(__file__)
        windowIconPath = os.path.join(dirname, "../../icons/cherry.png")
        self.windowIcon = QIcon(windowIconPath)
        self.setWindowIcon(self.windowIcon)
        self.setWindowTitle("cherry-dl")

    @pyqtSlot(int)
    def changeDisplay(self, index):
        self.stackedWidget.setCurrentIndex(index)
    
    @pyqtSlot()
    def changeDisplayToHome(self):
        self.stackedWidget.setCurrentIndex(0)
    
    @pyqtSlot()
    def changeConfigInHome(self):
        self.homeWidget.setConfig(self.configWidget.getConfig())

    def closeEvent(self, closeEvent):
        QCoreApplication.exit()

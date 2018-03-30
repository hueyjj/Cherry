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

from .cherryui import Ui_MainWindow
from .sidebar import Sidebar
from core.downloader import MetaInformation


class Cherry(QMainWindow, Ui_MainWindow):
    """ Main window that holds the main layout """

    # FIXME Embedding thumbnail requires ffmpeg and atomicparsely. Include as dependencies in project later?
    defaultYoutubeOpts = {
        "format": "m4a",
        "ignoreerrors": True,
        "writethumbnail": True,
        "outtmpl": "%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "EmbedThumbnail",
        }],
    }
    userYoutubeOpts = {
    }

    def __init__(self, parent=None):
        super(Cherry, self).__init__()

        self.metaThreadPool = QThreadPool()

        self.setupUi(self)

        ## Override sidebar generated by Qt designer
        self.sidebar = Sidebar(self.centralWidget)

        # Change display when a sidebar action is clicked
        self.connectToSidebar(self.sidebar)

        self.run.clicked.connect(self.startMetaDownloadThread)

        self.description.setReadOnly(True)

        # Rearrange widget order
        self.horizontalLayout.removeWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.sidebar)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.setWindowTitle("Cherry")

    def connectToSidebar(self, sidebar):
        sidebar.actionChanged.connect(self.changeDisplay)
    
    def startMetaDownloadThread(self):
        url = self.url.text()

        meta = MetaInformation(url)
        meta.signal.metaDownloaded.connect(self.loadMetaInfo)
        meta.signal.unableToRetrieveMeta.connect(self.noMetaInformationFound)

        self.metaThreadPool.start(meta)

    @pyqtSlot(dict)
    def loadMetaInfo(self, meta):
        print("Loaded meta information")

        # Title
        self.title.setText(meta["title"])

        # Description
        self.description.setText("""
        <p>
        %s
        </p>
        """ % meta["description"])

        # Image (load from a byte array)
        pic = QPixmap()
        pic.loadFromData(meta["thumbnail"])
        pic = pic.scaledToWidth(self.home.width())
        self.image.setPixmap(pic)

    @pyqtSlot(str)
    def noMetaInformationFound(self, url):
        if url:
            print("No meta information found for " + url)
        else:
            print("No meta information found and no url provided.")

    @pyqtSlot(int)
    def changeDisplay(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def closeEvent(self, closeEvent):
        QCoreApplication.exit()

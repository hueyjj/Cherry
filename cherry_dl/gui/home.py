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

from ..ui.home_ui import Ui_Home
from ..core.downloader import (
    MetaInformation,
    Downloader,
)


class Home(QWidget, Ui_Home):

    metaThreadPool = QThreadPool()

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

    def __init__(self, parent):
        super().__init__(parent)

        self.setupUi(self)

        self.userInput.textChanged.connect(self.urlChanged)
        self.download.clicked.connect(self.startDownload)

        self.description.setReadOnly(True)

    def startMetaDownloadThread(self):
        url = self.userInput.text()

        meta = MetaInformation(url)
        meta.signal.metaDownloaded.connect(self.loadMetaInfo)
        meta.signal.unableToRetrieveMeta.connect(self.noMetaInformationFound)

        self.metaThreadPool.start(meta)

    def startDownload(self):
        # validate(self.userInput.text())
        url = self.userInput.text()

        dl = Downloader(url, r"C:/users/jj/downloads", self.defaultYoutubeOpts)

        self.metaThreadPool.start(dl)

    @pyqtSlot(str)
    def urlChanged(self, text):
        # FIXME validate url later
        self.startMetaDownloadThread()

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
        pic = pic.scaledToWidth(self.width())
        self.image.setPixmap(pic)

    @pyqtSlot(str)
    def noMetaInformationFound(self, url):
        if url:
            print("No meta information found for " + url)
        else:
            print("No meta information found and no url provided.")

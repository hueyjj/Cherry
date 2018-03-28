from PyQt5 import (
    QtCore, 
    QtWidgets, 
    QtGui
)
from PyQt5.QtCore import (
    Qt, 
    QCoreApplication, 
    QThread, 
    QRect,
    QPoint,
    QSize,
    pyqtSignal,
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
)

from PyQt5.QtGui import (
    QIcon,
    QCursor,
    QWindow,
    QGuiApplication,
    QPainter,
    QFont,
    QColor,
)


class Sidebar(QWidget):

    # Widget parameter for extracting information from UI widget if necessary
    def __init__(self, parent):
        super(Sidebar, self).__init__(parent)

        self.buttonSize = 90

        self.homeAction = QAction(QIcon("./icons/home.png"), "Home", self)
        self.progressAction = QAction(QIcon("./icons/progress.png"), "Progress", self)
        self.historyAction = QAction(QIcon("./icons/history.png"), "History", self)

        self.actionList = [self.homeAction, self.progressAction, self.historyAction]

        self.addAction(self.homeAction)
        self.setObjectName("sidebar")

    # Set minimum size of sidebar
    def minimumSizeHint(self):
        return self.buttonSize * QSize(1, len(self.actionList))

    def paintEvent(self, event):
        p = QPainter(self)

        font = QFont(p.font())
        font.setFamily("Helvetica Neue")
        p.setFont(font)

        actionY = 0
        actionHeight = 90
        p.fillRect(QRect(), QColor(100, 100, 100));

        for action in self.actionList:
            actionRect = QRect(0, actionY, event.rect().width(), actionHeight)

            if action.isChecked():
                p.fillRect(actionRect, QColor(35, 35, 35))

            #if action == mOverAction:
            #    p.fillRect(actionRect, QColor(150, 150, 150))

            p.setPen(QColor(255, 255, 255))
            size = p.fontMetrics().size(Qt.TextSingleLine, action.text())
            actionTextRect = QRect(QPoint(actionRect.width() / 2 - size.width() / 2, actionRect.bottom() - size.height() - 5), size)
            p.drawText(actionTextRect, Qt.AlignCenter, action.text())

            actionIconRect = QRect(0, actionY + 10, actionRect.width(), actionRect.height()-2 * actionTextRect.height() - 10)
            actionIcon = QIcon(action.icon())
            actionIcon.paint(p, actionIconRect)

            actionY += actionRect.height()

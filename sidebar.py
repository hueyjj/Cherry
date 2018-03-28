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

        self.homeAction = QAction(QIcon("./icons/icon0.png"), "Home", self)
        self.setFixedSize(90, 90)
        self.setMinimumSize(90, 90)

        self.addAction(self.homeAction)
        self.setObjectName("sidebar")

    def minimumSize(self):
        return QSize(90, 90)

    def paintEvent(self, event):
        p = QPainter(self)

        font = QFont(p.font())
        font.setFamily("Helvetica Neue")
        p.setFont(font)

        action_y = 0
        action_height = 90
        p.fillRect(QRect(), QColor(100, 100, 100));
        actionRect = QRect(0, action_y, event.rect().width(), action_height)

        if self.homeAction.isChecked():
            p.fillRect(actionRect, QColor(35, 35, 35))

        #if self.homeAction == mOverAction:
        #    p.fillRect(actionRect, QColor(150, 150, 150))

        p.setPen(QColor(255, 255, 255))
        size = p.fontMetrics().size(Qt.TextSingleLine, self.homeAction.text())
        actionTextRect = QRect(QPoint(actionRect.width() / 2 - size.width() / 2, actionRect.bottom() - size.height() - 5), size)
        p.drawText(actionTextRect, Qt.AlignCenter, self.homeAction.text())

        #actionIconRect = QRect(0, action_y + 10, actionRect.width(), actionRect.height()-2 * actionTextRect.height() - 10)
        actionIconRect = QRect(0, 0, actionRect.width(), actionRect.height()-2 * actionTextRect.height() - 10)
        actionIcon = QIcon(self.homeAction.icon())
        actionIcon.paint(p, actionIconRect)

        action_y += actionRect.height()

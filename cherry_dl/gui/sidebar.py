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
    QStyle,
    QStyleOption,
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
    
    actionChanged = pyqtSignal(int)

    # Widget parameter for extracting information from UI widget if necessary
    def __init__(self, parent):
        super(Sidebar, self).__init__(parent)

        # Home, progress, history, etc. width and height
        self.actionWidth = 90
        self.actionHeight = 90

        dirname = os.path.dirname(__file__)
        homeIconPath = os.path.join(dirname, "../../icons/cherry.png")
        progressIconPath = os.path.join(dirname, "../../icons/tree.png")
        historyIconPath = os.path.join(dirname, "../../icons/roots.png")
        configIconPath = os.path.join(dirname, "../../icons/gear-white.png")
        self.homeAction = QAction(QIcon(homeIconPath), "Home", self)
        self.progressAction = QAction(QIcon(progressIconPath), "Progress", self)
        self.historyAction = QAction(QIcon(historyIconPath), "History", self)
        self.configAction = QAction(QIcon(configIconPath), "Config", self)

        self.actionList = [
            self.homeAction,
            self.progressAction,
            self.historyAction,
            self.configAction,
        ]

        for action in self.actionList:
            self.addAction(action)

        self.selectedAction = 0

        self.setStyleSheet("background-color:black;")
        self.setObjectName("sidebar")

    def setSelectedAction(self, index):
        self.selectedAction = index
        # Emit signal to tell others that they should be in a home widget
        self.actionChanged.emit(index)

    # Finds which action that the point lies in
    def actionAt(self, at):
        actionY = 0
        for action in self.actionList:
            actionRect = QRect(0, actionY, self.actionWidth, self.actionHeight)
            if actionRect.contains(at):
                return action
            actionY += actionRect.height()
        return None

    # Set minimum size of sidebar
    def minimumSizeHint(self):
        return QSize(self.actionWidth, self.actionHeight * len(self.actionList))
    
    def mousePressEvent(self, event):
        action = self.actionAt(event.pos())
        #if action:
        #    print("x: " + str(event.pos().x()) + " y: " + str(event.pos().y()) + " " + action.text() + " pressed")
        # FIXME Programmically assign index 
        if action == self.homeAction:
            self.setSelectedAction(0)
        elif action == self.progressAction:
            self.setSelectedAction(1)
        elif action == self.historyAction:
            self.setSelectedAction(2)
        elif action == self.configAction:
            self.setSelectedAction(3)

    def paintEvent(self, event):
        p = QPainter(self)

        # Need this configuration to enable stylesheets for subclasses of QWidgets
        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)

        # Set font
        font = QFont(p.font())
        font.setFamily("Helvetica Neue")
        p.setFont(font)

        actionY = 0

        for action in self.actionList:
            actionRect = QRect(0, actionY, self.actionWidth, self.actionHeight)

            if action.isChecked():
                p.fillRect(actionRect, QColor(35, 35, 35))

            #if action == mOverAction:
            #    p.fillRect(actionRect, QColor(150, 150, 150))

            # Draw text for button
            p.setPen(QColor(255, 255, 255))
            size = p.fontMetrics().size(Qt.TextSingleLine, action.text())
            actionTextRect = QRect(QPoint(actionRect.width() / 2 - size.width() / 2, actionRect.bottom() - size.height() - 5), size)
            p.drawText(actionTextRect, Qt.AlignCenter, action.text())

            # Draw button
            actionIconRect = QRect(0, actionY, actionRect.width(), actionRect.height() - 2 * actionTextRect.height() - 10)
            actionIcon = QIcon(action.icon())
            actionIcon.paint(p, actionIconRect)

            # Move to next button location
            actionY += actionRect.height()
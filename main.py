#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication
from cherry import Cherry
from cherryui import Ui_MainWindow

def main():
    import sys

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    cherry = Cherry()
    cherry.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

from PyQt5.QtWidgets import QApplication

from .gui.cherry import Cherry

def main():
    import sys

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    cherry = Cherry()
    cherry.show()

    sys.exit(app.exec_())


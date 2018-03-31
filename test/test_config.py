from PyQt5 import (
    QtWidgets,
)
from PyQt5.QtWidgets import (
    QApplication,
)

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cherry_dl.gui.config import Config

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    config = Config()
    config.show()

    sys.exit(app.exec_())
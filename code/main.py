import sys
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from first_window import FirstPage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = FirstPage()

    mainWindow.show()

    sys.exit(app.exec_())
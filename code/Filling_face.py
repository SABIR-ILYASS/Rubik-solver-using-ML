from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FillingFace(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Fenêtre non modale")
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        # self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setFixedSize(500, 600)
        self.setStyleSheet("""
            background-image: url(C:/Users/sabir/Desktop/rubik_solver/Images/background2.jpg);
            background-size: 100% auto;  
            background-repeat: no-repeat;
        """)
        self.titleLabel = QLabel("Filling the face number: {}".format(1), self)
        self.titleLabel.setGeometry(30, 10, 480, 50)
        # add a shadow effect to the title label
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(28)
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setOffset(0, 0)
        self.titleLabel.setGraphicsEffect(shadow)

        font = QFont()
        font.setPointSize(30)
        font.setFamily("Gabriola")
        font.setBold(True)

        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setStyleSheet("color: #a3f9ff;")

        self.titleLabel.show()

        self.face_widget = QWidget(self)
        self.face_widget.setGeometry(10, 60, 480, 500)
        self.face_widget.setStyleSheet("background-color: #FFFFFF;")
        """

        self.COLORS = ["White", "Yellow", "Red", "Orange", "Blue", "Green"]

        self.list_buttons_colors = []

        self.face_widget = QWidget(self)
        self.face_widget.setGeometry(10, 10, 480, 500)
        self.face_widget.setStyleSheet(
                                    "background-color: #000000;"
        )
        self.face_widget.show()

        iteration = 0
        for color in self.COLORS:
            button = QPushButton("{}".format(color), self)
            button.setGeometry(10 + 100 * iteration, 450, 80, 40)

            button.setStyleSheet(
                "QPushButton {"
                "   background-color: #a3f9ff;"
                "   border-style: solid;"
                "   border-width: 0px;"
                "   border-color: #1a5ebd;"
                "   border-radius: 10px;"
                "   color: #081B2A;"
                "   font-size: 16px;"
                "   font-weight: bold;"
                "}"
                "QPushButton:hover {"
                "   background-color: #1a5ebd;"
                "   color: white;"
                "}"
            )
            iteration += 1
            self.list_buttons_colors.append(button)

        for button in self.list_buttons_colors:  button.show()"""
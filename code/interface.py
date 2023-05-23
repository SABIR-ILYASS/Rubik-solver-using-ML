from PySide2.QtGui import *
from PySide2.QtWidgets import *

from OpenGL_widget import PygameWidget
from Filling_face import FillingFace


class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.help_button1 = QPushButton("Help!", self)
        self.setWindowTitle("Rubik's cube solver")
        self.setFixedSize(1200, 600)

        self.setWindowIcon(QIcon("C:/Users/sabir/Desktop/rubik_solver/Images/logo.png"))

        self.centralWidget = QWidget(self)
        self.centralWidget.setFixedSize(1200, 600)
        self.centralWidget.setStyleSheet("""background-image: url(C:/Users/sabir/Desktop/rubik_solver/Images/background.jpg);
                            background-size: cover;
                            background-repeat: no-repeat;
                            background-position: center;
                           """)
        self.setCentralWidget(self.centralWidget)

        self.show_Window_title(1)
        self.show_help_button1()
        self.show_manualy_button()

        self.rubik_3D = QWidget(self)
        self.rubik_3D.hide()

        self.white_widget = None

        self.list_buttons = []
        self.list_buttons_colors = []
        self.MOVES = ["up", "down", "right", "left"]


    def show_Window_title(self, title_index=True):
        title = "Rubik's Cube Solver" if title_index else "Rotate the cube."
        # create a label for the title text
        self.titleLabel = QLabel(title, self)
        self.titleLabel.setGeometry(0, 150, 1200, 200) if title_index else self.titleLabel.setGeometry(610, 80, 580, 50)

        # add a shadow effect to the title label
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setOffset(0, 0)
        self.titleLabel.setGraphicsEffect(shadow)

        font = QFont()
        font.setPointSize(100) if title_index else font.setPointSize(30)
        font.setFamily("Gabriola")
        font.setBold(True)

        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setStyleSheet("color: #a3f9ff;")

        self.titleLabel.show()

    def hide_window_title(self):
        self.titleLabel.hide()

    def show_help_button1(self):
        self.help_button1.setGeometry(1100, 20, 80, 25)
        self.help_button1.setStyleSheet(
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

        # Connect a function to the button click event
        self.help_button1.clicked.connect(self.show_help)

    def hide_help_button1(self):
        self.help_button1.hide()

    def hide_camera_button(self):
        self.button1.hide()

    def show_manualy_button(self):
        # Create a button
        icon2 = QIcon("Images/manually.png")
        self.button2 = QPushButton(icon2, " Add the faces manually.", self)

        # Set the button position and size
        self.button2.setGeometry(450, 400, 300, 50)

        # Set the button style using CSS
        self.button2.setStyleSheet(
            "QPushButton {"

            "   color: #081B2A;"
            "   font-size: 16px;"
            "   font-weight: bold;"
            "}"
            "QPushButton:hover {"
            "   background-color: #1a5ebd;"
            "   color: white;;"
            "}"
        )

        # Connect a function to the button click event
        self.button2.clicked.connect(self.show_white_widget)

    def hide_manually_button(self):
        self.button2.hide()

    def show_help(self):
        help_dialog = QDialog(self)
        help_dialog.setWindowTitle("Help")
        help_dialog.setModal(True)

        help_label = QLabel("This is some help text. Click the close button to close this window.")
        help_layout = QVBoxLayout()
        help_layout.addWidget(help_label)
        help_dialog.setLayout(help_layout)

        help_dialog.exec_()

    def show_white_widget(self):
        """
        self.hide_window_title()
        self.hide_manually_button()
        if self.white_widget is None:
            self.widget_3d = QLabel(self)
            self.widget_3d.setGeometry(10, 10, 580, 500)
            self.widget_3d.setStyleSheet(
            "   background-color: white;" 
            "   border-radius: 10px;"
            )
        self.widget_3d.show()
        self.show_buttons()
        self.show_colors()
        """
        self.hide_window_title()
        self.hide_manually_button()

        if self.white_widget is None:
            self.white_widget = PygameWidget(self.centralWidget)
            self.white_widget.setGeometry(10, 10, 580, 500)
            self.white_widget.show()

        self.show_buttons()
        self.show_colors()

    def show_buttons(self):

        self.show_Window_title(False)

        # list of buttons

        iteration = 2
        for name in self.MOVES:
            icon = QIcon("C:/Users/sabir/Desktop/rubik_solver/Images/{}.png".format(name))
            button = QPushButton(icon, "   Rotate the cube to {}".format(name), self)
            button.setGeometry(650, 100 * iteration, 500, 50)
            button.setStyleSheet(
                "QPushButton {"

                "   color: #081B2A;"
                "   font-size: 16px;"
                "   font-weight: bold;"
                "}"
                "QPushButton:hover {"
                "   background-color: #1a5ebd;"
                "   color: white;;"
                "}"
            )

            iteration += 1
            self.list_buttons.append(button)

        for button in self.list_buttons:  button.show()

    def show_colors(self):
        title_color = QLabel("Choose the \n color:", self)
        title_color.setGeometry(10, 520, 100, 50)

        # add a shadow effect to the title label
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setOffset(0, 0)
        title_color.setGraphicsEffect(shadow)

        font = QFont()
        font.setPointSize(10)
        font.setFamily("Gabriola")
        font.setBold(True)

        title_color.setFont(font)
        title_color.setAlignment(Qt.AlignCenter)
        title_color.setStyleSheet("color: #a3f9ff;")

        """
        

        title_color.show()"""
        button = QPushButton("Fill in the face", self)
        button.setGeometry(200, 535, 200, 40)
        button.setStyleSheet(
            "QPushButton {"
            "   color: #000000;"
            "   font-size: 12px;"
            "   font-weight: bold;"
            "}"
            "QPushButton:hover {"
            "   background-color: #{color};"
            "   color: white;"
            "}"
        )
        button.show()
        button.clicked.connect(self.open_window)

    def open_window(self):
        # Créer une nouvelle fenêtre
        #window = MyWindow(self)
        #window.show()
        # Instanciez une nouvelle fenêtre (FenetreNonModale)
        self.fenetre_non_modale = FillingFace(self)
        self.fenetre_non_modale.show()
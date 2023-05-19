from PySide2.QtGui import *
from PySide2.QtWidgets import *

class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the window title
        self.setWindowTitle("Rubik's cube solver")
        # set a fixed size to the window
        self.setFixedSize(1200, 600)
        # add the app's icon
        self.setWindowIcon(QIcon("Images/logo.png"))

        # create a centralWidget
        self.centralWidget = QWidget(self)
        self.centralWidget.setFixedSize(1200, 600)

        self.centralWidget.setStyleSheet("""background-image: url(Images/background.jpg);
                            background-size: cover;
                            background-repeat: no-repeat;
                           """)
        
        self.setCentralWidget(self.centralWidget)

        self.show_Window_title()
        self.show_help_button1()
        self.show_manualy_button()

        self.rubik_3D = QWidget(self)
        self.rubik_3D.hide()
        
        self.white_widget = None
        self.list_buttons = []

    def show_Window_title(self):
        # create a label for the title text
        self.titleLabel = QLabel("Rubik's Cube Solver", self)
        self.titleLabel.setGeometry(0, 150, 1200, 200)

        # add a shadow effect to the title label
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setOffset(0, 0)
        self.titleLabel.setGraphicsEffect(shadow)

        font = QFont()
        font.setPointSize(100)
        font.setFamily("Gabriola")
        font.setBold(True)

        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setStyleSheet("color: #a3f9ff;")

    def hide_window_title(self):
        self.titleLabel.hide()

    def show_help_button1(self):
        # Create a button
        self.help_button1 = QPushButton("Help!", self)

        # Set the button position and size
        self.help_button1.setGeometry(1100, 20, 80, 25)

         # Set the button style using CSS
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
        # create a new dialog window
        help_dialog = QDialog(self)
        help_dialog.setWindowTitle("Help")
        help_dialog.setModal(True)

        # add some text to the dialog
        help_label = QLabel("This is some help text. Click the close button to close this window.")
        help_layout = QVBoxLayout()
        help_layout.addWidget(help_label)
        help_dialog.setLayout(help_layout)

        # display the dialog window
        help_dialog.exec_()

    def show_white_widget(self):
        self.hide_window_title()
        self.hide_manually_button()
        if self.white_widget is None:
            self.widget_3d = QLabel(self)
            self.widget_3d.setGeometry(10, 10, 580, 580)
            self.widget_3d.setStyleSheet(
            "   background-color: white;" 
            "   border-radius: 10px;"
            )

            #pixmap = QPixmap(200, 200)
            #pixmap.fill(Qt.white)
            #self.white_widget.setPixmap(pixmap)
        
        self.widget_3d.show()
        self.show_buttons()
    
    def show_buttons(self):

        self.buttonLabel = QLabel("Rotate the cube.", self)
        self.buttonLabel.setGeometry(610, 80, 580, 50)

        # add a shadow effect to the title label
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setOffset(0, 0)
        self.buttonLabel.setGraphicsEffect(shadow)

        font = QFont()
        font.setPointSize(40)
        font.setFamily("Gabriola")
        font.setBold(True)

        self.buttonLabel.setFont(font)
        self.buttonLabel.setAlignment(Qt.AlignCenter)
        self.buttonLabel.setStyleSheet("color: #a3f9ff;")
        self.buttonLabel.show()

        # list of buttons
    
        iteration = 2
        for name in ["up", "down", "right", "left"]:
            icon = QIcon("Images/{}.png".format(name))
            button = QPushButton(icon, "   Rotate the cube to {}".format(name), self)
            # Set the button position and size
            button.setGeometry(650, 100 * iteration, 500, 50)
             # Set the button style using CSS
            button.setStyleSheet(
                "QPushButton {"
                
                "   color: #081B2A;"
                "   font-size: 16px;"
                "   font-weight: bold;"
                #"   border-radius: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: #1a5ebd;"
                "   color: white;;"
                "}"
            )

            iteration += 1
            self.list_buttons.append(button)

        for button in self.list_buttons:  button.show()
        


        
        

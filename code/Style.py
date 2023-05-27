from PySide2.QtGui import *
from PySide2.QtWidgets import *

def set_title_style(title, geometry, font_size):
    title.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])
    # add a shadow effect to the title label
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(30)
    shadow.setColor(QColor(0, 0, 0, 100))
    shadow.setOffset(0, 0)
    title.setGraphicsEffect(shadow)

    font = QFont()
    font.setPointSize(font_size)
    font.setFamily("Gabriola")
    font.setBold(True)

    title.setFont(font)
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet("color: #a3f9ff;")
    
def hide(element):
    element.hide()

from PySide2.QtWidgets import *
from OpenGL.GL import *
from OpenGL.GLU import *

class PygameWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(580, 500)

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, (0.5, 0.5, 1.0, 0.0))
        glEnable(GL_COLOR_MATERIAL)

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(width) / float(height), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-0.75, -0.25, -5.0)
        glRotatef(30, 1.0, 0.0, 0.0)
        glRotatef(30, 0.0, 1.0, 0.0)
        draw_cube()

def draw_cube():
    vertices = [
        [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # Face inférieure
        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]   # Face supérieure
    ]
    faces = [
        [0, 1, 2, 3],  # Face inférieure
        [4, 5, 6, 7],  # Face supérieure
        [0, 1, 5, 4],  # Face arrière
        [1, 2, 6, 5],  # Face droite
        [2, 3, 7, 6],  # Face avant
        [3, 0, 4, 7]   # Face gauche
    ]

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    for face in faces:
        for vertex in face:
            x, y, z = vertices[vertex]
            glVertex3f(x, y, z)
    glEnd()

    # Ajouter des lignes pour diviser le cube en deux
    glColor3f(0.0, 1.0, 0.0)  # Couleur des lignes (blanc)
    glDisable(GL_LINE_STIPPLE)
    glBegin(GL_LINES)
    glVertex3f(0.5, 0, 0)  # Ligne verticale au milieu de la face inférieure
    glVertex3f(0.5, 1, 0)
    glEnd()
    glDisable(GL_LINE_STIPPLE)
    glBegin(GL_LINES)
    glVertex3f(0.5, 0, 1)  # Ligne verticale au milieu de la face supérieure
    glVertex3f(0.5, 1, 1)
    glEnd()

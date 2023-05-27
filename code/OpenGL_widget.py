from PySide2.QtWidgets import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

class Cube:
    def __init__(self, color, translation):
        self.vertices = [
            [0, 0, 0], [1 / 3, 0, 0], [1 / 3, 1 / 3, 0], [0, 1 / 3, 0],  # Face inférieure
            [0, 0, 1 / 3], [1 / 3, 0, 1 / 3], [1 / 3, 1 / 3, 1 / 3], [0, 1 / 3, 1 / 3]   # Face supérieure
        ]

        self.faces = [
            [0, 1, 2, 3],  # Face inférieure
            [4, 5, 6, 7],  # Face supérieure
            [0, 1, 5, 4],  # Face arrière
            [1, 2, 6, 5],  # Face droite
            [2, 3, 7, 6],  # Face avant
            [3, 0, 4, 7]   # Face gauche
        ]

        self.color = color
        self.translation = translation

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
        glTranslatef(self.translation[0], self.translation[1], self.translation[2])
        glRotatef(30, 1.0, 0.0, 0.0)
        glRotatef(30, 0.0, 1.0, 0.0)
        self.draw_cube()

    def draw_cube(self):

        glBegin(GL_QUADS)
        for face in self.faces:
            glColor3f(* self.color)
            for vertex in face:
                x, y, z = self.vertices[vertex]
                glVertex3f(x, y, z)
        glEnd()

class PygameWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(580, 500)

        self.rotation_speed = 90.0  # Vitesse de rotation en degrés par seconde
        self.last_time = pygame.time.get_ticks()
        
        self.colors = [
            [1.0, 1.0, 1.0], # white
            [1.0, 1.0, 0.0], # Yellow
            [1.0, 0.0, 0.0], # Red
            [1.0, 0.5, 0.0], # Orange
            [0.0, 0.0, 1.0], # Blue
            [0.0, 1.0, 0.0] # Green
        ]

        self.list_cube = []

        index = 0    
        l = [-1 / 3, 0, 1 / 3]
        for x in l:
            for y in [0]:
                self.list_cube.append(Cube(self.colors[index], [x, y, 0]))
                index += 1
        

    def initializeGL(self):
        for cube in self.list_cube:
            cube.initializeGL()

    def resizeGL(self, width, height):
        for cube in self.list_cube:
            cube.resizeGL(width, height)

    def paintGL(self):
        for cube in self.list_cube:
            cube.paintGL()

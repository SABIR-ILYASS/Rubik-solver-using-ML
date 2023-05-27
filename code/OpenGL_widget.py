from PySide2.QtWidgets import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

from cube import Cube

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
        l = [-1/3, 0, 1/3]
        for x in l:
            for y in l:
                for z in l:
                    self.list_cube.append(Cube(self.colors[index % 6], [x, y, z]))
                    index += 1
        

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
        glTranslatef(0, -0.25, -5.0)
        glRotatef(30, 1.0, 0.0, 0.0)
        glRotatef(30, 0.0, 1.0, 0.0)

        
        for cube in self.list_cube:
            glPushMatrix()
            glTranslatef(*cube.translation)
            cube.draw_cube()
            glPopMatrix()
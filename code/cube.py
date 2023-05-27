from pygame.locals import *
from PySide2.QtWidgets import *
from OpenGL.GL import *
from OpenGL.GLU import *


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

    def draw_cube(self):

        glBegin(GL_QUADS)
        for face in self.faces:
            glColor3f(* self.color)
            for vertex in face:
                x, y, z = self.vertices[vertex]
                glVertex3f(x, y, z)
        glEnd()

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Coordonnées des sommets du cube
vertices = [
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # Face inférieure
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]   # Face supérieure
]

# Faces du cube (indices des sommets)
faces = [
    [0, 1, 2, 3],  # Face inférieure
    [4, 5, 6, 7],  # Face supérieure
    [0, 1, 5, 4],  # Face arrière
    [1, 2, 6, 5],  # Face droite
    [2, 3, 7, 6],  # Face avant
    [3, 0, 4, 7]   # Face gauche
]

def draw_cube():
    glBegin(GL_QUADS)

    # Tracer les faces du cube
    for face in faces:
        for vertex in face:
            x, y, z = vertices[vertex]
            glVertex3f(x, y, z)

    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from object import Object

from OpenGL.GL import *
import numpy as np

class Boat(Object):
    def __init__(self, program):
        super().__init__(program, None)

    def create(self):
        vertices = np.zeros(11, [("position", np.float32, 2)])
        vertices['position'] = [
            # Casco
            (-0.78, -0.89),
            (-0.84, -0.76),
            (-0.40, -0.76),
            (-0.46, -0.89),

            # Vela
            (-0.62, -0.75),
            (-0.88, -0.75),
            (-0.62, -0.56),

            # Mastro
            (-0.62, -0.76),
            (-0.62, -0.56),
            (-0.58, -0.76),
            (-0.58, -0.56),
        ]
        return vertices

    def draw(self):
        glBindVertexArray(self.vao)
        glUniformMatrix4fv(glGetUniformLocation(self.program, "mat_transformation"), 1, GL_TRUE, self.mat_transformation)
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.0, 0.0, 0.5, 1.0)
        glDrawArrays(GL_QUADS, 0, 4)
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.7, 0.2, 0.2, 1.0)
        glDrawArrays(GL_TRIANGLE_STRIP, 4, 3)
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.2, 0.3, 0.3, 1.0)
        glDrawArrays(GL_TRIANGLE_STRIP, 7, 4)
        glBindVertexArray(0)

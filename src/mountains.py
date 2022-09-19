#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from object import Object, Color

import numpy as np
from OpenGL.GL import *

class Mountains(Object):
    def __init__(self, program):
        super().__init__(program, Color(0.627, 0.322, 0.176))

    def create(self):
        vertices = np.zeros(21, [("position", np.float32, 2)])
        vertices['position'] = [
            (-0.20, 0.20),
            (0.03, 0.50),
            (0.20, 0.20),

            (-0.05, 0.20),
            (-0.38, 0.45),
            (-0.60, 0.20),

            (-0.90, 0.20),
            (-0.65, 0.38),
            (-0.50, 0.20),

            (-1.30, 0.20),
            (-0.98, 0.35),
            (-0.75, 0.20),

            (0.56, 0.20),
            (0.38, 0.40),
            (0.10, 0.20),

            (0.82, 0.20),
            (0.67, 0.40),
            (0.43, 0.20),

            (1.3, 0.20),
            (0.89, 0.40),
            (0.71, 0.20),
        ]
        return vertices

    def draw(self):
        glBindVertexArray(self.vao)
        glUniform4f(glGetUniformLocation(self.program, "color"), self.color.R - 0.1, self.color.G, self.color.B, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 0, 3)
        glUniform4f(glGetUniformLocation(self.program, "color"), self.color.R, self.color.G, self.color.B, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 3, 3)
        glDrawArrays(GL_TRIANGLE_FAN, 6, 3)
        glDrawArrays(GL_TRIANGLE_FAN, 9, 3)
        glUniform4f(glGetUniformLocation(self.program, "color"), self.color.R + 0.1, self.color.G, self.color.B, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 12, 3)
        glDrawArrays(GL_TRIANGLE_FAN, 15, 3)
        glDrawArrays(GL_TRIANGLE_FAN, 18, 3)
        glBindVertexArray(0)

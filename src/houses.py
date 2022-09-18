from object import Object

from OpenGL.GL import *
import numpy as np

class House(Object):
    def __init__(self, program):
        super().__init__(program, None)

    def create(self):
        vertices = np.zeros(20, [("position", np.float32, 2)])
        vertices['position'] = [
            # Main Body
            (-0.91, -0.32),
            (-0.91, -0.04),
            (-0.63, -0.04),
            (-0.63, -0.32),

            # Roof
            (-0.95, -0.04),
            (-0.91, 0.10),
            (-0.63, 0.10),
            (-0.59, -0.04),

            # Door
            (-0.81, -0.09),
            (-0.81, -0.32),
            (-0.73, -0.32),
            (-0.73, -0.09),

            # Window 1
            (-0.89, -0.08),
            (-0.89, -0.20),
            (-0.82, -0.20),
            (-0.82, -0.08),

            # Window 2
            (-0.72, -0.08),
            (-0.72, -0.20),
            (-0.65, -0.20),
            (-0.65, -0.08),
        ]
        return vertices

    def draw(self):
        glBindVertexArray(self.vao)
        glUniform4f(glGetUniformLocation(self.program, "color"), 1.0, 0.14, 0.0, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 0, 4)
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.38, 0.19, 0.0, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 4, 4)
        glDrawArrays(GL_TRIANGLE_FAN, 8, 4)
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.0, 0.31, 0.31, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 12, 4)
        glDrawArrays(GL_TRIANGLE_FAN, 16, 4)
        glBindVertexArray(0)

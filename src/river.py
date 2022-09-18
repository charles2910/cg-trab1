from utilities import Color

from OpenGL.GL import *
import numpy as np

class River:
    def __init__(self, program):
        self.program = program
        self.color = Color(0.255, 0.412, 0.882)
        self.vertices = np.zeros(4, [("position", np.float32, 2)])
        self.vao = None

    def prepare(self):
        self.vertices['position'] = [
            (-1.0, -1.0),
            (-1.0, -0.5),
            (1.0, -0.1),
            (1.0, -1.0),
        ]

        self.vao = glGenVertexArrays(1)
        buffer = glGenBuffers(1)
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, buffer)

        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_DYNAMIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, buffer)

        stride = self.vertices.strides[0]

        loc = glGetAttribLocation(self.program, "position")
        glEnableVertexAttribArray(loc)

        glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, ctypes.c_void_p(0))
        glBindVertexArray(0)

    def draw(self):
        glBindVertexArray(self.vao)
        glUniform4f(glGetUniformLocation(self.program, "color"), self.color.R, self.color.G, self.color.B, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 0, len(self.vertices))
        glBindVertexArray(0)

from utilities import Coordinates, Color

from OpenGL.GL import *
import numpy as np
import math

class Circle:
    def __init__(self, program, coordinates: Coordinates, radius, color: Color):
        self.num_vertices = 200
        self.vertices = np.zeros(self.num_vertices, [("position", np.float32, 2)])
        self.program = program
        self.radius = radius
        self.color = color
        self.coordinates = coordinates

    def prepare(self):
        self.loc_color = glGetUniformLocation(self.program, "color")

        for i in range(self.num_vertices):
            angle = (2 * i * math.pi) / 25
            x = self.coordinates.x + (self.radius - .07) * math.cos(angle)
            y = self.coordinates.y + self.radius * math.sin(angle)
            self.vertices[i] = [x, y]

        buffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, buffer)

        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_DYNAMIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, buffer)

        stride = self.vertices.strides[0]

        loc = glGetAttribLocation(self.program, "position")
        glEnableVertexAttribArray(loc)

        glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, ctypes.c_void_p(0))

    def draw(self):
        glDrawArrays(GL_TRIANGLE_FAN, 0, len(self.vertices))
        glUniform4f(self.loc_color, self.color.R, self.color.G, self.color.B, 1.0)

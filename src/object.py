#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from abc import abstractmethod
import numpy as np
from OpenGL.GL import *

class Coordinates:
    """
        A class used to represent a cartesian coordinate

        ...

        Attributes
        ----------
        x : float
        x coordinate that varies from -1 to 1
        y : float
        y coordinate that varies from -1 to 1
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Color:
    """
        A class used to represent a RGB color

        ...

        Attributes
        ----------
        R : float
        red parameter that varies from 0 to 1
        B : float
        blue parameter that varies from 0 to 1
        G : float
        green parameter that varies from 0 to 1
    """

    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

class Object:
    def __init__(self, program, color: Color):
        self.program = program
        self.color = color
        self.vao = None
        self.mat_transformation = np.array([1.0, 0.0, 0.0, 0.0,
                                            0.0, 1.0, 0.0, 0.0,
                                            0.0, 0.0, 1.0, 0.0,
                                            0.0, 0.0, 0.0, 1.0], np.float32)

    @abstractmethod
    def create(self):
        pass

    def prepare(self):
        self.vertices = self.create()

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
        glUniformMatrix4fv(glGetUniformLocation(self.program, "mat_transformation"), 1, GL_TRUE, self.mat_transformation)
        glUniform4f(glGetUniformLocation(self.program, "color"), self.color.R, self.color.G, self.color.B, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 0, len(self.vertices))
        glBindVertexArray(0)

#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from object import Object

from OpenGL.GL import *
import numpy as np

class Windmill(Object):
    """
        A class used to represent the windmill. Child of class Object.

        ...

        Attributes
        ----------
        program : class 'ctypes.c_uint'
        an object to which the shader objects will be attached
    """
    def __init__(self, program):
        super().__init__(program, None)

    def create(self):
        '''Define the vertex of the windmill'''
        vertices = np.zeros(22, [("position", np.float32, 2)])
        vertices['position'] = [
            # Main Body
            (-0.50, -0.10),
            (-0.10, -0.10),
            (-0.20,  0.40),
            (-0.40,  0.40),

            # Roof
            (-0.45,  0.40),
            (-0.40,  0.50),
            (-0.33,  0.54),
            (-0.27,  0.54),
            (-0.20,  0.50),
            (-0.15,  0.40),

            # Door
            (-0.34, -0.10),
            (-0.34,  0.00),
            (-0.26,  0.00),
            (-0.26, -0.10),

            # Window 1
            (-0.32,  0.10),
            (-0.28,  0.10),
            (-0.28,  0.18),
            (-0.32,  0.18),

            # Window 2
            (-0.32,  0.33),
            (-0.28,  0.33),
            (-0.28,  0.25),
            (-0.32,  0.25),
        ]
        return vertices

    def draw(self):
        '''Draw the windmill in the window with the proper colors'''
        glBindVertexArray(self.vao)
        glUniformMatrix4fv(glGetUniformLocation(self.program, "mat_transformation"), 1, GL_TRUE, self.mat_transformation)

        # Color and draw the main body
        glUniform4f(glGetUniformLocation(self.program, "color"), 1.0, 0.14, 0.0, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 0, 4)
        # Color and draw the roof and the door
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.38, 0.19, 0.0, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 4, 6)
        glDrawArrays(GL_TRIANGLE_FAN, 10, 4)
        # Color and draw the windows
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.0, 0.31, 0.31, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 14, 4)
        glDrawArrays(GL_TRIANGLE_FAN, 18, 4)

        glBindVertexArray(0)
#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from object import Object, Coordinates

from OpenGL.GL import *
import numpy as np

class Boat(Object):
    """
        A class used to represent the boat. Child of class Object.

        ...

        Attributes
        ----------
        program : class 'ctypes.c_uint'
        an object to which the shader objects will be attached
    """
    def __init__(self, program, coord: Coordinates):
        super().__init__(program, None)
        self.coordinates = coord
        self.mat_transformation = np.array([1.0, 0.0, 0.0, self.coordinates.x,
                                            0.0, 1.0, 0.0, self.coordinates.y,
                                            0.0, 0.0, 1.0, 0.0,
                                            0.0, 0.0, 0.0, 1.0], np.float32)
        self.obj_scale = 1.0

    def create(self):
        '''Define the vertex of the boat'''
        vertices = np.zeros(11, [("position", np.float32, 2)])
        vertices['position'] = [
            # Hull
            (-0.16, -0.12),
            (-0.22,  0.00),
            ( 0.22,  0.00),
            ( 0.16, -0.12),

            # Sail
            ( 0.00,  0.02),
            (-0.26,  0.02),
            ( 0.00,  0.20),

            # Mast
            ( 0.00,  0.00),
            ( 0.00,  0.20),
            ( 0.04,  0.00),
            ( 0.04,  0.20),
        ]
        return vertices

    def draw(self):
        '''Draw the boat in the window with the proper colors'''
        glBindVertexArray(self.vao)
        glUniformMatrix4fv(glGetUniformLocation(self.program, "mat_transformation"), 1, GL_TRUE, self.mat_transformation)

        # Color and draw the hull
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.0, 0.0, 0.5, 1.0)
        glDrawArrays(GL_QUADS, 0, 4)
        # Color and draw the sail
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.7, 0.2, 0.2, 1.0)
        glDrawArrays(GL_TRIANGLE_STRIP, 4, 3)
        # Color and draw the mast
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.2, 0.3, 0.3, 1.0)
        glDrawArrays(GL_TRIANGLE_STRIP, 7, 4)

        glBindVertexArray(0)

    def translate(self, t_x, t_y):
        '''Returns a translation matrix with offset (t_x, t_y)'''
        self.coordinates.x += t_x
        self.coordinates.y += t_y

        if self.coordinates.x > 1:
            self.coordinates.x -= 2
        elif self.coordinates.x < -1:
            self.coordinates.x += 2
        if self.coordinates.y > 1:
            self.coordinates.y -= 2
        elif self.coordinates.y < -1:
            self.coordinates.y = -1

        self.mat_transformation = np.array([
            1.0, 0.0, 0.0, self.coordinates.x,
            0.0, 1.0, 0.0, self.coordinates.y,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0],
            np.float32)

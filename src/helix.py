#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from object import Object, Color, Coordinates

from OpenGL.GL import *
import numpy as np
import math


class Helix(Object):
    """
        A class used to represent a cloud. Child of class Object.

        ...

        Attributes
        ----------
        program : class 'ctypes.c_uint'
        an object to which the shader objects will be attached

        translate_x : float
        offset in the x axis relative to the original position of the cloud
    """
    def __init__(self, program, coord: Coordinates):
        super().__init__(program, None)
        self.coordinates = coord
        self.mat_transformation = np.array([1.0, 0.0, 0.0, self.coordinates.x,
                                            0.0, 1.0, 0.0, self.coordinates.y,
                                            0.0, 0.0, 1.0, 0.0,
                                            0.0, 0.0, 0.0, 1.0], np.float32)
        self.angle = 0.0

    def create(self):
        '''Define the vertices for the helix'''
        vertices = np.zeros(16, [("position", np.float32, 2)])
        vertices['position'] = [
            # Pá 1
            (-0.02,  0.00),
            ( 0.02,  0.05),
            ( 0.02, -0.20),
            (-0.02, -0.20),

            # Pá 2
            ( 0.00, -0.02),
            ( 0.00,  0.02),
            (-0.20,  0.02),
            (-0.20, -0.02),

            # Pá 3
            ( 0.02,  0.00),
            ( 0.02,  0.20),
            (-0.02,  0.20),
            (-0.02,  0.00),

            # Pá 4
            ( 0.00, -0.02),
            ( 0.20, -0.02),
            ( 0.20,  0.02),
            ( 0.00,  0.02),
        ]
        return vertices

    def draw(self):
        '''Draw the boat in the window with the proper colors'''
        glBindVertexArray(self.vao)
        glUniformMatrix4fv(glGetUniformLocation(self.program, "mat_transformation"), 1, GL_TRUE, self.mat_transformation)

        # Color and draw the hull
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.3, 0.3, 0.3, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 0, 4)
        glDrawArrays(GL_TRIANGLE_FAN, 4, 4)
        glDrawArrays(GL_TRIANGLE_FAN, 8, 4)
        glDrawArrays(GL_TRIANGLE_FAN, 12, 4)

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
            self.coordinates.y += 2
        self.mat_transformation = np.array([
            1.0, 0.0, 0.0, self.coordinates.x,
            0.0, 1.0, 0.0, self.coordinates.y,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0],
            np.float32)

    def rotate(self, ang):
        '''Returns a rotation matrix with angle ang'''
        self.angle += ang
        self.mat_transformation = np.array([
            np.cos(self.angle),
            -np.sin(self.angle),
            0.0,
            self.coordinates.x * (1 - np.cos(ang)) + self.coordinates.y * np.sin(ang),

            np.sin(self.angle),
            np.cos(self.angle),
            0.0,
            self.coordinates.y * (1 - np.cos(ang)) - self.coordinates.x * np.sin(ang),

            0.0,
            0.0,
            1.0,
            0.0,

            0.0,
            0.0,
            0.0,
            1.0],
            np.float32)
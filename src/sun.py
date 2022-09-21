#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from circle import Circle
from object import Color, Coordinates
import numpy as np

class Sun(Circle):
    """
        A class used to represent the sun. Child of class Circle.

        ...

        Attributes
        ----------
        program : class 'ctypes.c_uint'
        an object to which the shader objects will be attached
    """
    # Defines the custom coordinates, radius and color of the sun
    def __init__(self, program, coord = Coordinates(-0.25, 0.75), obj_scale = 1.0, obj_rotation = 0.0, color = Color(1.0, 0.843, 0)):
        super().__init__(program, 0.18, coord, obj_scale, obj_rotation, color)

    def scale(self, s_x, s_y):
        '''Change a scaling matrix with factor (s_x, s_y)'''
        self.obj_scale += s_x
        if self.obj_scale < 0.0:
            self.obj_scale = 0.00
        mat_scale = np.array([
            [self.obj_scale, 0.0,            0.0, self.coordinates.x * (1.0 - self.obj_scale)],
            [0.0,            self.obj_scale, 0.0, self.coordinates.y * (1.0 - self.obj_scale)],
            [0.0,            0.0,            1.0, 0.0],
            [0.0,            0.0,            0.0, 1.0]],
            np.float32)
        self.mat_transformation = mat_scale
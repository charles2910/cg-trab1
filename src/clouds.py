#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from object import Object, Color, Coordinates
from circle import Circle

import numpy as np

class Cloud(Object):
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
    def __init__(self, program, translate_x, coord = Coordinates(0.0, 0.0), obj_scale = 1.0, obj_rotation = 0.0, color = Color(1.0, 1.0, 1.0)):
        super().__init__(program, coord, obj_scale, obj_rotation, color)
        self.t_x = translate_x

        # A cloud is a composition of 4 circles
        self.circles = [
            Circle(program, 0.15, Coordinates(-0.85, 0.77), Color(0.80, 0.80, 0.80)),
            Circle(program, 0.15, Coordinates(-0.79, 0.70), Color(0.80, 0.80, 0.80)),
            Circle(program, 0.15, Coordinates(-0.70, 0.70), Color(0.80, 0.80, 0.80)),
            Circle(program, 0.15, Coordinates(-0.75, 0.77), Color(0.80, 0.80, 0.80))
        ]

    def create(self):
        '''Define the vertices for each of the circles'''
        for circle in self.circles:
            circle.create()

    def prepare(self):
        '''Prepare the vertices information for each of the circles'''
        for circle in self.circles:
            circle.prepare()

    def draw(self):
        '''Draw each of the circles applying the translation matrix'''
        for circle in self.circles:
            circle.translate(self.t_x, 0.0)
            circle.draw()

#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from circle import Circle
from object import Color, Coordinates

class Sun(Circle):
    """
        A class used to represent the sun. Child of class Circle.

        ...

        Attributes
        ----------
        program : class 'ctypes.c_uint'
        an object to which the shader objects will be attached
    """
    def __init__(self, program):
        # Defines the coordinates, radius and color of the sun
        super().__init__(program, Coordinates(-0.25, 0.75), 0.18, Color(1.0, 0.843, 0))

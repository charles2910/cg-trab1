#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from object import Object, Color

from OpenGL.GL import *
import numpy as np
import math

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle(Object):
    def __init__(self, program, coordinates: Coordinates, radius, color: Color):
        super().__init__(program, color)
        self.num_vertices = 200
        self.radius = radius
        self.coordinates = coordinates

    def create(self):
        vertices = np.zeros(self.num_vertices, [("position", np.float32, 2)])

        for i in range(self.num_vertices):
            angle = (2 * i * math.pi) / 25
            x = self.coordinates.x + (self.radius - .07) * math.cos(angle)
            y = self.coordinates.y + self.radius * math.sin(angle)
            vertices[i] = [x, y]

        return vertices

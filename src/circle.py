from utilities import Coordinates, Color
from object import Object

from OpenGL.GL import *
import numpy as np
import math

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

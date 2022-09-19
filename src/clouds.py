#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from object import Object, Color
from circle import Circle, Coordinates

class Cloud(Object):
    def __init__(self, program, translate_x):
        super().__init__(program, None)
        self.circles = [
            Circle(program, Coordinates(-0.85 + translate_x, 0.77), 0.15, Color(0.80, 0.80, 0.80)),
            Circle(program, Coordinates(-0.79 + translate_x, 0.70), 0.15, Color(0.80, 0.80, 0.80)),
            Circle(program, Coordinates(-0.70 + translate_x, 0.70), 0.15, Color(0.80, 0.80, 0.80)),
            Circle(program, Coordinates(-0.75 + translate_x, 0.77), 0.15, Color(0.80, 0.80, 0.80))
        ]

    def create(self):
        for circle in self.circles:
            circle.create()

    def prepare(self):
        for circle in self.circles:
            circle.prepare()

    def draw(self):
        for circle in self.circles:
            circle.draw()

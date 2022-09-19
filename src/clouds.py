from utilities import Color, Coordinates
from object import Object
from circle import Circle

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

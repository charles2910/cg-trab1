from geometries import Circle, Color, Coordinates

class Sun(Circle):
    def __init__(self, program):
        super().__init__(program, Coordinates(-0.25, 0.75), 0.18, Color(1.0, 0.843, 0))

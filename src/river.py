from utilities import Color
from object import Object

import numpy as np

class River(Object):
    def __init__(self, program):
        super().__init__(program, Color(0.255, 0.412, 0.882))

    def create(self):
        vertices = np.zeros(4, [("position", np.float32, 2)])
        vertices['position'] = [
            (-1.0, -1.0),
            (-1.0, -0.5),
            (1.0, -0.1),
            (1.0, -1.0),
        ]
        return vertices

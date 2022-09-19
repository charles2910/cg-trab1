#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from object import Object, Color

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

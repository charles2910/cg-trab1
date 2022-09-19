#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from circle import Circle, Coordinates
from object import Color

class Sun(Circle):
    def __init__(self, program):
        super().__init__(program, Coordinates(-0.25, 0.75), 0.18, Color(1.0, 0.843, 0))

#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from houses import RedHouse, GreenHouse
from mountains import Mountains
from sun import Sun
from field import Field
from river import River
from tree import ScotchPineTree, SugarPineTree
from boat import Boat
from clouds import Cloud

class Scene:
    """
        A class used to group all objects in the scene.

        ...

        Attributes
        ----------
        program : class 'ctypes.c_uint'
        an object to which the shader objects will be attached
    """
    def __init__(self, program):
        # List of all the objects in the scene
        self.objects = [
            Sun(program),
            River(program),
            Field(program),
            Mountains(program),
            RedHouse(program),
            GreenHouse(program),
            SugarPineTree(program),
            ScotchPineTree(program),
            Boat(program),
            Cloud(program, 0),
            Cloud(program, 1.1),
            Cloud(program, 1.5)
        ]

    def prepare(self):
        '''Prepare all the objects in the scene'''
        for object in self.objects:
            object.prepare()

    def draw(self):
        '''Draw all the objects in the scene'''
        for object in self.objects:
            object.draw()

from houses import RedHouse, GreenHouse
from mountains import Mountains
from sun import Sun
from field import Field
from river import River
from tree import ScotchPineTree, SugarPineTree
from boat import Boat
from clouds import Cloud

class Scene:
    def __init__(self, program):
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
        for object in self.objects:
            object.prepare()

    def draw(self):
        for object in self.objects:
            object.draw()

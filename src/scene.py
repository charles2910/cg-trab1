from houses import RedHouse, GreenHouse
from mountains import Mountains
from sun import Sun
from field import Field
from river import River
from tree import ScotchPineTree, SugarPineTree

class Scene:
    def __init__(self, program):
        self.sun = Sun(program)
        self.river = River(program)
        self.field = Field(program)
        self.mountains = Mountains(program)
        self.redHouse = RedHouse(program)
        self.yellowHouse = GreenHouse(program)
        self.tree1 = SugarPineTree(program)
        self.tree2 = ScotchPineTree(program)

    def prepare(self):
        self.sun.prepare()
        self.river.prepare()
        self.field.prepare()
        self.mountains.prepare()
        self.redHouse.prepare()
        self.yellowHouse.prepare()
        self.tree1.prepare()
        self.tree2.prepare()

    def draw(self):
        self.sun.draw()
        self.river.draw()
        self.field.draw()
        self.mountains.draw()
        self.redHouse.draw()
        self.yellowHouse.draw()
        self.tree1.draw()
        self.tree2.draw()

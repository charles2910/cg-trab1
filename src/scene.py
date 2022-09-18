from houses import RedHouse, GreenHouse
from sun import Sun
from field import Field
from river import River

class Scene:
    def __init__(self, program):
        self.sun = Sun(program)
        self.river = River(program)
        self.field = Field(program)
        self.redHouse = RedHouse(program)
        self.yellowHouse = GreenHouse(program)

    def prepare(self):
        self.sun.prepare()
        self.river.prepare()
        self.field.prepare()
        self.redHouse.prepare()
        self.yellowHouse.prepare()

    def draw(self):
        self.sun.draw()
        self.river.draw()
        self.field.draw()
        self.redHouse.draw()
        self.yellowHouse.draw()

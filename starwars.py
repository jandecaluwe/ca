from ca.base.generations import Generations
from ca.base.gui import play


class StarWars(Generations):
    states = 4
    def birth(self):
        return self.live_count == 2
    def survival(self):
        return self.live_count in (3, 4, 5)

play(StarWars)


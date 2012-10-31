from ca.base.generations import Generations
from ca.base.gui import play

class Spirals(Generations):
    states = 5
    def birth(self):
        return self.live_count in [2, 3, 4]
    def survival(self):
        return self.live_count in [2]

play(Spirals)

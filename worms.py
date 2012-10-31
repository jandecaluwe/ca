from ca.base.generations import Generations
from ca.base.gui import play

class Worms(Generations):
    states = 6
    def birth(self):
        return self.live_count in [2, 5]
    def survival(self):
        return self.live_count in [3, 4, 6, 7]

play(Worms)




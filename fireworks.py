from ca.base.generations import Generations
from ca.base.gui import play

class FireWorks(Generations):
    states= 21
    def birth(self):
        return self.live_count in [1, 3]
    def survival(self):
        return self.live_count in [2]

play(FireWorks)

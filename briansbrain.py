from ca.base.generations import Generations
from ca.base.gui import play


class BriansBrain(Generations):
    states = 3
    def birth(self):
        return self.live_count == 2
    def survival(self):
        return False

play(BriansBrain)


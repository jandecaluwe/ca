
from ca.base.life import Life
from ca.base.gui import play

class ConwaysLife(Life):
    def birth(self):
        return self.live_count in [3]
    def survival(self):
        return self.live_count in [2, 3]

play(ConwaysLife)


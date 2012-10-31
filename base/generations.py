class Generations(object):

    def __init__(self):
        self.age = self.next_age = 0
        self.neighbors = [None] * 8
        self.live_count = 0

    def count_live_neighbors(self):
        self.live_count = 0
        for n in self.neighbors:
            if n.age == 1:
                self.live_count += 1

    def calc_next_age(self):
        self.count_live_neighbors()
        if self.age == 0:
            if self.birth():
                self.next_age = 1
        elif self.age == 1 and self.survival():
            pass
        else:
             self.next_age = (self.age + 1) % self.states

    def step(self):
        self.age = self.next_age

    def make_older(self):
        self.age = self.next_age = (self.age + 1) % self.states

    def clear(self):
        self.age = self.next_age = 0


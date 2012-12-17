    def calc_next_age(self):
        self.count_live_neighbors()
        if self.age == 0:
            if self.birth():
                self.next_age = 1
        elif self.age == 1 and self.survival():
            pass
        else:
             self.next_age = (self.age + 1) % self.states

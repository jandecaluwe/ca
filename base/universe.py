class Universe(object):

    def __init__(self, cellType, rows=64, cols=64):
        self.grid = g = []
        self.rows = rows
        self.cols = cols
        for r in range(rows):
            row = [cellType() for c in range(cols)]
            g.append(row)
        for r in range(rows):
            N = (r - 1) % rows
            S = (r + 1) % rows
            for c in range(cols):
                W = (c - 1) % cols
                E = (c + 1) % cols
                n = [g[N][W], g[N][c], g[N][E], g[r][E],
                     g[S][E], g[S][c], g[S][W], g[r][W]]
                g[r][c].neighbors = n

    def step(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c].calc_next_age()
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c].step()

    def clear(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c].clear()


from Tkinter import *
import colorsys

from ca.base.universe import Universe

class CellGui(Label):
    
    def __init__(self, parent, cell, colormap):
        
        Label.__init__(self, parent, relief="raised", width=2, borderwidth=1)
        self.cell = cell
        self.colormap = colormap
        self.bind("<Button-1>", self.make_older)
        self.display()

    def make_older(self, event):
        self.cell.make_older()
        self.display()

    def display(self):
        self.config(bg=self.colormap[self.cell.age])


def tk_colormap(states, colorrange):
    colormap = [None] * states
    colormap[0] = "black"
    colormap[1] = "#%02x%02x%02x" % (255, 1, 1)
    if states > 2:
        step = colorrange / (states-2)
        for i in range(2, states):
            h = step * (i-1)
            r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
            r, g, b = int(r*255), int(g*255), int(b*255)
            colormap[i] = "#%02x%02x%02x" % (r, g, b)
    return colormap


class GridGUI(object):

    def __init__(self, parent, cellType, rows, cols, steps, colorrange=0.7):
        self.universe = universe = Universe(cellType, rows, cols)
        self.parent = parent
        self.rows = rows
        self.cols = cols
        self.steps = steps
        self.universe = universe = Universe(cellType, rows, cols)
        colormap = tk_colormap(cellType.states, colorrange)
        self.cells = []
        for r in range(rows):
            rowcells = []
            for c in range(cols):
                fr_cell = Frame(parent, width=10, height=10)
                fr_cell.pack_propagate(0)
                fr_cell.grid(row=r, column=c)
                cell = CellGui(fr_cell, universe.grid[r][c], colormap)
                cell.pack(fill=BOTH, expand=1)
                rowcells.append(cell)
            self.cells.append(rowcells)
        
    def step(self):
        self.universe.step()
        self.steps.set(self.steps.get() + 1)
        self.display()

    def clear(self):
        self.universe.clear()
        self.steps.set(0)
        self.display()

    def run(self):
        self.running = 1
        self.do_run()

    def do_run(self):
        self.step()
        if self.running:
            self.parent.after(50, self.do_run)

    def stop(self):
        self.running = 0

    def display(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.cells[r][c].display()
                  

def play(cellType, rows=48, cols=64):
    root = Tk()
    frame = Frame(root)
    frame.pack()
    steps = IntVar()
    grid = GridGUI(frame, cellType, rows, cols, steps)
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    buttonStep = Button(bottomFrame, text="Step", command=grid.step)
    buttonStep.pack(side=LEFT)
    buttonClear = Button(bottomFrame, text="Clear", command=grid.clear)
    buttonClear.pack(side=LEFT, after=buttonStep)
    buttonRun = Button(bottomFrame, text="Run", command=grid.run)
    buttonRun.pack(side=LEFT, after=buttonClear)
    buttonStop = Button(bottomFrame, text="Stop", command=grid.stop)
    buttonStop.pack(side=LEFT, after=buttonRun)
    labelSteps = Label(bottomFrame, textvariable=steps)
    labelSteps.pack(side=LEFT, after=buttonStop)
    root.mainloop()


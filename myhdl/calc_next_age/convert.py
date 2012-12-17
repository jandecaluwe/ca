from myhdl import *

from calc_next_age import calc_next_age

def convert():
                
    age_out = Signal(bool(0))
    live_count = Signal(intbv(0, min=0, max=9))
    step = Signal(bool(0))
    clock = Signal(bool(0))
    reset = ResetSignal(0, active=1, async=True)

    toVerilog(calc_next_age, age_out, live_count, step, clock, reset)
    toVHDL(calc_next_age, age_out, live_count, step, clock, reset)


convert()

from myhdl import *

def calc_next_age(
    age_out, 
    live_count,
    step, 
    clock,
    reset
):

    age = Signal(bool(0))

    @always_seq(clock.posedge, reset=reset)
    def seq():
        birth = (live_count == 3)
        survival = (live_count == 2) or (live_count == 3)
        if step:
            if age == 0 and birth:
                age.next = 1
            elif age == 1 and not survival:
                age.next = 0

    @always_comb
    def alias():
        age_out.next = age

    return seq, alias
                

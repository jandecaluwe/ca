from random import randrange

from myhdl import *

vectors = tuple([randrange(0, 9) for i in range(1000)])

from calc_next_age import calc_next_age

def tb():
                
    age_out = Signal(bool(0))
    live_count = Signal(intbv(0, min=0, max=9))
    step = Signal(bool(0))
    clock = Signal(bool(0))
    reset = ResetSignal(0, active=1, async=True)

    dut = calc_next_age(age_out, live_count, step, clock, reset)

    @instance
    def clockgen():
        reset.next = 0
        clock.next = 0
        yield delay(10)
        reset.next = 1
        yield delay(10)
        reset.next = 0
        while True:
            yield delay(10)
            clock.next = not clock
    
    @instance
    def check():
        expected_age = 0
        for i in range(len(vectors)):
            yield clock.negedge
            print age_out
            v = vectors[i]
            if age_out == 0 and v == 3:
                expected_age = 1
            if age_out == 1 and not (v == 2 or v == 3):
                expected_age = 0
            live_count.next = v
            step.next = 1
            yield clock.posedge
            yield delay(1)
            assert age_out == expected_age
        raise StopSimulation()

    return dut, clockgen, check
                    
sim = Simulation(tb())
sim.run()

toVerilog(tb)
toVHDL(tb)

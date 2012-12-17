module tb_calc_next_age;

wire age_out;
reg [3:0] live_count;
reg step;
reg clock;
reg reset;

initial begin
    $from_myhdl(
        live_count,
        step,
        clock,
        reset
    );
    $to_myhdl(
        age_out
    );
end

calc_next_age dut(
    age_out,
    live_count,
    step,
    clock,
    reset
);

endmodule

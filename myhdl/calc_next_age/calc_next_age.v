// File: calc_next_age.v
// Generated by MyHDL 0.8dev
// Date: Sun Dec 16 22:44:22 2012


`timescale 1ns/10ps

module calc_next_age (
    age_out,
    live_count,
    step,
    clock,
    reset
);


output age_out;
wire age_out;
input [3:0] live_count;
input step;
input clock;
input reset;

reg age;





always @(posedge clock, posedge reset) begin: CALC_NEXT_AGE_SEQ
    reg survival;
    reg birth;
    if (reset == 1) begin
        age <= 0;
    end
    else begin
        birth = (live_count == 3);
        survival = ((live_count == 2) || (live_count == 3));
        if (step) begin
            if (((age == 0) && birth)) begin
                age <= 1;
            end
            else if (((age == 1) && (!survival))) begin
                age <= 0;
            end
        end
    end
end



assign age_out = age;

endmodule
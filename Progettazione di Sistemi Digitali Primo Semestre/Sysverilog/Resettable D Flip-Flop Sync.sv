module resettable_ff_sync(
input logic d, clk, r,
output logic q);

always_ff @(posedge clk)
    if (r) // r == 1
    q <= 1'b0;
    else
    q <= d;
endmodule
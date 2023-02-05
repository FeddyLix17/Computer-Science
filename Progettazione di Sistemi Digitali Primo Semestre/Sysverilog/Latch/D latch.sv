module d_latch (
    input logic clk, d,
    output logic q, q_bar
    );
    always_latch
    if (clk) 
        q <= d;
    // q_bar <= ~q;
endmodule
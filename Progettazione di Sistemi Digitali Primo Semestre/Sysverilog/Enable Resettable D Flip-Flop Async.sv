module enable_resettable_ff_async(
    input logic enable, clk, reset, d, 
    output logic q
    );
    always_ff @(posedge clk, posedge reset)
        if(reset) 
            q <= 1'b0;
        else if(enable) 
            q <= d;
endmodule
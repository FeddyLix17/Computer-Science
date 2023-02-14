module risoluzione_esercizio(
    input logic clk, a,
    output logic[1:0] y
);
    logic net;
always_ff @(posedge clk )
    begin 
        y[0] <= ~a;
        net <= a;
        y[1] <= net;
    end
endmodule
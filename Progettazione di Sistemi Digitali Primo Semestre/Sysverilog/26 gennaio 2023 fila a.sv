module risoluzione_esercizio(
    input logic clk, a,
    output logic[1:0] y
);
always_ff @(posedge clk ) begin 
    y[0] <= ~a;
    y[1] <= a;
end
endmodule
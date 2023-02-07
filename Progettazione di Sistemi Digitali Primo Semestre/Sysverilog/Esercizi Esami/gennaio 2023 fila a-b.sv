module solution(
    input logic a,clk,
    output logic[1:0] y 
);
logic n1;
always_ff @(posedge clk) begin
    y[0] <= ~a;
    n1 <= a;
    y[1] <= n1;
end
endmodule
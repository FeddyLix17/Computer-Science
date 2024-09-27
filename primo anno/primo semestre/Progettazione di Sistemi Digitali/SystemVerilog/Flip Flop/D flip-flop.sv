module d_flip_flop (
    input logic clk, D,
    output logic Q, Q_bar
    );


always_ff @(posedge clk) begin
    Q = D;
    Q_bar = ~Q;
end

endmodule
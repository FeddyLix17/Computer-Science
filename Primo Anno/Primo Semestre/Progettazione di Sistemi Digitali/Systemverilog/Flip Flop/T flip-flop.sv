module t_flip_flop (
    input logic clk, T,
    output logic Q, Q_bar
);

initial begin
    Q = 0;
    Q_bar = 1;
end

always_ff @(posedge clk) begin
    if (T) begin
        Q = ~Q;
        Q_bar = ~Q_bar;
    end
end

endmodule
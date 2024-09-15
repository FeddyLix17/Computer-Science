module jk_flip_flop (
    input logic clk, J, K,
    output logic Q, Q_bar
    );

    always_ff @(posedge clk) begin
        case ({J, K})
            2'b00: begin
                // Q e Q_bar non cambiano
            end
            2'b01: begin
                Q = 0;
                Q_bar = ~Q;
            end
            2'b10: begin
                Q = 1;
                Q_bar = ~Q;
            end
            2'b11: begin
                Q = ~Q;
                Q_bar = Q_bar;
            end
        endcase
    end

endmodule
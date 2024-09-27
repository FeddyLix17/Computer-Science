module jk_latch (
    input logic J, K, clk,
    output logic Q, Q_bar
    );

    always_latch begin
        if (clk) begin
            case ({J, K})
                2'b00: ; // Q, Q_bar mantengono il loro stato precedente
                2'b01: Q = 0;
                2'b10: Q = 1;
                2'b11: Q = ~Q;
            endcase
            Q_bar = ~Q;
        end
    end

endmodule
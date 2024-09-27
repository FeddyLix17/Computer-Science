module t_latch (
    input logic clk, T,
    output logic Q, Q_bar
    );

    initial begin
        Q = 0;
        Q_bar = 1;
    end
    always_latch begin
        if (clk) begin
            if (T) begin
                Q = ~Q;
            end
            Q_bar = ~Q;
        end
    end

endmodule
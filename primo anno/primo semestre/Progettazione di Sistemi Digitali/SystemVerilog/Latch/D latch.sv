module d_latch (
    input logic clk, D,
    output logic Q, Q_bar
    );

    always_latch begin
        if (clk) begin
            Q <= D;
            Q_bar <= ~D;
        end
    end

endmodule
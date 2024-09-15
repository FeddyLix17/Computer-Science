module sr_flip_flop (
    input logic S, R, clk,
    output logic Q, Q_bar
    );

    always_ff @(posedge clk) begin
        if (S && !R) begin
            Q <= 1;
            Q_bar <= 0;
        end else if (!S && R) begin
            Q <= 0;
            Q_bar <= 1;
        end else if (S && R) begin
            Q <= 1'bx;
            Q_bar <= 1'bx;
        end else begin
            // Q e Q_bar non cambiano
        end
    end

endmodule
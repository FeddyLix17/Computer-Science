module sr_latch (
    input logic S,    // Set input
    input logic R,    // Reset input
    output logic Q,   // Output
    output logic Q_bar   // Inverted output
    );

    always_latch begin
        if (S && !R) begin
            Q <= 1;
            Q_bar <= 0;
        end else if (!S && R) begin
            Q <= 0;
            Q_bar <= 1;
        end else if (!S && !R) begin
            // Q, Q_bar = loro stato precedente
        end else begin
            // stato illegale (S == 1 && R == 1)
            Q <= 1'bx;
            Q_bar <= 1'bx;
        end
    end

endmodule
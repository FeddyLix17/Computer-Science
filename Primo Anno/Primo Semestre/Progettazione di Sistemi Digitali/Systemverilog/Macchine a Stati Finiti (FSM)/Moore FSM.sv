module moore_fsm (
    input logic clk, reset, in,
    output logic out
    );

    typedef enum logic [1:0] {
        S1, S2, S3, S4 // codificati come 00, 01, 10, 11
    } state_t;

    state_t current_state, next_state;

    // State transition logic
    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            current_state <= S1;
        end else begin
            current_state <= next_state;
        end
    end

    // Next state logic
    always_comb begin
        case (current_state)
            S1: next_state = in ? S1 : S2;
            S2: next_state = in ? S1 : S3;
            S3: next_state = in ? S4 : S3;
            S4: next_state = in ? S1 : S2;
            default: next_state = S1;
        endcase
    end

    // Output logic
    assign out = current_state == S4;

endmodule
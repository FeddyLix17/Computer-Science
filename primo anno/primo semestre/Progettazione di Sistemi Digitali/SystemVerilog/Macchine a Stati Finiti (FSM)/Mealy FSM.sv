module mealy_fsm (
	input logic clk, reset, in,
	output logic [1:0] out
);

	typedef enum logic [1:0] {
		A, B, C // codificati come 00, 01, 10
	} state_t;

	state_t current_state, next_state;

	// State transition logic
	always_ff @(posedge clk or posedge reset) begin
		if (reset) begin
			current_state <= A;
		end else begin
			current_state <= next_state;
		end
	end

	// Next state logic e Output logic
	always_comb begin
		case (current_state)
			A:
				if (in) begin
					next_state <= B;
					out <= 2'b01;
				end else begin
					next_state <= A;
					out <= 2'b00;
				end
			B:
				if (in) begin
					next_state <= C;
					out <= 2'b10;
				end else begin
					next_state <= A;
					out <= 2'b01;
				end
			C:
				if (in) begin
					next_state <= C;
					out <= 2'b10;
				end else begin
					next_state <= A;
					out <= 2'b01;
				end
			default: begin
				next_state <= A;
				out <= 2'b00;
			end
		endcase
	end

endmodule
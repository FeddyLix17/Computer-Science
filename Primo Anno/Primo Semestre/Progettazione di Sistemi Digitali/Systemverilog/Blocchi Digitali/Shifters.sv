module Shifters (
    input logic [7:0] data_in,
    input logic [2:0] shift_amount,
    output logic [7:0] data_out_left,
    output logic [7:0] data_out_right
);

    // Left shifter
    assign data_out_left = data_in << shift_amount;

    // Right shifter
    assign data_out_right = data_in >> shift_amount;

endmodule
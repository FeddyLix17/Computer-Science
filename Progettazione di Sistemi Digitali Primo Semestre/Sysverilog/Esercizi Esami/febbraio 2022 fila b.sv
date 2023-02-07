module contatoredelsiumfinoa11(
    input logic clk,
    output logic [3:0] y = 4'b0000,
);
always_ff @(posedge clk)
begin
    if (y == 4'b1010)
        y = 4'b0000;
    else
        y = y + 4'b0001;
end
endmodule
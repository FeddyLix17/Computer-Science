/*
module sillyfunction(
    input logic  a, b, c,
    output logic y
    );
assign y = ~b & ~c | a & ~b;
endmodule
*/
// do a hello world
module hi(
    input logic  a, b, c,
    output logic y
    );
    // display a message
    initial begin
        $display("Hello World");
    end
endmodule
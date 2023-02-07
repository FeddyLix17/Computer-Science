module sillyfunction(
    input logic  a, b, c,
    output logic y
    );
assign y = ~b & ~c | a & ~b;
endmodule

module testbench1();
logic a, b, c;
logic y;
// definizione del DUT
sillyfunction dut(a, b, c, y);
// applicazione degli input al DUT
initial begin
    //000
a = 0; b = 0; c = 0; #10;
// 001
c = 1; #10;
// 010
b = 1; c = 0; #10;
//011
c = 1; #10;
// il # indica un delay da aspettare
// prima di testare un nuovo input
// 100
a = 1; b = 0; c = 0; #10;
// 101
c = 1; #10;
// 110
b = 1; c = 0; #10;
// 111
c = 1; #10;
// guardando bene i valori assegnati,
// possiamo notare come venga testata l'intera
// tavola della verità di A, B e C
end
endmodule

module testbench2();
logic a, b, c;
logic y;
sillyfunction dut(a, b, c, y);
initial begin
// $display() mostra a schermo un messaggio
    a = 0; b = 0; c = 0; #10;
    if (y  == 1) 
        $display("Test 000 on gang!");
    c = 1; #10;
    if (y == 0) 
        $display("Test 001 on gang!");
    b = 1; c = 0; #10;
    if (y == 0) 
        $display("Test 010 on gang!");
    c = 1; #10;
    if (y == 0) 
        $display("Test 011 on gang!");
    a = 1; b = 0; c = 0; #10;
    if (y == 1) 
        $display("Test 100 on gang!");
    c = 1; #10;
    if (y == 1) 
        $display("Test 101 on gang!");
    b = 1; c = 0; #10;
    if (y == 0) 
        $display("Test 110 on gang!");
    c = 1; #10;
    if (y == 0) 
        $display("Test 111 on gang!");
end
endmodule
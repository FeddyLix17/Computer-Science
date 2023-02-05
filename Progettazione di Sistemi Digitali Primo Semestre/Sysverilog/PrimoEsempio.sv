module fulladder(
    input logic[3:0] a, b,
    output logic [6:0] y);
// { } indicano sempre un vettore di bit
// se un numero è presente davanti a {},
// allora quel vettore viene ripetuto per N
assign y = {a[2:1], {3{b[0]}}, a[0], 6'b100_010};
// se y è un segnale a 12-bit, l'istruzione qua sopra produce:
//y = { a[2] a[1] b[0] b[0] b[0] a[0] 1 0 0 0 1 0 }
// inoltre, possiamo modificare anche
// un singolo bit di un vettore
//assign y[0] = 1’b1;
//assign y[1] = 1’b0;
endmodule
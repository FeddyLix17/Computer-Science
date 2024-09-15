module multiplier_4bit (
    input  logic [3:0] a,
    input  logic [3:0] b,
    /* per rappresentare il risultrato di un prodotto tra
    due numeri a n bit sono necessari 2*n bit */
    output logic [7:0] product
);

    assign product = a * b;

endmodule
module ALU (
    input  logic [3:0]  A, B,
    input  logic [1:0]  ALUcontrol,
    output logic [4:0]  Risultato,
    output logic [3:0]  ALUflags // N, Z, C, V
);

    always_comb begin
        case (ALUcontrol)
            2'b00: Risultato = A + B;
            2'b01: Risultato = A - B;
            2'b10: Risultato = A & B;
            2'b11: Risultato = A | B;
            default: Risultato = 4'b0000;
        endcase
    end

    // se il risultato dell'operazione eseguita è un numero negativo
    assign ALUflags[0] = (Risultato[3] == 1);

    // se il risultato dell'operazione eseguita è zero
    assign ALUflags[1] = (Risultato == 4'b0000);

    // se il risultato dell'operazione ha generato un riporto
    // Risultato[4] = C_out
    assign ALUflags[2] = (~ALUcontrol[1] && Risultato[4]);

    // se il risultato dell'operazione ha generato un overflow
    assign ALUflags[3] = (~ALUcontrol[1] && (Risultato[3] ^ A[3]) && ~(A[3] ^ B[3] ^ ALUcontrol[0]));
endmodule
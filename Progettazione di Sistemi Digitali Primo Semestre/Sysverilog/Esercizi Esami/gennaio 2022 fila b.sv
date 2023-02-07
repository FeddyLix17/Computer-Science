module moduleName (
    input logic a,b,c,
    output logic y
);
    logic n1;
    assign n1 = a ^ b;
    logic n2;
    assign n2 = a | b;
    always_comb begin 
        case ({b, c, a})
            3'b010 : y = c;
            3'b100 : y = n2;
            3'b101 : y = 0;
            3'b011 : y = 1;
            default: y = n1; 
        endcase
    end



endmodule
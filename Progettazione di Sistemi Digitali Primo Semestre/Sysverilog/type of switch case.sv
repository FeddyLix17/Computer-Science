module syncronizer(input logic d, clk,
output logic q);
logic n1;
always_ff @(posedge clk)
begin
q = n1; // bloccante
n1 = d; // bloccante
//viene generato un latch per conservare n1
end
endmodule

/* tocca rivede sto codice per provare 
a semplificare la proba di gennaio fila a (daje roma)*/
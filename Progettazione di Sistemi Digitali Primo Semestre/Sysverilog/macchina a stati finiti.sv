module threeStatesFSM (input logic clk, reset,
output logic q);
// definiamo i tre stati della FSM
typedef enum logic [1:0] {S0, S1, S2} statetype;
statetype state, nextstate;
// registri della FSM
always_ff @ (posedge clk, posedge reset)
if (reset) state <= S0;
else state <= nextstate;
// NSL della FSM
always_comb
case (state)
S0: nextstate = S1;
S1: nextstate = S2;
S2: nextstate = S0;
default: nextstate = S0;
endcase
// OL della FSM
assign q = (state == S0);
// q è il risultato della condizione (Vero o Falso)
// se lo stato attuale è S0, allora q = 1, altrimenti q = 0
endmodule
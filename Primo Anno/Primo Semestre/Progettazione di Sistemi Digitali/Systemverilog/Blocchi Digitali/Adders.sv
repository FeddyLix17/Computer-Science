module half_adder (
    input  logic a, b,
    output logic sum, Carry
    );

    assign sum = a ^ b;

    assign carry = a & b;

endmodule

module full_adder (
    input  logic a, b, cin,
    output logic sum, cout
    );

    logic s1, c1, c2;

    half_adder ha1 (a, b, s1, c1);
    half_adder ha2 (s1, cin, sum, c2);

    assign cout = c1 | c2;

endmodule

module ripple_carry_adder (
    input  logic [3:0] a, b,
    output logic [3:0] sum, cout
    );

    logic [3:0] c;

    full_adder fa0 (a[0], b[0], 0, sum[0], c[0]);
    full_adder fa1 (a[1], b[1], c[0], sum[1], c[1]);
    full_adder fa2 (a[2], b[2], c[1], sum[2], c[2]);
    full_adder fa3 (a[3], b[3], c[2], sum[3], cout);

endmodule

module carry_lookahead_adder (
    input  logic [3:0] a, b,
    output logic [3:0] sum, cout
    );

    logic [3:0] p, g, c;

    assign p[0] = a[0] | b[0];
    assign g[0] = a[0] & b[0];

    assign p[1] = a[1] | b[1];
    assign g[1] = a[1] & b[1];

    assign p[2] = a[2] | b[2];
    assign g[2] = a[2] & b[2];

    assign p[3] = a[3] | b[3];
    assign g[3] = a[3] & b[3];

    assign c[0] = g[0] | (p[0] & c[0]);
    assign c[1] = g[1] | (p[1] & c[1]);
    assign c[2] = g[2] | (p[2] & c[2]);
    assign c[3] = g[3] | (p[3] & c[3]);

    assign sum[0] = a[0] ^ b[0] ^ c[0];
    assign sum[1] = a[1] ^ b[1] ^ c[1];
    assign sum[2] = a[2] ^ b[2] ^ c[2];
    assign sum[3] = a[3] ^ b[3] ^ c[3];

    assign cout = c[3];

endmodule
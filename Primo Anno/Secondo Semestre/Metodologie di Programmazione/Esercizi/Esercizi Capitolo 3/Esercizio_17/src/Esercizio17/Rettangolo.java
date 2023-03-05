package Esercizio17;

public class Rettangolo {
    
    private double base;
    private double altezza;

    public Rettangolo(double base, double altezza) {
        this.base = base;
        this.altezza = altezza;
    }

    public void ridimensiona(double base, double altezza) {
        this.base = base;
        this.altezza = altezza;
    }

    public double perimetro() {
        return 2 * (base + altezza);
    }

    public double area() {
        return base * altezza;
    }
}

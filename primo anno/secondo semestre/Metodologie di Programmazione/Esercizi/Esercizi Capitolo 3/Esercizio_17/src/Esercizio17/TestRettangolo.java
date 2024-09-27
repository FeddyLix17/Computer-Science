package Esercizio17;

public class TestRettangolo {
    public static void main(String[] args) {
        Rettangolo r1 = new Rettangolo(1, 2);
        Rettangolo r2 = new Rettangolo(3, 4);
        Rettangolo r3 = new Rettangolo(5, 6);
        
        double sommaAree = r1.area() + r2.area() + r3.area();
        double sommaPerimetri = r1.perimetro() + r2.perimetro() + r3.perimetro();
        
        System.out.println("Somma aree: " + sommaAree);
        System.out.println("Somma perimetri: " + sommaPerimetri + "\n");
        
        r1.ridimensiona(6, 2);
        
        sommaAree = r1.area() + r2.area() + r3.area();
        sommaPerimetri = r1.perimetro() + r2.perimetro() + r3.perimetro();

        System.out.println("Somma aree: " + sommaAree);
        System.out.println("Somma perimetri: " + sommaPerimetri);
    }
}

package Esercizio1;
public class CounterTester {
    public static void main(String[] args) {
        Counter c = new Counter();  // creo un oggetto di tipo Counter
        c.click();
        c.click();     // incremento il contatore di 3 unità
        c.click();
        System.out.printf("attuale valore contatore: %d%n", c.getValue());       // stampo il suo valore
        c.undo();   // decremento il contatore di un'unità
        System.out.printf("attuale valore contatore: %d%n", c.getValue()); // stampo il suo valore
        System.out.printf("attuale valore %d uguale a 2: %b%n", c.getValue(), c.getValue() == 2);  // controllando che sia pari a 2
        c.undo();
        c.undo();                               // decremento il contatore di 3 unità
        c.undo();
        System.out.printf("attuale valore contatore: %d%n", c.getValue()); // stampo il suo valore
        System.out.printf("valore %d uguale a 0: %b", c.getValue(), c.getValue() == 0);  // controllando che sia pari a 0
    }
}
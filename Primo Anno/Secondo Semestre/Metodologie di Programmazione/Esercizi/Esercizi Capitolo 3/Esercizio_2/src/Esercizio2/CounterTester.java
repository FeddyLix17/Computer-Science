package Esercizio2;
public class CounterTester {
    public static void main(String[] args) {
        Counter c = new Counter();  // creo un oggetto di tipo Counter
        c.setLimit(3);      // imposto il valore massimo del contatore a 3
        c.click();
        c.click();     // richiamo il metodo click per 4 volte
        c.click();
        c.click();
        System.out.printf("valore counter dopo aver richiamato 4 volte il metodo click: %d", c.getValue());  // mi accerto che il valore attuale del contatore sia rimasto uguale a 3
    }
}
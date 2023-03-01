package Esercizio1;

public class Counter {

    private int CounterCurrentValue;   // creo un campo privato, di tipo intero, che rappresenterà il valore corrente del contatore
    
    public Counter() {          // creo un costruttore inizializzando il valore corrente del contatore a 0
        CounterCurrentValue = 0;
    }
    public void getValue() {
        System.out.println(CounterCurrentValue);
    }
    
    public void click() {
        CounterCurrentValue++;
    }

    public void reset() {
        CounterCurrentValue = 0;
    }

    public void undo() {
        if (CounterCurrentValue > 0) {
            CounterCurrentValue--;
        }
    }
}
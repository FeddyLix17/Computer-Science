package Esercizio1;

public class Counter { // creo una classe Counter che rappresenti il funzionamento di un contatore

    private int CounterCurrentValue;   // creo un campo privato, di tipo intero, che memorizzi il suo valore attuale
    
    public Counter() {          // creo un costruttore inizializzando il valore corrente del contatore a 0
        CounterCurrentValue = 0;
    }
    public int getValue() {    // metodo che ritorna il valore attuale del contatore
        return CounterCurrentValue;
    }
    
    public void click() {   // metodo che permette l'incremento del campo di un'unità
        CounterCurrentValue++;
    }

    public void reset() {   // metodo che reimposta il valore del campo a 0
        CounterCurrentValue = 0;
    }

    public void undo() {    // metodo che annulla l'ultima esecuizione del click, evitando che il valore del campo non scenda sotto allo 0
        if (CounterCurrentValue > 0) {
            CounterCurrentValue--;
        }
    }
}
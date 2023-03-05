package Esercizio19;

public class Interruttore {
    
    private Lampadina lampadina;
    private int statoCorrente;

    public Interruttore(Lampadina lampadina) {
        this.lampadina = lampadina;
        statoCorrente = 0;
    }
    
    public void click() {
        statoCorrente = statoCorrente == 0 ? 1 : 0;
        lampadina.click();
    }
}

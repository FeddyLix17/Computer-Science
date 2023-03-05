package Esercizio18;

public class Lampadina {
    
    private String statoLampadina;
    private int numeroClickMassimo;
    private int numeroClickAttuale;

    public Lampadina(int numeroClickMassimo) {
        statoLampadina = "Spenta";
        this.numeroClickMassimo = numeroClickMassimo;
        numeroClickAttuale = 0;
    }

    public void click() {
        numeroClickAttuale++;
        if (numeroClickAttuale == numeroClickMassimo) {
            statoLampadina = "Rotta";
        }
        switch (statoLampadina) {
            case "Spenta":
                statoLampadina = "Accesa";
                break;
            case "Accesa":
                statoLampadina = "Spenta";
                break;
            case "Rotta":
                break;
        }
    }

    public String stato() {
        return statoLampadina;
    }
}

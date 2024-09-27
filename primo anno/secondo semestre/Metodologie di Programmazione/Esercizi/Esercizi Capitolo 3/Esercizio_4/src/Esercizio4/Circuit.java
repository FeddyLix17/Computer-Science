package Esercizio4;

public class Circuit {
    
    private int firstSwitch;
    private int secondSwitch;
    private int lampState;

    public Circuit(int ffirstSwitch, int fsecondSwitch, int flampState) {
        this.firstSwitch = ffirstSwitch;
        this.secondSwitch = fsecondSwitch;
        this.lampState = flampState;
    }

    public int getFirstSwitchState() {
        return firstSwitch;
    }

    public int getSecondSwitchState() {
        return secondSwitch;
    }

    public int getLampState() {
        return lampState;
    }

    /* per entrambi i metodi toggleFirstSwitch e toggleSecondSwitch
    *  il mio approccio è il seguente:
    *  se il valore dello switch è 0, allora lo setto a 1, altrimenti
    *  lo setto a 0. Inoltre, se il valore della lampada è 0, allora
    *  la setto a 1, altrimenti la setto a 0.
    */
    public void toggleFirstSwitch() {
        firstSwitch = (firstSwitch == 0) ? 1 : 0;
        lampState = (lampState == 0) ? 1 : 0;
    }

    public void toggleSecondSwitch() {
        secondSwitch = (secondSwitch == 0) ? 1 : 0;
        lampState = (lampState == 0) ? 1 : 0;
    }

    public void printcurrentState() {
        System.out.println("Primo switch: " + firstSwitch);
        System.out.println("Secondo switch: " + secondSwitch);
        System.out.println("Stato lampada: " + lampState);
        System.out.println();
    }
}

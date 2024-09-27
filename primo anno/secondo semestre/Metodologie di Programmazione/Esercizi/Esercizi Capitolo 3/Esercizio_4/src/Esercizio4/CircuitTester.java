package Esercizio4;

public class CircuitTester {
    public static void main(String[] args) {
        Circuit circuit = new Circuit(0, 0, 0);
        System.out.println("Stato iniziale:");
        circuit.printcurrentState();
        circuit.toggleFirstSwitch();
        System.out.println("prima attivazione primo switch:");
        circuit.printcurrentState();
        circuit.toggleSecondSwitch();
        System.out.println("prima attivazione secondo switch:");
        circuit.printcurrentState();
        circuit.toggleFirstSwitch();
        System.out.println("seconda attivazione primo switch:");
        circuit.printcurrentState();
        circuit.toggleSecondSwitch();
        System.out.println("seconda attivazione secondo switch:");
        circuit.printcurrentState();
    }
}
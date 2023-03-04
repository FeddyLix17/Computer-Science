package Esercizio9;

public class CashRegister {

    private double Purchase;
    private double Payment;
    private String History;

    public CashRegister() {
        this.Purchase = 0;
        this.Payment = 0;
        this.History = "";
    }

    public void recordPurchase(double amount) {
        this.Purchase += amount;
        this.History += String.valueOf(amount) + "\n";
    }

    public void receivePayment(double payment) {
        this.Payment += payment;
    }

    public double giveChange() {
        double change = Payment - Purchase;
        this.Purchase = 0;
        this.Payment = 0;
        this.History = "";

        return change;
    }

    public void printReceipt() {
        System.out.println(this.History);
        System.out.println("Totale prodotti acquistati: " + String.valueOf(this.Purchase));
    }
}
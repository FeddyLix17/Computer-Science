package Esercizio10;

public class CashRegister {

    private double Purchase;
    private double Payment;
    private String History;
    private double salesTotal;
    private int salesCount;

    public CashRegister() {
        this.Purchase = 0;
        this.Payment = 0;
        this.History = "";
        this.salesTotal = 0;
        this.salesCount = 0;
    }

    public void recordPurchase(double amount) {
        this.Purchase += amount;
        this.salesTotal += amount;
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
        this.salesCount++;

        return change;
    }

    public void printReceipt() {
        System.out.println(this.History);
        System.out.println("Totale prodotti acquistati: " + String.valueOf(this.Purchase));
    }

    public double getSalesTotal() {
        return this.salesTotal;
    }

    public int getSalesCount() {
        return this.salesCount;
    }

    public void Reset() {
        this.salesTotal = 0;
        this.salesCount = 0;
    }
}
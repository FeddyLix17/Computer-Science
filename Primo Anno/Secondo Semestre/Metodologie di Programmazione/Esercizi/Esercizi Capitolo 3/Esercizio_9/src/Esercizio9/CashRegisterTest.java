package Esercizio9;

public class CashRegisterTest {
    public static void main(String[] args) {
        CashRegister register = new CashRegister();
        register.recordPurchase(12.34);
        register.recordPurchase(56.78);
        register.receivePayment(90.12);
        register.printReceipt();
        System.out.println("Il resto è di: " + register.giveChange());
    }
}
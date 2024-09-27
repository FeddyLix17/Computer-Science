package Esercizio10;

public class CashRegisterTester {
    public static void main(String[] args) {
        CashRegister register = new CashRegister();
        register.recordPurchase(12.34);
        register.recordPurchase(56.78);
        register.receivePayment(90.12);
        register.printReceipt();
        System.out.println("Il resto è di: " + register.giveChange());

        register.recordPurchase(12.34);
        register.recordPurchase(56.78);
        register.receivePayment(90.12);
        register.printReceipt();
        System.out.println("Il resto è di: " + register.giveChange() + "\n");
        System.out.println("Totale vendite: " + register.getSalesTotal());
        System.out.println("Numero di vendite: " + register.getSalesCount() + "\n");
        register.Reset();
        System.out.println("Totale vendite dopo il reset: " + register.getSalesTotal());
        System.out.println("Numero di vendite dopo il reset: " + register.getSalesCount());
    }
}
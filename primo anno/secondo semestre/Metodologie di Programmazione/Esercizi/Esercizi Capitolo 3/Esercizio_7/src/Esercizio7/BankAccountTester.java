package Esercizio7;

public class BankAccountTester {
    public static void main(String[] args) {
        BankAccount account = new BankAccount(1000);
        account.addInterest(10);
        System.out.println("Saldo risultante " + account.getBalance()
                            + " uguale a 1100: " + (account.getBalance() == 1100));
    }
}

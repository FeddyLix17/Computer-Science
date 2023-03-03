package Esercizio6;

public class BankAccountTester {
    public static void main(String[] args) {
        BankAccount account = new BankAccount(1000);
        account.Withdraw(500);
        account.Withdraw(400);
        System.out.println("Saldo risultante " + account.getBalance()
                            + " uguale a 100: " + (account.getBalance() == 100));
    }
}

package Esercizio8;

public class SavingAccountTester {
    public static void main(String[] args) {
        SavingsAccount savingaccount = new SavingsAccount(1000, 10);

        savingaccount.addInterest();

        System.out.println("Saldo risultante " + savingaccount.getBalance() + " uguale a 1100: "
                + (savingaccount.getBalance() == 1100));
    }
}

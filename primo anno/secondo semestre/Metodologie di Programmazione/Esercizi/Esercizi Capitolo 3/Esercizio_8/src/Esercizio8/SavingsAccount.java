package Esercizio8;

public class SavingsAccount {
    
    private double balance;
    private double interest_rate;

    public SavingsAccount() { 
        this.balance = 0;
        this.interest_rate = 0;
    }

    public SavingsAccount(double fbalance, double finterest_rate)  { 
        this.balance = fbalance;
        this.interest_rate = finterest_rate;
    }

    public void Deposit(double famount) {
        this.balance += famount;
    }

    public void Withdraw(double famount) {
        this.balance -= famount;
    }

    public double getBalance() {
        return this.balance;
    }

    public void addInterest() {
        this.balance += this.balance * this.interest_rate / 100;
    }
}

package Esercizio7;

public class BankAccount {
    
    private double balance;

    public BankAccount() { 
        this.balance = 0;
    }
    
    public BankAccount(double balance) { 
        this.balance = balance;
    }

    public void Deposit(double amount) { 
        this.balance += amount;
    }

    public void Withdraw(double amount) { 
        this.balance -= amount;
    }

    public double getBalance() {
        return balance;
    }

    public void addInterest(double rate) { 
        this.balance += this.balance * rate / 100;
    }
}
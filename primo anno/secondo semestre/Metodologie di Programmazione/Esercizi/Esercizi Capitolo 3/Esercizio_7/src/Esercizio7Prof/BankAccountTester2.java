package Esercizio7Prof;
/**
   Tests the bank account class with interest.
*/
public class BankAccountTester2
{  
   public static void main(String[] args)
   {  
      BankAccount momsSavings = new BankAccount();
      momsSavings.deposit(2000);
      momsSavings.addInterest(5);
      System.out.println(momsSavings.getBalance());
      System.out.println("Expected: 2100");
      momsSavings.addInterest(10);
      System.out.println(momsSavings.getBalance());
      System.out.println("Expected: 2310");
      momsSavings.withdraw(500);
      System.out.println(momsSavings.getBalance());
      System.out.println("Expected: 1810");
      
   }
}

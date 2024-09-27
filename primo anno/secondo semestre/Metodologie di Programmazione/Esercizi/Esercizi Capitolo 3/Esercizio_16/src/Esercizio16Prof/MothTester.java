package Esercizio16Prof;
public class MothTester
{
   public static void main(String[] args)
   {
      Moth gypsy = new Moth(10);
      gypsy.moveToLight(0);
      System.out.println(gypsy.getPosition());
      System.out.println("Expected: 5");
      gypsy.moveToLight(10);
      System.out.println(gypsy.getPosition());
      System.out.println("Expected: 7.5");
      gypsy.moveToLight(0);
      System.out.println(gypsy.getPosition());
      System.out.println("Expected: 3.75");
   }
}

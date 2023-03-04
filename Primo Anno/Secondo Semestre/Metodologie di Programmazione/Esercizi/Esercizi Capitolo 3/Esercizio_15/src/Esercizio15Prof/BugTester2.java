package Esercizio15Prof;
public class BugTester2
{
   public static void main(String[] args)
   {
      Bug lady = new Bug(10);
      lady.turn();
      lady.move();
      lady.move();
      lady.turn();
      lady.turn();
      lady.move();
      lady.move();
      lady.move();
      lady.move();
      System.out.println(lady.getPosition());
      System.out.println("Expected: 4");
   }
}

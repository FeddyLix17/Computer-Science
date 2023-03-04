package Esercizio15;

public class BugTester {
    public static void main(String[] args) {
        Bug bug = new Bug(10);
        bug.Move();
        bug.Move();
        bug.Turn();
        bug.Move();
        System.out.println("Posizione finale " + bug.GetPosition() + " uguale a 11: "
        + (bug.GetPosition() == 11));
    }
}

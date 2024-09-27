package Esercizio20;



public class TestInterruttore {
    public static void main(String[] args) {
        Lampadina lampadina = new Lampadina(4);
        Interruttore interruttore_1 = new Interruttore(lampadina);
        Interruttore interruttore_2 = new Interruttore(lampadina);

        interruttore_1.click();
        System.out.println(lampadina.stato());
        interruttore_2.click();
        System.out.println(lampadina.stato());
        interruttore_1.click();
        System.out.println(lampadina.stato());
        interruttore_2.click();
        System.out.println(lampadina.stato());
    }
}

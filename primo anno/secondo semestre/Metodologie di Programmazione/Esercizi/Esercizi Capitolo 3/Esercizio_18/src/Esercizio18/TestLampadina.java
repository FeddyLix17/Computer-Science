package Esercizio18;

public class TestLampadina {
    public static void main(String[] args) {
        Lampadina lampadina = new Lampadina(3);
        lampadina.click();
        lampadina.click();
        lampadina.click();
        lampadina.click();
        System.out.println(lampadina.stato());
    }
}

package Esercizio16;

public class DayTester {
    public static void main(String[] args) {
        Day d1 = new Day(14, 10, 2023);
        Day d2 = new Day(24, 10, 2023);
        System.out.printf("numero dei giorni ' %d ' uguale a 10: %b", d1.daysFrom(d2),
                            d1.daysFrom(d2) == 10);
    }
}

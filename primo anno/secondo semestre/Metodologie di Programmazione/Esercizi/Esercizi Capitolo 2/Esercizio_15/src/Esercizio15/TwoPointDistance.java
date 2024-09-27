package Esercizio15;

import java.awt.Point;

public class TwoPointDistance {
    public static void main(String[] args) {
        Point p1 = new Point(1, 2);
        Point p2 = new Point(3, 4);
        double Distanza = p1.distance(p2);
        System.out.printf("Distanza: %.2f", Distanza);
    }
}
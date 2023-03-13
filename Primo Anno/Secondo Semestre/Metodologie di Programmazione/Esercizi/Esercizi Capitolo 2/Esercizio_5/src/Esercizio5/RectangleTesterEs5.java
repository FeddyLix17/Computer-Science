package Esercizio5;

import java.awt.Rectangle;

public class RectangleTesterEs5 {
    public static void main(String[] args) {
        Rectangle r1 = new Rectangle(6, 7);
        Rectangle r2 = new Rectangle(3, 14);
        System.out.println("Base primo rettangolo: " + r1.getWidth());
        System.out.println("Altezza primo rettangolo: " + r1.getHeight());
        System.out.println("Base secondo rettangolo: " + r2.getWidth());
        System.out.println("Altezza rettangolo: " + r2.getHeight());
    }
}

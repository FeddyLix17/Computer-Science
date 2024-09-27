package Esercizio4;

import java.awt.Rectangle;

public class RectangleTester2 {
    public static void main(String[] args) {
        Rectangle rettangolo = new Rectangle(0, 0, 12, 34);
        // calcolare il perimetro del rettangolo
        System.out.println("Perimetro rettangolo: " 
                            + ((rettangolo.getWidth() + rettangolo.getHeight())) * 2);
    }
}

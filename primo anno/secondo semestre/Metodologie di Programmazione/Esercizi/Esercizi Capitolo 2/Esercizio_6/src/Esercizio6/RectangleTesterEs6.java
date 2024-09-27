package Esercizio6;

import java.awt.Rectangle;

public class RectangleTesterEs6 {
    public static void main(String[] args) {
        Rectangle rettangolo = new Rectangle(10, 20, 12, 34);
        System.out.println("coordinata x prima della modifica: " + rettangolo.getX() + "\n" 
                            + "coordinata y prima della modifica: " + rettangolo.getY() + "\n");
        
        rettangolo.add(0, 0);
        System.out.println("coordinata x dopo della modifica: " + rettangolo.getX() + "\n"
                            + "coordinata y dopo della modifica: " + rettangolo.getY());
        System.out.println("nuova base rettangolo: " + rettangolo.getWidth() + "\n"
                            + "nuova altezza rettangolo: " + rettangolo.getHeight());
    }
}

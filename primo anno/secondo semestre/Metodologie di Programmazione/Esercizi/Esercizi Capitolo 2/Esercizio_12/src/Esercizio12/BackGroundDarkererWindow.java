package Esercizio12;

import java.awt.Color;

public class BackGroundDarkererWindow {
    public static void main(String[] args) {
        Color colore = new Color(12, 34, 56);
        Color coloreRossopiuScuro = new Color(colore.getRed() / 2, colore.getGreen(), colore.getBlue());
        coloreRossopiuScuro = colore.darker();
        System.out.printf("Rosso: %d \nVerde: %d \nBlu: %d",
                            coloreRossopiuScuro.getRed(), coloreRossopiuScuro.getGreen(), coloreRossopiuScuro.getBlue());
    }
}

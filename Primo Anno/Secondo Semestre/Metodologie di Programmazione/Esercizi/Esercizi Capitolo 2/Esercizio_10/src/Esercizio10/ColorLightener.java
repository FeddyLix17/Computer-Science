package Esercizio10;

import java.awt.Color;

public class ColorLightener {
    public static void main(String[] args) {
        Color color = new Color(12, 34, 56);
        color = color.brighter();
        System.out.printf("Red: %d \nGreen: %d \nBlue: %d", color.getRed(), color.getGreen(), color.getBlue());
    }
}

package Esercizio11;

import java.awt.Color;
import javax.swing.*;

public class BackGroundWindow {
    public static void main(String[] args) {
        Color coloresfondofinestra = new Color(12, 34, 56);
        coloresfondofinestra = coloresfondofinestra.brighter();
        JFrame finestra = new JFrame();
        finestra.setSize(200, 200);
        finestra.getContentPane().setBackground(coloresfondofinestra);
        finestra.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        finestra.setVisible(true);
    }
}

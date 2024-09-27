package Esercizio19;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import javax.swing.JComponent;
import javax.swing.JFrame;

public class RectangleWindowsEs19  extends JComponent {
    
    public void paintComponent(Graphics g) {
        Graphics2D g2 = (Graphics2D) g;

        // Creazione dei due rettangoli
        Rectangle rect1 = new Rectangle(50, 50, 200, 200);
        Rectangle rect2 = new Rectangle(100, 100, 100, 100);

        // Impostazione del colore di riempimento del rettangolo più grande
        g2.setColor(Color.GRAY);
        g2.fill(rect1);

        // Impostazione del colore di contorno del rettangolo più grande
        g2.setColor(Color.BLACK);
        g2.draw(rect1);

        // Impostazione del colore di contorno del rettangolo più piccolo
        g2.setColor(Color.RED);
        g2.draw(rect2);

        // Aggiunta dei rettangoli al contenitore di tipo Graphics2D
        g2.draw(rect1);
        g2.draw(rect2);
    }
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.setSize(300, 300);
        frame.setTitle("Rectangle Window");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        RectangleWindowsEs19 rectWindow = new RectangleWindowsEs19();
        frame.add(rectWindow);

        frame.setVisible(true);
    }
}

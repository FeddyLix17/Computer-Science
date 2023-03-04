package Esercizio14;

public class LetterPrinter {
    public static void main(String[] args) {
        Letter letter = new Letter("J. K. Rowling", "Harry");
        letter.addLine("Benvenuto a Hogwarts!");
        letter.addLine("Spero che ti piaccia");
        letter.addLine("Il mondo magico");
        System.out.println(letter.getText());
    }
}

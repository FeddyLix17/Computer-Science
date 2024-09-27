package Esercizio2;

import java.util.Scanner;

public class SpaceReplacer {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Inserire la stringa: ");
        String string = scanner.nextLine();

        string = string.trim();
        string = string.replace(" ", "");
        System.out.println("Stringa Formattata: " + string);

        scanner.close();
    }
}

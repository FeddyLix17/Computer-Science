package Esercizio4;

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Inserisci una parola: ");
        String parola = scanner.nextLine();
        String primameta = parola.substring(0, (parola.length() - 1) / 2);
        String secondameta = parola.substring((parola.length() / 2) + 1, parola.length());
        if (primameta.equals(secondameta)) {
            System.out.println("La prima metà della parola è uguale alla seconda metà");
        } else {
            System.out.println("La prima metà della parola non è uguale alla seconda metà");
        }
        scanner.close();
    }
}

package Esercizio3;

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Inserisci una parola: ");
        String parola = scanner.nextLine();
        if (parola.charAt(0) == parola.charAt(parola.length() - 1)) {

            System.out.println("La parola inizia e finisce con la stessa lettera");
        } else {

            System.out.println("La parola non inizia e finisce con la stessa lettera");
        }
        scanner.close();
    }
}

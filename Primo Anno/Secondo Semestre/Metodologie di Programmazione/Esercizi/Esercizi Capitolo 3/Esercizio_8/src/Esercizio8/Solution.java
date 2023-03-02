package Esercizio8;

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Inserisci il primo numero: ");
        int num1 = scanner.nextInt();
        
        System.out.print("Inserisci il secondo numero: ");
        int num2 = scanner.nextInt();

        System.out.print("Inserisci il terzo numero: ");
        int num3 = scanner.nextInt();
        
        if (num1 < num2 && num2 < num3) {
            System.out.println("I numeri sono in ordine crescente");
        } else if (num1 > num2 && num2 > num3) {
            System.out.println("I numeri sono in ordine decrescente");
        } else {
            System.out.println("I numeri non sono in nessun ordine");
        }
        
        scanner.close();
    }
}

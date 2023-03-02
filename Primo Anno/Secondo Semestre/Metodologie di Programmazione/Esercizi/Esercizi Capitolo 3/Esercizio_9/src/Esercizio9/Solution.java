package Esercizio9;

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
        
        System.out.print("Inserisci il quarto numero: ");
        int num4 = scanner.nextInt();

        if (num1 == num2) {
            System.out.println("Il primo e il secondo numero sono uguali");
        }
        
        if (num1 == num3) {
            System.out.println("Il primo e il terzo numero sono uguali");
        }
        
        if (num1 == num4) {
            System.out.println("Il primo e il quarto numero sono uguali");
        }
        
        if (num2 == num3) {
            System.out.println("Il secondo e il terzo numero sono uguali");
        }
        
        if (num2 == num4) {
            System.out.println("Il secondo e il quarto numero sono uguali");
        }
        
        if (num3 == num4) {
            System.out.println("Il terzo e il quarto numero sono uguali");
        }
        
        if (num1 != num2 && num1 != num3 && num1 != num4 && num2 != num3 && num2 != num4 && num3 != num4) {
            System.out.println("Nessun numero è uguale");
        }
        
        scanner.close();
    }
}

package Esercizio5;

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        /*  ogni numero sarà dichiarato come double in modo 
            da poter rispettare la richiesta per la quale i
            3 numeri debbano essere a virgola mobile con 
            doppia precisione 
                                */

        System.out.print("Inserire il primo numero: ");
        double num1 = scanner.nextDouble();

        System.out.print("Inserire il secondo numero: ");
        double num2 = scanner.nextDouble();

        System.out.print("Inserire il terzo numero: ");
        double num3 = scanner.nextDouble();

        if (num1 == num2 && num2 == num3) {
            System.out.println("Tutti e tre i numeri sono uguali.");
        } else if (num1 != num2 && num1 != num3 && num2 != num3) {
            System.out.println("Tutti e tre i numeri sono diversi.");
        } else {
            System.out.println("I numeri non appartengono ai casi precedenti.");
        }

        scanner.close();
    }
}

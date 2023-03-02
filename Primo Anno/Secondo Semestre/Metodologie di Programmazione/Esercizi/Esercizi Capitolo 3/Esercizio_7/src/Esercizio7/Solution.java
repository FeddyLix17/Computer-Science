package Esercizio7;

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Inserire il primo numero: ");
        double num1 = scanner.nextDouble();

        System.out.print("Inserire il secondo numero: ");
        double num2 = scanner.nextDouble();

        System.out.print("Inserire il terzo numero: ");
        double num3 = scanner.nextDouble();

        System.out.print("Scegliere il tipo di controllo "
        + "('S' o 's' = tipo stretto, 'L' o 'l' = tipo lato): ");
        char choice = scanner.next().charAt(0);
        /* Con "controllo di tipo stretto" si intende verificare che la sequenza
            di numeri sia strettamente crescente o strettamentedecrescente, 
            ovvero se ogni numero successivo è maggiore o minore del precedente 
            senza che ci siano numeri uguali.

            Con "controllo di tipo lato", invece, si intende verificare 
            che la sequenza di numeri sia crescente o decrescente 
            anche ammettendo numeri uguali tra di loro. In questo caso, la
            sequenza viene considerata crescente o decrescente se ogni numero 
            successivo è maggiore o uguale (o minore o uguale) del precedente.
         */
        if (choice == 'S' || choice == 's') {
            if (num1 < num2 && num2 < num3) {
                System.out.println("increasing");
            } else if (num1 > num2 && num2 > num3) {
                System.out.println("decreasing");
            } else {
                System.out.println("la sequenza non è in nessun ordine stretto.");
            }
        } else if (choice == 'L' || choice == 'l') {
            if (num1 <= num2 && num2 <= num3) {
                System.out.println("increasing");
            } else if (num1 >= num2 && num2 >= num3) {
                System.out.println("decreasing");
            } else {
                System.out.println("la sequenza non è in nessun ordine lato.");
            }
        } else {
            System.out.println("Scelta inserita invalida.");
        }
        scanner.close();
    }
}

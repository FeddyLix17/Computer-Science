package Esercizio13;

import java.util.Random;

public class Dado {
    public static void main(String[] args) {
        Random numerorandom = new Random();
        System.out.println("Lancio del dado");
        System.out.println("Il numero uscito è: " + numerorandom.nextInt(6) + 1);
    }
}
package Esercizio14;

import java.util.Random;

public class CasualPrice {
    public static void main(String[] args) {
        Random prezzocasuale = new Random();
        int prezzo = prezzocasuale.nextInt(100);
        int centesimi = prezzocasuale.nextInt(100);
        double prezzofinale = ((prezzo*100) + centesimi) / 100.0;
        System.out.printf("Il prezzo del prodotto è: %.2f", prezzofinale);
    }
}
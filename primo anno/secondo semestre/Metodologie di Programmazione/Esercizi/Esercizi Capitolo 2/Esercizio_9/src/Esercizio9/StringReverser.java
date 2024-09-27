package Esercizio9;

public class StringReverser {
    public static void main(String[] args) {
        String stringa = "desserts";
        StringBuilder stringbuilder = new StringBuilder(stringa);
        stringbuilder.reverse();
        System.out.print(stringbuilder);
    }
}
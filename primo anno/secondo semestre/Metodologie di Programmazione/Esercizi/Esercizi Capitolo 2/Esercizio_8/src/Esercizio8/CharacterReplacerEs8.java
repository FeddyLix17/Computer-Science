package Esercizio8;

public class CharacterReplacerEs8 {
    public static void main(String[] args) {
        String stringa = "Hello, World!";
        stringa = stringa.replace('e', '%');
        stringa = stringa.replace('o', 'e');
        stringa = stringa.replace('%', 'o');
        System.out.printf("%s uguale a Holle, Werld!: %b", stringa, stringa.equals("Holle, Werld!"));
    }
}

package Esercizio7;

public class CharacterReplacerEs7 {
    public static void main(String[] args) {
        String s = "Mississippi";
        s = s.replace("i", "!");
        s = s.replace("s", "$");
        System.out.printf("%s uguale a M!$$!$$!pp!: %b", s, s.equals("M!$$!$$!pp!"));
    }
}
package Esercizio1;

public class CharacterReplacer {
    
    public static void main(String[] args) {
        String Stringa = "Mississippi";
        System.out.println(Stringa);
        
        Stringa = Stringa.replace("i", "ii");
        Stringa = Stringa.replace("ss", "s");
        System.out.println("Stringa con i caratteri rimpiazzati: " + Stringa);
    }
}

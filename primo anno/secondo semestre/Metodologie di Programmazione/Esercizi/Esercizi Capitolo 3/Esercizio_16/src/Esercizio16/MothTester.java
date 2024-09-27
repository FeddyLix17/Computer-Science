package Esercizio16;

public class MothTester {
    public static void main(String[] args) {
        Moth moth = new Moth(10);

        moth.moveToLight(0);
        System.out.println(moth.getPosition());
        
        moth.moveToLight(10);
        System.out.println(moth.getPosition());
        
        moth.moveToLight(0);
        System.out.println(moth.getPosition());
    }
}

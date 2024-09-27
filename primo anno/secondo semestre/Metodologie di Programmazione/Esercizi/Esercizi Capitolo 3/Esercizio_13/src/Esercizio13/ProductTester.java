package Esercizio13;

public class ProductTester {
    public static void main(String[] args) {
        Product product1 = new Product("Aspirapolvere", 30);
        product1.reducePrice(5);
        System.out.println("Nome prodotto: " + product1.getName());
        System.out.println("Prezzo prodotto: " + product1.getPrice());
    }
}

package Esercizio13;

public class Product {
    
    private String Name;
    private double Price;

    public Product(String Name, double Price) {
        this.Name = Name;
        this.Price = Price;
    }

    public String getName() {
        return this.Name;
    }

    public double getPrice() {
        return this.Price;
    }

    public void reducePrice(double amount) {
        this.Price -= amount;
    }
}

package Esercizio12;

public class CarTester {
    public static void main(String[] args) {
        Car car = new Car(50);
        car.addGas(20);
        car.Drive(100);
        System.out.println("Carburante residuo rimasto " + car.getGasInTank() 
                            + " uguale a 18 litri: " + (car.getGasInTank() == 18));
    }
}

package Esercizio12;

public class Car {
    
    private double Gas;
    private double Efficiency;

    public Car(double Efficiency) {
        this.Gas = 0;
        this.Efficiency = Efficiency;
    }

    public void addGas(double Gas) {
        this.Gas += Gas;
    }

    public void Drive(double Distance) {
        this.Gas -= Distance / this.Efficiency;
    }

    public double getGasInTank() {
        return this.Gas;
    }
}

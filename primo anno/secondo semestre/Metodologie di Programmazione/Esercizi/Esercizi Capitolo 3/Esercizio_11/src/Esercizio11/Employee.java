package Esercizio11;

public class Employee {
    
    private String Name;
    private double Salary;

    public Employee(String Name, double Salary) {
        this.Name = Name;
        this.Salary = Salary;
    }

    public String getName() {
        return this.Name;
    }

    public double getSalary() {
        return this.Salary;
    }

    public void raiseSalary(double percent) {
        this.Salary += (this.Salary * percent / 100);
    }
}
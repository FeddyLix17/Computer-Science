package Esercizio16;

public class Moth {
    
    private double Position;
    
    public Moth(double initialPosition) {
        this.Position = initialPosition;
    }
    
    public void moveToLight(double lightPosition) {
        this.Position = (this.Position + lightPosition) / 2;
    }
    
    public double getPosition() {
        return Position;
    }
}

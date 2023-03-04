package Esercizio15;

public class Bug {
    
    private int Position;
    private int Direction;

    public Bug(int initialPosition) {
        this.Position = initialPosition;
        this.Direction = 1;
    }

    public void Move() {
        this.Position += this.Direction;
    }

    public void Turn() {
        this.Direction *= -1;
    }

    public int GetPosition() {
        return this.Position;
    }
}

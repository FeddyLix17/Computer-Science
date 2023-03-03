package Esercizio3;

public class RangeInput {
    
    private int Min;
    private int Max;
    private int Current;
    
    public RangeInput(int fmin, int fmax, int fcurrent) {
        this.Min = fmin;
        this.Max = fmax;
        this.Current = fcurrent;
    }
    
    public void up(){
        if (Current < Max){
            Current++;
        }
    }

    public void down(){
        if (Current > Min){
            Current--;
        }
    }
}

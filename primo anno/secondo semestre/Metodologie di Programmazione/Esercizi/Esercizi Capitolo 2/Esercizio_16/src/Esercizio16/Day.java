package Esercizio16;

public class Day {
    
    private int Giorno;
    private int Mese;
    private int Anno;

    public Day(int Giorno, int Mese, int Anno) {
        this.Giorno = Giorno;
        this.Mese = Mese;
        this.Anno = Anno;
    }

    public void addDays(int days) {
        Giorno += days;
        if (Giorno > 30) {
            Giorno -= 30;
            Mese++;
        }
        if (Mese > 12) {
            Mese -= 12;
            Anno++;
        }
    }

    public int daysFrom(Day day) {
        int NumberOfDay = 0;
        if (Anno > day.Anno) {
            NumberOfDay = (Anno - day.Anno) * 365;
            NumberOfDay += (Mese - day.Mese) * 30;
            NumberOfDay += Giorno - day.Giorno;
        } else {
            NumberOfDay = (day.Anno - Anno) * 365;
            NumberOfDay += (day.Mese - Mese) * 30;
            NumberOfDay += day.Giorno - Giorno;
        }
        return NumberOfDay;
    }
}

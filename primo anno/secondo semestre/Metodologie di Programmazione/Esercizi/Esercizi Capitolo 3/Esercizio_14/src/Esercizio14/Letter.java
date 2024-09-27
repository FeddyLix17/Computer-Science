package Esercizio14;

public class Letter {
    
    private String Sender;
    private String Recipient;
    private String Body;

    public Letter(String Sender, String Recipient) {
        this.Sender = Sender;
        this.Recipient = Recipient;
        this.Body = "";
    }

    public void addLine(String line) {
        this.Body += (line + "\n");
    }

    public String getText() {
        return "Caro " + this.Recipient + ",\n" 
        + this.Body + "\nTuo\n" 
        + this.Sender;
    }
}

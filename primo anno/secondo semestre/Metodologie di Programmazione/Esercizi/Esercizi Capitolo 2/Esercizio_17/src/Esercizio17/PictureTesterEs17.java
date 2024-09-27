package Esercizio17;

public class PictureTesterEs17 {
    public static void main(String[] args) {
        Picture pic = new Picture();
        pic.load("C:/Users/FedVlogger17/Documents/GitHub/Uni/Primo Anno/Secondo Semestre/Metodologie di Programmazione/Esercizi/Esercizi Capitolo 2/Esercizio_17/src/Esercizio17/immaginediprova.jpg");
        pic.scale(pic.getWidth()/2, pic.getHeight()/2);
        pic.move(pic.getWidth()/4, pic.getHeight()/4);
    }
}
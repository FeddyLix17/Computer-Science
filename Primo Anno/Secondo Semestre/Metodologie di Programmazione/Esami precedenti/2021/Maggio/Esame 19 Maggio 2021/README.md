# <p align= "center"> Esame 19 Maggio 2021 </p>

### 1.  Descrivere i modificatori di visibilità utilizzati all’interno delle classi

I modificatori di visibilità sono implementati in java tramite l'uso di apposite *keyword* permettendo di definire la visibilità di un membro (metodo o variabile) di una classe. <br>

Essi sono:

- **public**: i membri pubblici sono accessibili da una qualsiasi classe.
- **private**: i membri privati sono accessibili solo dalla classe in cui sono dichiarati.
- **protected**: i membri protetti sono accessibili dalla classe in cui sono dichiarati e dalle sottoclassi che estendono la classe in cui sono dichiarati.

Qualora non dovessimo specificare nessun modificatore di visibilità, il tipo di modificatore sarà *default*, ed i membri dichiarati in questo modo saranno accessibili solo dalle classi che si trovano nello stesso pacchetto.

### 2. Spiegare il concetto di interfaccia ed il suo utilizzo. <br>Produrre un esempio (con codice minimale) che comprenda la definizione di una interfaccia insieme ad un metodo che la preveda come parametro per svolgere un compito a scelta

Un’interfaccia è un tipo di dato astratto (astratto perché definisce un insieme di metodi che una classe deve implementare, ma non specifica come questi metodi devono essere implementati). <br> Vengono dichiarate tramite la keyword *interface* ed *implementate* da una classe tramite la
keyword *implements*. <br> Una classe può implementare una o più interfacce, essa (l'interfaccia) non prevede un costruttore e tutti i suoi metodi hanno modificatore di visibilità public.


```java
public interface Dispositivo {
    public void accendi();
    public void spegni();
}
```

```java
public class Telefono implements Dispositivo {

    public Telefono() {...}

    @Override
    public void accendi() {
        System.out.println("Accendo il telefono");
    }

    @Override
    public void spegni() {
        System.out.println("Spengo il telefono");
    }
}
```

```java
public class Computer implements Dispositivo {
    public Computer() {...}

    @Override
    public void accendi() {
        System.out.println("Accendo il computer");
    }

    @Override
    public void spegni() {
        System.out.println("Spengo il computer");
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        Dispositivo telefono = new Telefono();
        Dispositivo computer = new Computer();
        telefono.accendi();                      // Accendo il telefono
        telefono.spegni();                      // Spengo il telefono
        computer.accendi();                    // Accendo il computer
        computer.spegni();                    // Spengo il computer
    }
}
```

### 3. Quante iterazioni eseguono i seguenti costrutti iterativi, supponendo che la variabile contatore i non venga modificata all’interno di ciascun ciclo?

```java
(a) for(int i = 1; i <= 10; i++){...}   // 10 iterazioni
(b) for(int i = 0; i < 10; i++){...}    // 10 iterazioni
(c) for(int i = 10; i > 0; i--){...}    // 10 iterazioni
(d) for(int i = -10; i >= 0; i++){...} // 0 iterazioni
(e) for(int i = 10; i >= 0; i++){...} // infinite iterazioni
(f) for(int i = -10; i <= 10; i = i + 2){...} // 11 iterazioni
(g) for(int i = -10; i <= 10; i = i + 3){...} // 7 iterazioni
```

### 4. Scrivere un programma che generi una sequenza di 20 lanci casuali di un dado, memorizzando i risultati in un array. <br> Successivamente, visualizzare i valori ottenuti, identificando soltanto la ripetizione più lunga e racchiudendola tra parentesi tonde come in questo esempio: <br>   <p align ="center"> *1 2 5 5 3 1 2 4 3 (2 2 2 2) 3 6 5 5 6 3 3 3 3 1* </p> In caso di più ripetizioni dalla stessa lunghezza massima, contrassegnare solamente la prima.

```java
import java.util.Random;                // libreria necessaria per generare la sequenza

public class LongestRepetition {

    public static void main (String[] args) {

        Random random = new Random();
        int[] lanci = random.ints(20, 1, 7).toArray();                  // generazione sequenza di 20 lanci casuali di un dado
        int currStart = 0;                                              // indice inizio ripetizione corrente
        int currLen = 1;                                                // lunghezza ripetizione corrente
        int maxStart = 0;                                               // indice inizio ripetizione più lunga di tutta la sequenza
        int maxLen = 0;                                                 // lunghezza ripetizione più lunga di tutta la sequenza

        for (int i = 1; i < lanci.length; i++) {                        // itero la sequenza generata partendo dal secondo elemento
            if (lanci[i] == lanci[i - 1]) {                             // se l'elemento precedente è uguale all'elemento corrente

                // prima incremento la lungezza della ripetizione corrente per poi confrontrarla con l'attuale lunghezza massima
                if (++currLen > maxLen) {
                    
                    // e se la lunghezza della ripetizione corrente aggiornata è più grande dell'attuale lunghezza massima
                    // la sostituisco a quest'ultima
                    maxStart = currStart;
                    maxLen = currLen;
                }
            }

            // altrimenti proseguo nella sequenza mantendendo aggiornati i valori correnti
            else {
            currStart = i;
            currLen = 1;
            }
        }
        
        // una volta trovata la ripetizione più lunga nella sequenza
        // stampo ogni elemento della sequenza con delle parentesi
        // tonde attorno alla ripetizione più lunga
        for (int i = 0; i < lanci.length; i++) {

            if (i == maxStart) {                                        // se mi trovo all'inizio della ripetizione più lunga
                System.out.print("(");                                 // apro una parentesi tonda
            }

            if (i == maxStart + maxLen - 1) {                         // se mi trovo alla fine della ripetizione più lunga
                System.out.print(lanci[i] + ") ");                   // chiudo la parentesi tonda
                continue;                                           // e passo al carattere successivo
            }

            System.out.print(lanci[i] + " ");                      // altrimenti stampo semplicemente l'elemento corrente della sequenza
        }
    }
}
```

### 5. il responsabile amministrativo di un albergo registra le transazioni in un file di testo. Ogni riga contiene le seguenti informazioni, separate da “punti e virgola”:
- il nome del cliente;
- il servizio venduto (ad esempio, cena, conferenza, alloggio, etc.);
- l’importo pagato;
- la data dell’evento.

Scrivere un programma che legga un tale file di testo e visualizzi l’importo totale relativo a ciascun servizio, segnalando un errore se il file non esiste oppure se il suo formato non è corretto. <br> A seguire viene
riportato un esempio del contenuto del file: <br>

<p align="center">
    Mario Bianchi;Cena;29.95;6/7/2020 <br>
    Giovanna Rossi;Conferenza;499.00;8/9/2020 <br>
    Manuela Verdi;Alloggio;23.45;10/10/2020 <br>
    Giulia Gialli;Cena;93.00;11/12/2020 <br>
    Michele Apicella;Cinema;10.00;1/1/1970 <br>
</p>

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class ReadFile {
    public static void main(String[] args) {

        File file = new File("transazioni.txt");                                    // creo un oggetto File rappresentante il file da leggere
        Map<String, Double> ServizioConPrezzo = new HashMap<>();                   // mi preparo a "mappare" il servizo venduto con il relativo importo pagato in coppia chiave-valore

        try (Scanner scanner = new Scanner(file)) {                                 // "provo" a leggere il contenuto del file
            while (scanner.hasNextLine()) {                                        // finché ci sono righe da leggere

                String riga = scanner.nextLine();                                // leggo la riga corrente
                String[] InformazioniRiga = riga.split(";");                    // e salvo ogni informazione separatamente in una lista

                if (InformazioniRiga.length != 4) {                               // se i dati della riga corrente non sono stati inseriti in modo corretto
                    System.out.println("Formato del file non corretto.");        // stampo il relativo messaggio di errore
                    return;                                                     // terminando del programma
                }

                String service = InformazioniRiga[1];                          // altrimenti, se la riga correte è stata inserita in modo corretto, salvo rispettivamente
                double amount = Double.parseDouble(InformazioniRiga[2]);      // il servizio venduto e l'importo pagato che dovranno essere stampati successivamente
                
                // per aggiungere/aggiornare il valore totale del servizio venduto corrente,
                // invece di usate il metodo get utilizzo il metodo getOrDefault che permette di
                // gestire entrambi i casi in cui il servizio sia già stato venduto in precedenza
                // o non sia ancora stato venduto
                ServizioConPrezzo.put(service, ServizioConPrezzo.getOrDefault(ServizioConPrezzo, null) + amount);
            }
        } catch (FileNotFoundException e) {                          // se il file non esiste
            System.out.println("Il file non esiste.");              // stampo il relativo messaggio di errore
            return;                                                // terminando del programma
        }
        // una volta registrati correttamente tutti i servizi venduti con il relativo importo totale pagato per ognuno di essi
        // li stampo uno per uno
        for (Map.Entry<String, Double> entry : ServizioConPrezzo.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
```

### 6. Un aeroporto ha un’unica pista. <br> Quando la pista è occupata, gli aerei che vogliono atterrare o decollare devono attendere. <br> Realizzare un programma di simulazione usando due code, una per gli aerei in attesa di decollare e una per quelli in attesa di atterrare. <br> Gli aerei in attesa di atterrare hanno la precedenza. <br> L’utente del simulatore può digitare i seguenti comandi: takeoﬀ codiceDelVolo, land codiceDelVolo next e quit. <br> I primi due comandi inseriscono il volo nella coda corrispondente (decollo per takeoﬀ e atterraggio per land). <br> Il comando next pone termine all’operazione in corso (decollo o atterraggio) e fa partire la successiva, visualizzando l’azione da intraprendere (decollo o atterraggio) e il codice del volo. <br> Il comando quit, ovviamente, termina la simulazione


```java
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Aeroporto {
    public static void main(String[] args) {
        
        Queue<String> AereiDecollo = new LinkedList<String>();                  // Coda contenente i codici dei voli in decollo    
        Queue<String> AereiAtterraggio = new LinkedList<String>();             // Coda contenente i codici dei voli in atterraggio
        Scanner scanner = new Scanner(System.in);                              
        String CodiceVolo = "";

        System.out.print("Si scelga un comando da eseguire (takeoff, land, next, quit): ");
        String comando = scanner.next();

        while (!comando.equals("quit")) {
            switch (comando) {
                case "takeoff":
                    System.out.print("Inserire il codice del Volo che deve decollare: ");
                    CodiceVolo = scanner.next();
                    AereiDecollo.add(CodiceVolo);
                    break;
                case "land":
                    System.out.print("Inserire il codice del Volo che deve atterrare: ");
                    CodiceVolo = scanner.next();
                    AereiAtterraggio.add(CodiceVolo);
                    break;
                case "next":
                    if (AereiDecollo.isEmpty() && AereiAtterraggio.isEmpty()) {
                        System.out.println("Non ci sono aerei in coda");
                    } else if (!AereiAtterraggio.isEmpty()) {
                        System.out.println("Il volo " + AereiAtterraggio.poll() + " sta atterrando");
                    } else if (!AereiDecollo.isEmpty()) { 
                        System.out.println("Il Volo " + AereiDecollo.peek() + " sta decollando");
                        AereiAtterraggio.add(AereiDecollo.poll());
                    }
                    break;
                default:
                    System.out.println("Comando non valido, riprovare");
                    break;
            }
            System.out.print("Si scelga un comando da eseguire (takeoff, land, next, quit): ");
            comando = scanner.next();
        }
        scanner.close();
    }
}
```

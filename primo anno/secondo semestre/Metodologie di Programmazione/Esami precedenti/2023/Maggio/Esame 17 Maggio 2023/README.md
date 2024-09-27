# <p align="center"> Esame 17 Maggio 2023 </p>

## Esercizio 1

Per ogni domanda, indicare con una X la risposta desiderata.

Si ricorda che ogni domanda ha al più una risposta corretta.

L’assegnazione dei punti alle risposte è la seguente.

- Verranno attribuiti 2 punti per ogni risposta esatta;
- -0.4 punti per ogni risposta errata;
- 0 punti per ogni risposta omessa.

Al fine del superamento della soglia è necesssario totalizzare un punteggio di almeno 5 punti.

**(a)** Un ciclo for è un costrutto di iterazione

- Indeterminato

- Determinato  ✅

- Ciclico

Un ciclo for è un costrutto di iterazione **determinato** poichè il numero di iterazioni è noto prima dell’inizio del ciclo stesso.

Un costrutto di iterazione indeterminato è un costrutto dove invece il numero di iterazioni non è noto prima dell’inizio del ciclo, come ad esempio un ciclo **while**. 

Infine un costrutto di iterazione ciclico è un costrutto che si ripete un numero infinito di volte, come ad esempio un ciclo **while(true)**.

**(b)** Una costante in Java è indicata dal modificatore

- static

- abstract

- final ✅

Il modificatore **final** può essere utilizzato per dichiarare una costante, ovvero una variabile il cui valore non può essere modificato una volta inizializzato.

Il modificatore **static** invece indica che una variabile o un metodo appartiene alla classe, piuttosto che a un’istanza della stessa.

Ciò significa che una variabile **static** è condivisa tra tutte le istanze della classe e può essere acceduta senza creare un’istanza della classe.

Infine, il modificatore **abstract** indica che una classe o un metodo sono incompleti e devono essere estesi o implementati da una classe figlia.

**(c)** I metodi di un’interfaccia sono

- protected

- public ✅

- private

In Java, tutti i metodi di un’interfaccia sono implicitamente **public** e **abstract**.

Ciò significa che i metodi di un’interfaccia devono essere implementati dalle classi che implementano l’interfaccia e possono essere invocati da qualsiasi classe.

**(d)** Il contenuto di due stringhe è confrontabile tramite il metodo

- *compareTo*

- *equals* ✅

- *corresponds*

Il metodo [*equals*](https://www.programiz.com/java-programming/library/string/equals) della classe *String* viene utilizzato per confrontare il contenuto di due stringhe e determinare se sono uguali.

Il metodo [*compareTo*](https://www.programiz.com/java-programming/library/string/compareto) invece viene utilizzato per confrontare due stringhe in base all’ordine lessicografico, se ad esempio la prima stringa è minore della seconda, il metodo restituisce un valore negativo.

Infine, il metodo *corresponds* non esiste ne nella classe *String* ne in nessun’altra classe di Java.

**(e)** Un metodo static può essere accessibile tramite

- la sua classe ✅
- il suo oggetto
- l’uso di alcun modificatore di visibilità

In Java, un metodo **static** può essere accessibile tramite la sua classe.

Un metodo **static** è un metodo che appartiene a una classe piuttosto che a un'istanza di una classe (rispetto a un suo oggetto).

Il metodo è accessibile a ogni istanza di una classe e può essere rappresentato come *ClassName.methodName(arguments)*.

## Esercizio 2

Qual è la differenza tra overloading e overriding?

Fornire un esempio minimale, scritto in Java, che descriva quanto richiesto

L’overloading è un meccanismo che permette di definire più metodi con lo stesso nome ma con firme diverse, dove per firma s'intende il tipo di valore di ritorno della funzione e/o il tipo e il numero di parametri passati al metodo.


```java
public class Overloading {

    // definisco per la prima volta il metodo sum con due parametri interi
    public static int sum(int a, int b) {
        return a + b;
    }

    // primo esempio di overloading
    // definisco il metodo sum con tre parametri interi
    public static int sum(int a, int b, int c) {
        return a + b + c;
    }

    // secondo esempio di overloading
    // definisco il metodo sum con due parametri double
    public static double sum(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        // invoco il metodo sum con due parametri interi
        System.out.println(sum(1, 2));

        // invoco il metodo sum con tre parametri interi
        System.out.println(sum(1, 2, 3));

        // invoco il metodo sum con due parametri double
        System.out.println(sum(1.0, 2.0));
    }
}
```

L’overriding, invece, è un meccanismo che permette di ridefinire un metodo già definito in una classe padre all’interno di una classe figlia.

```java
public class Overriding {

    // definisco il metodo sum con due parametri interi
    public static int sum(int a, int b) {
        return a + b;
    }
}

public class OverridingChild extends Overriding {

    // esempio di overriding
    // ridefinisco il metodo sum con due parametri interi cambiandone il comportamento
    // ad esempio aggiungendo 1 al risultato
    public static int sum(int a, int b) {
        return a + b + 1;
    }

    public static void main(String[] args) {
        // invoco il metodo ridefinito sum con due parametri interi
        System.out.println(sum(1, 2));
    }
}
```

## Esercizio 3

Per ogni costrutto iterativo, indicare il numero di volte per il quale viene eseguito il suo corpo.

Se non diversamente indicato, si assume che la variabile contatore non venga modificata all’interno del
corpo di ciascun costrutto iterativo.

```java
for(int i = 12; i <= 7; i++) {...}  // (a)
for(int i = 0; i < 10; i++) {...}  // (b)
for(int i = -10; i >= 0; i++) {...}  // (c)
for(int i = -2; i >= 0; i++) {...}  // (d)
for(int i = -8; i <= 3; i = i + 4) {...}  // (e)
for (int k = 0; k < 20; k+=2) {          // (f)
    if (k + 3 == 1) {
        System.out.println(k + " ");
    }
}
```

- il corpo del costrutto iterativo **(a)** non verrà mai eseguito (quindi verrà eseguito 0 volte) poichè la condizione del ciclo è falsa già al primo controllo.

- il corpo del costrutto iterativo **(b)** verrà eseguito 10 volte con i valori di $i$ uguali a $0, 1, 2, 3, 4, 5, 6, 7, 8, 9$.

- il corpo del costrutto iterativo **(c)** non verrà mai eseguito (quindi verrà eseguito 0 volte) poichè la condizione del ciclo è falsa già al primo controllo.

- il corpo del costrutto iterativo **(d)** non verrà mai eseguito (quindi verrà eseguito 0 volte) poichè la condizione del ciclo è falsa già al primo controllo.

- il corpo del costrutto iterativo **(e)** verrà eseguito 3 volte con i valori di $i$ uguali a $-8, -4, 0$.

- il corpo del costrutto iterativo **(f)** verrà eseguito 10 volte con i valori di $k$ uguali a $0, 2, 4, 6, 8, 10, 12, 14, 16, 18$.

## Esercizio 4

Spiegare le principali differenze tra ArrayList e Set in Java.

| Differenze | ArrayList | Set |
| :---: | :---: | :---: |
| **Ordine degli elementi** | Gli elementi sono ordinati | Gli elementi non sono ordinati |
| **Elementi duplicati** | Gli elementi possono essere duplicati | Gli elementi non possono essere duplicati |
| **Accesso agli elementi** | Gli elementi sono accessibili tramite indice | Gli elementi sono accessibili tramite iterazione |
| **Implementazione** | ArrayList è implementata tramite array | Set è implementata tramite hash table |

## Esercizio 5

Realizzare la classe *Customer* al fine di gestire le informazioni relative ad un cliente di una campagna di promozione commerciale.

Tale campagna si articola in questo modo:

dopo aver effettuato una serie di acquisti per almeno $100\$$, il cliente riceverà uno sconto di $10\$$ sull’acquisto successivo.

Progettare quindi i seguenti metodi:
```java
public void makePurchase(double amount) // registra un acquisto
public boolean discountReached() // true se e solo se l’utente ha raggiunto lo sconto
```

Al fine di verificare la correttezza delle propria implementazione, si realizzi un programma di collaudo (test).

Esso dovrà rappresentare la seguente situazione:

un utente dovrà ottenere uno sconto, il quale
lo utilizzerà per fare degli acquisti.

L’importo totale derivante da tali acquisti dovrà essere maggiore di
$90\$$ ma minore di $100\$$ in modo tale da non poter ottenere uno sconto.

Successivamente, l’utente dovrà effettuare un altro acquisto, il quale lo porterà a godere dello sconto sull’acquisto successivo.

```java
public class Customer {

    private double costoTotale;
    private boolean scontoRaggiunto;

    public Customer() {
        this.costoTotale = 0;
        this.scontoRaggiunto = false;
    }

    public void makePurchase(double amount) {

        if (this.scontoRaggiunto) {
            this.costoTotale += amount - 10;
        } else {
            this.costoTotale += amount;
        }

        if (this.costoTotale > 90 && this.costoTotale < 100) {
            this.scontoRaggiunto = false;
        } else if (this.costoTotale >= 100) {
            this.scontoRaggiunto = true;
        }
    }

    public boolean discountReached() {
        return this.scontoRaggiunto;
    }
```

```java
public class CustomerTest {

    public static void main(String[] args) {

        Customer cliente = new Customer();

        cliente.makePurchase(50);
        cliente.makePurchase(50);
        cliente.makePurchase(50);

        System.out.println(cliente.discountReached()); // false

        customer.makePurchase(50);

        System.out.println(cliente.discountReached()); // true
    }
}
```

## Esercizio 6

Un supermercato ha accesso ad un database contenente tutte le informazioni sui propri prodotti.

Tali informazioni sono rappresentate in formato tabellare, in cui ciascuna riga contiene i seguenti campi
separati da uno spazio:

<p align="center"> codiceProdotto1 NomeProdotto1 Quantità1 PrezzoPerUnità1 <br> codiceProdotto2 NomeProdotto2 Quantità2 PrezzoPerUnità2 <br> . . . </p>

Scrivere un programma che legga un file di testo con questa struttura, segnalando un opportuno errore in caso di file inesistente.

Successivamente, visualizzare:
- Le informazioni relative al prodotto più costoso;
- Il prezzo medio per ciascun prodotto, calcolato come il rapporto tra prezzo per unità e la quantità disponibile. Gestire gli eventuali casi speciali
- I nomi dei prodotti esauriti, ossia con una quantità pari a zero

```java
public class Prodotto {

    private String codice;
    private String nome;
    private int quantita;
    private double prezzoPerUnita;

    public Prodotto(String codice, String nome, int quantita, double prezzoPerUnita) {
        this.codice = codice;
        this.nome = nome;
        this.quantita = quantita;
        this.prezzoPerUnita = prezzoPerUnita;
    }

    public String getCodice() {
        return codice;
    }

    public String getNome() {
        return nome;
    }

    public int getQuantita() {
        return quantita;
    }

    public double getPrezzoPerUnita() {
        return prezzoPerUnita;
    }

    public double getPrezzoMedio() {
        return this.prezzoPerUnita / this.quantita;
    }

    @Override
    public String toString() {
        return "Prodotto{" +
                "codice='" + codice + '\'' +
                ", nome='" + nome + '\'' +
                ", quantita=" + quantita +
                ", prezzo per unità=" + prezzo +
                '}';
    }
}
```

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class SuperMercato {
    public static void main(String[] args) {

        // utilizzo un ArrayList per memorizzare i prodotti
        // memorizzandoli come oggetti della classe Prodotto
        ArrayList<Prodotto> prodotti = new ArrayList<>();
        try {

            // provo ad aprire il file
            File file = new File("prodotti.txt");
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {

                // leggo ogni riga del file
                // e la divido in base agli spazi
                // salvando separatamente ogni campo
                String[] line = scanner.nextLine().split(" ");
                String codice = line[0];
                String nome = line[1];
                int quantita = Integer.parseInt(line[2]);
                double prezzoPerUnita = Double.parseDouble(line[3]);

                // ragguppandoli sotto forma di oggetto della classe Prodotto
                prodotti.add(new Prodotto(codice, nome, quantita, prezzoPerUnita));
            }

            // finito di leggere il file, chiudo lo scanner
            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("File non trovato");
        }

        // una volta registrati tutti i prodotti
        // eseuguo le operazioni richieste

        // individuo il prodotto più costoso
        Prodotto prodottoPiuCostoso = prodotti.get(0);
    
        for (Prodotto prodotto : prodotti) {
            if (prodotto.getPrezzoPerUnita() > prodottoPiuCostoso.getPrezzoPerUnita()) {
                prodottoPiuCostoso = prodotto;
            }
        }

        // e lo stampo
        // nota: il metodo toString() viene invocato automaticamente
        // quando si stampa un oggetto, utilizzando l'overriding
        // lo si è personalizzato secondo le esigenze dell'esercizio
        System.out.println("Prodotto più costoso: " + prodottoPiuCostoso);

        // stampo il prezzo medio di ogni prodotto
        for (Prodotto prodotto : prodotti) {
            System.out.println("Prezzo medio di " + prodotto.getNome() + ": " 
                                + prodotto.getPrezzoMedio());
            }

        // infine, stampo i nomi dei prodotti esauriti
        for (Prodotto prodotto : prodotti) {
            if (prodotto.quantita == 0) {
                System.out.println(prodotto.getNome() + " è esaurito");
            }
        }
    }
}
```

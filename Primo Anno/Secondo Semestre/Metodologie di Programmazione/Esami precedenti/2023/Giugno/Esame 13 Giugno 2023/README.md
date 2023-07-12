# <p align= "center"> Esame 13 Giugno 2023 </p>

## Esercizio 1

Per ogni domanda, indicare con una X la risposta desiderata.

Si ricorda che ogni domanda ha al più una risposta corretta.

L’assegnazione dei punti alle risposte è la seguente:

- verranno attribuiti 2 punti per ogni risposta esatta,
- -0.75 punti per ogni risposta errata,
- 0 punti per ogni risposta omessa.

Al fine del superamento della soglia è necessario totalizzare un punteggio di almeno 5 punti.

**(a)** Quale dei seguenti è un esempio corretto di creazione di una sottoclasse in Java?

- *class* **MyFrame** *extends* **Jframe** ✅

- *private* *interface* **JFrame** *implements* **MyFrame**

- *public* **MyFrame** *implements* **Jframe**

La risposta corretta è "*class* **MyFrame** *extends* **Jframe**".

Per creare una sottoclasse in Java si usa la parola chiave *extends* e non *implements*, usata invece per implementare un'interfaccia.

**(b)** Lo statement "*new String[] {"Metodologie", "Di", "Programmazione"};*":

- Non è sintatticamente corretto 

- Crea un array anonimo con tre elementi di tipo String ✅

- Crea una array chiamato String con tre elementi

La risposta corretta è "Crea un array anonimo con tre elementi di tipo String".

Per creare un array anonimo si usa la sintassi "*new tipo[] {elementi*}*",
dove per anonimo si intende che non viene assegnato ad una variabile, quindi non ha un nome a cui fare riferimento.

Può essere utile ad esempio per passare un array come parametro ad un metodo
senza doverlo creare prima e assegnarlo ad una variabile.

```java
public static void stampaArray(String[] array) {
    for (String elemento : array) {
        System.out.println(elemento);
    }
}

public static void main(String[] args) {
    stampaArray(new String[] {"Metodologie", "Di", "Programmazione"});
}

/* 
Output:
    Metodologie
    Di
    Programmazione
*/
```

**(c)** l’uso dell’istruzione “*break*” in un blocco “*switch*”:

- Permette di continuare l’esecuzione del blocco

- Interrompe l’esecuzione del blocco ✅

- Nessuna delle precedenti

La risposta corretta è "Interrompe l’esecuzione del blocco".

In un blocco *switch*, l'istruzione *break* serve per interrompere l'esecuzione del blocco passando all'istruzione successiva ad esso, altrimenti verrebbe eseguito anche tutto il codice successivo al *case* che ha soddisfatto la condizione del blocco prima di passare all'istruzione successiva al blocco.

**(d)** Le code convention in Java prevedono che:

- Il nome delle classi cominci con lettera minuscola, mentre quello dei metodi con la maiuscola
- Il nome delle classi cominci con lettera maiuscola, mentre quello dei metodi con la minuscola ✅
- Non esiste alcuna convenzione a riguardo

L’opzione corretta è "Il nome delle classi cominci con lettera maiuscola, mentre quello dei metodi con la minuscola".

In Java, le *code convention* prevedono che il nome delle classi cominci con una lettera maiuscola (ad esempio, *MyClass*) mentre il nome dei metodi cominci con una lettera minuscola (ad esempio, *myMethod*).

**(e)** Il metodo *public* *static* *Class* **forName(*String* className)**:

- Restituisce l’oggetto *Class* che rappresenta la classe dal nome **className** ✅

- Non restituisce alcun valore

- Restituisce un oggetto *Object*

La risposta corretta è "Restituisce l’oggetto *Class* che rappresenta la classe dal nome **className**".

Il metodo *forName*, ha come tipo di ritorno un oggetto *Class* e come riportato nella [documentazione ufficiale](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)

"Restituisce l'oggetto *Class* associato alla classe o all'interfaccia con il nome di stringa specificato (className)". 

## Esercizio 2

Qual è la differenza tra eccezione controllata e non controllata?

Fornire un esempio per ognuno dei due tipi e una porzione di codice, scritta in Java, che mostri il meccanismo di gestione di uno di essi

Le eccezioni controllate sono quelle verificate dal compilatore, che controllerà che non vengano ignorate.

La classe *IOException* è tutte le sue sottoclassi sono eccezioni controllate.

```java
import java.io.FileReader;
import java.io.IOException;

public class EccezioneControllata {
    public static void main(String[] args) {
        try {
            FileReader reader = new FileReader("file.txt");
        } catch (IOException e) {
            System.out.println("Errore durante l'apertura del file: " + e.getMessage());
        }
    }
}
```

Le eccezioni non controllate, invece, non sono gestite controllate dal compilatore ma dal programmatore stesso.

La classe *RuntimeException*, la classe *Error* e tutte le loro sottoclassi sono eccezioni non controllate.

```java
public class EccezioneNonControllata {
    public static void main(String[] args) {
        int[] array = new int[5];
        try {
            int x = array[5];
        } catch (ArrayIndexOutOfBoundsException e) {
            System.err.println("Errore: indice dell'array fuori dai limiti");
        }
    }
}
```

## Esercizio 3

Per ogni costrutto iterativo, indicare il numero di volte per il quale viene eseguito il suo corpo.

Se non diversamente espresso, si assume che la variabile contatore non venga modificata all’interno del corpo di ciascun costrutto iterativo.

```java
for (int i = 1; i <= 5; i++){...} // (a)
for (int i = 10; i >= 0; i -= 2){...} // (b)
for (int i = 100; i > 0; i /= 2){...} // (c)
for (int i = 2; i < 1000; i *= 2){...} // (d)
for (int i = 0; i <= 100; i += 10){...} // (e)
for (int i = 50; i >= -10; i -= 5){...} // (f)
```

- il corpo del costrutto iterativo **(a)** verrà eseguito 5 volte, con i che assumerà i valori $1, 2, 3, 4, 5$

- il corpo del costrutto iterativo **(b)** verrà eseguito 6 volte, con i che assumerà i valori $10, 8, 6, 4, 2, 0$

- il corpo del costrutto iterativo **(c)** verrà eseguito 7 volte, con i che assumerà i valori $100, 50, 25, 12, 6, 3, 1$

- il corpo del costrutto iterativo **(d)** verrà eseguito 9 volte, con i che assumerà i valori $2, 4, 8, 16, 32, 64, 128, 256, 512$

- il corpo del costrutto iterativo **(e)** verrà eseguito 11 volte, con i che assumerà i valori $0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100$

- il corpo del costrutto iterativo **(f)** verrà eseguito 13 volte, con i che assumerà i valori $50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10$

## Esercizio 4

Spiegare le principali differenze tra *LinkedList* e *ArrayList* in Java, evidenziando gli scenari in cui è meglio utilizzare ognuna delle due classi.

| Differenze | ArrayList | LinkedList |
| :----: | :----: | :----: |
| Implementazione | basato su array con dimensione variabile | basata su una lista di nodi collegati da puntatori |
| Accesso agli elementi | più veloce | più lento |
| Inserimento e cancellazione di elementi | più lento | più veloce |
| Occupazione spazio di memoria | occupa meno spazio | occupa più spazio |
| Scenari Migliori | quando si devono effettuare molte operazioni di lettura | quando si devono effettuare molte operazioni di inserimento e cancellazione |

## Esercizio 5

La classe *BankAccount* gestisce le informazioni relative ai conti bancari.

Il conto viene creato con un saldo iniziale e consente operazioni di prelievo e deposito.

Nel caso in cui il saldo del conto superi una una determinata soglia, il sistema applica un interesse al saldo attuale.

Progettare i seguenti metodi:
```java
// effettua un deposito
public void deposit(double amount)

// effettua un prelievo, restituisce true se il prelievo ha avuto successo, altrimenti false
public boolean withdraw(double amount)

// applica l’interesse all’importo presente sull’account se il saldo supera una soglia specifica
public void applyInterest(double interestRate)
```
Realizzare un programma di collaudo (test) per verificare la correttezza dell’implementazione.

Il programma dovrà creare un conto con un saldo iniziale di $\$500$, effettuare un prelievo di $\$200$, un deposito di $\$100$ e applicare un interesse del $5\%$ all’importo presente sul conto se il saldo supera $\$1000$.

```java
public class BankAccount {
    private double balance;

    public BankAccount(double balance) {
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public boolean withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            return true;
        } else {
            return false;
        }
    }

    public void applyInterest(double interestRate) {
        if (balance > 1000) {
            balance += balance * (interestRate / 100)
        }
    }

    public double getBalance() {
        return balance;
    }
}
```

```java
public class TestBankAccount {
    public static void main(String[] args) {
        BankAccount account = new BankAccount(500);
        account.withdraw(200);
        account.deposit(100);
        account.applyInterest(5);
        System.out.println(account.getBalance());
    }
}
```

## Esercizio 6

Un negozio di abbigliamento tiene traccia delle informazioni sui propri prodotti attraverso un file di testo.

Ciascuna riga del file contiene i seguenti campi separati da una virgola:

<p align="center">  nomeProdotto1,categoria1,prezzo1 <br> nomeProdotto2, categoria2,prezzo2 <br> . . . </p>

Scrivere un programma che legga un file di testo con questa struttura, segnalando un opportuno errore in caso di file inesistente.

Successivamente, visualizzare:
- La lista dei prodotti nella categoria Shoes;
- Il prezzo medio dei prodotti nella categoria Pants;
- Il nome del prodotto più costoso.

Scrivere un programma di collaudo (test) che utilizzi le classi create in precedenza.

Si assume che il formato di ciascuna riga sia sempre corretto

```java
public class Prodotto {
    private String nome;
    private String categoria;
    private double prezzo;

    public Prodotto(String nome, String categoria, double prezzo) {
        this.nome = nome;
        this.categoria = categoria;
        this.prezzo = prezzo;
    }

    public String getNome() {
        return nome;
    }

    public String getCategoria() {
        return categoria;
    }

    public double getPrezzo() {
        return prezzo;
    }
}
```

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class TestProdotto {
    public static void main(String[] args) {
        // utilizzo un ArrayList per memorizzare i prodotti
        // poichè un ArrayList ha una dimensione variabile
        // e permette di memorizzare oggetti all'interno di esso
        ArrayList<Prodotto> ListaProdotti = new ArrayList<>();
        try {
            // provo ad aprire il file
            // gestendo il caso in cui il file non esista
            File file = new File("prodotti.txt");

            // se il file è stato aperto correttamente
            // leggo il file riga per riga
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                String riga = scanner.nextLine();

                // divido la riga in base al carattere ','
                // cosi da avere ogni campo separato in una lista
                String[] CampiRiga = riga.split(",");
                // per poi creare un nuovo oggetto Prodotto
                // assegnandogli i correcti parametri
                String NomeProdotto = CampiRiga[0];
                String CategoriaProdotto = CampiRiga[1];
                double PrezzoProdotto = Double.parseDouble(CampiRiga[2]);
                ListaProdotti.add(new Prodotto(NomeProdotto, CategoriaProdotto, PrezzoProdotto));
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            System.err.println("Errore: file non trovato");
        }

        // finito di leggere il file, si procede con le operazioni richieste

        // visualizzo la lista dei prodotti nella categoria Shoes
        System.out.println("Lista dei prodotti nella categoria Shoes:");
        for (Prodotto prodotto : ListaProdotti) {
            if (prodotto.getCategoria().equals("Shoes")) {
                System.out.println(prodotto.getNome());
            }
        }

        // calcolo il prezzo medio dei prodotti nella categoria Pants
        double SommaPrezzoProdottiPants = 0;
        int NumeroProdottiPants = 0;
        for (Prodotto prodotto : ListaProdotti) {
            if (prodotto.getCategoria().equals("Pants")) {
                SommaPrezzoProdottiPants += prodotto.getPrezzo();
                NumeroProdottiPants++;
            }
        }

        System.out.println("Prezzo medio dei prodotti nella categoria Pants: " 
                            + SommaPrezzoProdottiPants / NumeroProdottiPants);

        // trovo il prodotto più costoso
        Prodotto ProdottoPiuCostoso = ListaProdotti.get(0);
        for (Prodotto prodotto : ListaProdotti) {
            if (prodotto.getPrezzo() > ProdottoPiuCostoso.getPrezzo()) {
                ProdottoPiuCostoso = prodotto;
            }
        }

        // e ne stampo il nome
        System.out.println("Prodotto più costoso: " + ProdottoPiuCostoso.getNome());
    }
}
```

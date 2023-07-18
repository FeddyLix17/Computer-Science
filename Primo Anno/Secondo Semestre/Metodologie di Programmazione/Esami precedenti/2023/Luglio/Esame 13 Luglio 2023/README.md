# <p align="center"> Esame 13 Luglio 2023 </p>

## Esercizio 1

Per ogni domanda, indicare con una X la risposta desiderata.

Si ricorda che ogni domanda ha al più una risposta corretta.

L’assegnazione dei punti alle risposte è la seguente:

- verranno attribuiti 2 punti per ogni risposta esatta,

- -0.75 punti per ogni risposta errata,

- 0 punti per ogni risposta omessa.

Al fine del superamento della soglia è necessario totalizzare un punteggio di almeno 5 punti.

---
**(a)** Quale dei seguenti è un esempio corretto di creazione di un oggetto in Java utilizzando il costruttore di una classe?

- *MyClass obj = new MyClass();* ✅

- *MyClass obj = createObject();*

- *MyClass obj = MyClass.create();*

In java la sintassi per creare un oggetto utilizzando il costruttore di una classe è la seguente:


*NomeClasse nomeOggetto = new NomeClasse();*

---
**(b)** Qual è il risultato dell’esecuzione del seguente codice Java?

```java
int x = 5;
int y = x++;
System.out.println(x + ”, ” + y);
```

- 5, 5

- 5, 6

- 6, 5 ✅

La soluzione corretta è 6, 5 poiché come riportato anche da altre [fonti](https://stackoverflow.com/questions/1094872/is-there-a-difference-between-x-and-x-in-java), il comportamento del codice sarà il seguente:

- *int x = 5;* assegna alla variabile x il valore 5

- *int y = x++;* assegna alla variabile y il valore di x (5), **incrementando successivamente** il valore di x di 1 (6)

- *System.out.println(x + ”, ” + y);* stampa a video il valore di x (6) e il valore di y (5)

---

**(c)** Qual'è l’output del seguente codice Java?

```java
String str = "Hello";
str.concat(" World");
System.out.println(str);
```

- Hello World

- World Hello

- Hello ✅

L'output del codice Java fornito sarà *Hello*.

Il metodo [*concat*](https://www.w3schools.com/java/ref_string_concat.asp) restituisce una nuova stringa rappresentante la concatenazione della stringa originale e della stringa specificata come argomento, **non modificando la stringa originale**.

Nel codice fornito, il risultato del metodo *concat* non viene assegnato a nessuna variabile, quindi la stringa originale *str* rimane invariata.

Esempio:

Se invece di *str.concat(" World");* l'istruzione fosse stata *str = str.concat(" World");*, l'output sarebbe stato uguale a *Hello World*.

---

**(d)** Qual è il modificatore di accesso di default per i membri di una classe in Java?

- public

- private

- protected

- nessuno dei precedenti ✅

Se non viene specificato esplicitamente alcun modificatore di accesso, in questo caso la risposta corretta sarà *nessuno dei precedenti*.

Questo perchè quando non viene assegnato alcun modificatore di accesso per un membro di una classe, verrà assegnato automaticamente il modificatore di accesso *default*, che consente l'accesso solo all'interno dello stesso pacchetto.

Ciò significa che i membri con il modificatore di accesso *default* possono essere accessibili solo dalle classi all'interno dello stesso pacchetto, ma non da classi in pacchetti diversi.

---

**(e)** Qual è la differenza tra un’interfaccia e una classe astratta in Java?

- Un’interfaccia può implementare metodi, mentre una classe astratta no.

- Una classe astratta può essere istanziata, mentre un’interfaccia no.

- Una classe può implementare più interfacce, ma può estendere solo
una classe astratta ✅

La risposta corretta è la terza perché una classe può effettivamente implementare più interfacce, ma può estendere solo una classe astratta.

Questo significa che una classe può ereditare comportamenti da più interfacce, ma solo da una singola classe astratta.

La prima risposta non è corretta perché un'[interfaccia](https://www.andreaminini.com/java/le-interfacce-in-java) non può implementare metodi, ma solo dichiararli.

La seconda risposta non è corretta perché una [classe astratta](https://www.html.it/pag/51820/classi-astratte-in-java/) non può essere istanziata direttamente.

Solo le sue sottoclassi concrete (cioè le classi che estendono la classe astratta e implementano tutti i suoi metodi astratti) possono essere istanziate.

---

## Esercizio 2

Descrivi il concetto di Ereditarietà e fornisci un esempio di utilizzo minimale scritto in Java.

L'ereditarietà è un concetto riguardante la possibilità di creare nuove classi basate su classi esistenti.

Con l'ereditarietà, una classe (nota come classe figlia) può ereditare caratteristiche (metodi e attributi) di un'altra classe (nota come classe padre) aggiungendo opzionalmente nuove funzionalità o modificarle.

Questo favorisce la creazione di una struttura gerarchica delle classi, che offre la possibilità di riutilizzare il codice esistente, organizzare il codice in modo più efficiente e implementare concetti come l'astrazione e la generalizzazione.

```java
class Veicolo {
    private String marca;

    public Veicolo(String marca) {
        this.marca = marca;
    }

    public void accendi() {
        System.out.println("Il veicolo si sta avviando");
    }
}

class Auto extends Veicolo {
    private int numeroPorte;

    public Auto(String marca, int numeroPorte) {
        super(marca);
        this.numeroPorte = numeroPorte;
    }

    public void apriPorte() {
        System.out.println("Apertura delle " + numeroPorte + " porte dell'auto");
    }
}

public class EreditarietaEsempio {
    public static void main(String[] args) {
        Auto auto = new Auto("Fiat", 4);
        auto.avvia();    // Richiama il metodo della superclasse
        auto.apriPorte();
    }
}
```

## Esercizio 3

Qual è la differenza tra il passaggio di parametri per valore e il passaggio di parametri per riferimento in Java?

Fornisci un esempio minimale, scritto in Java, per ognuno dei due casi.

La differenza tra i 2 tipi di passaggio di parametri risiede nel tipo di dato passato al metodo.

- Se il parametro passato al metodo è di un tipo **primitivo** (*int, char, boolean, ecc.*), allora il passaggio avviene per valore. <br> In questo caso, il valore della variabile viene copiato e passato al metodo, quindi eventuali modifiche al valore del parametro all'interno del metodo non influiranno anche sul valore della variabile al di fuori del metodo.

- Se il parametro passato al metodo è di un tipo **non primitivo** (*oggetti, array, ecc.*), allora il passaggio avviene per riferimento, dove per riferimento si intende il puntatore all'oggetto o all'array. <br> Eventuali modifiche al valore del parametro all'interno del metodo influiranno anche sul valore della variabile al di fuori del metodo.

```java
public class PassaggioPerValore {

    public static void main(String[] args) {
        int x = 5;
        System.out.println("Valore di x prima di chiamare il metodo: " + x);
        increment(x);
        System.out.println("Valore di x dopo aver chiamato il metodo: " + x);
    }

    public static void increment(int x) {
        x++;
        System.out.println("Valore di x all'interno del metodo: " + x);
    }
}

/*
    Valore di x prima di chiamare il metodo: 5
    Valore di x all'interno del metodo: 6
    Valore di x dopo aver chiamato il metodo: 5
*/
```

```java
public class PassaggioPerRiferimento {

    public static void main(String[] args) {
        int[] x = {5};
        System.out.println("Valore di x prima di chiamare il metodo: " + x[0]);
        increment(x);
        System.out.println("Valore di x dopo aver chiamato il metodo: " + x[0]);
    }

    public static void increment(int[] x) {
        x[0]++;
        System.out.println("Valore di x all'interno del metodo: " + x[0]);
    }
}

/*
    Valore di x prima di chiamare il metodo: 5
    Valore di x all'interno del metodo: 6
    Valore di x dopo aver chiamato il metodo: 6
*/
```

## Esercizio 4

Descrivi brevemente il *Single Responsibility Principle (SRP)* appartenente ai principi *SOLID*.

A seguire, fornisci un esempio minimale di tale principio, scritto in Java.

Il Single Responsibility Principle (SRP) afferma che una classe dovrebbe avere dovrebbe avere solo una responsabilità, ovvero dovrebbe occuparsi solo di una parte specifica delle funzionalità di un'applicazione e non dovrebbe essere sovraccaricata con troppe *"responsabilità"*.

Ciò aiuta a mantenere il codice pulito, leggibile e facile da mantenere.

Quando ogni classe ha solo una responsabilità, è più facile capire cosa fa quella classe e come interagisce con le altre classi.

Inoltre, quando si apportano modifiche a una parte specifica dell'applicazione, si deve modificare solo la classe responsabile di quella funzionalità, il che riduce il rischio di introdurre errori in altre parti del codice.

```java
public class Utente {
    private String nome;
    private String email;

    public Utente(String nome, String email) {
        this.nome = nome;
        this.email = email;
    }

    public void setEmail(String nuovaEmail) {
        this.email = nuovaEmail;
    }
}

public class ServizioEmail {

    public void inviaEmail(String destinatario, String oggetto, String messaggio) {
        // Codice per inviare un'email
    }
}
```

In questo esempio, si hanno due classi: 

- La classe *User*, con la responsabilità di gestire le informazioni relative a un utente (come ad esempio il nome e l'indirizzo email)

- La classe *EmailService*, con la responsabilità di inviare email

Ogni classe quandi ha solo una responsabilità e non è sovraccaricata con troppe funzionalità.

## Esercizio 5

Si desidera creare un sistema per gestire una libreria online con le seguenti classi e interfacce:

- **Pubblicazione**: un’interfaccia che definisce il metodo *calcolaPrezzo()* per calcolare il prezzo di una pubblicazione

- **Libro**: una classe che rappresenta un libro con gli attributi titolo, autore e prezzo. <br> La classe deve implementare l’interfaccia **Pubblicazione**

- **Rivista**: una classe che rappresenta una rivista con gli attributi titolo, editore e numero. <br> La classe deve implementare l’interfaccia **Pubblicazione**

- **LibreriaOnline**: una classe che gestisce una collezione di pubblicazioni. <br> Deve avere
    - un metodo *aggiungiPubblicazione(Pubblicazione pubblicazione)* per aggiungere una pubblicazione alla libreria 
    - e un metodo *calcolaPrezzoTotale()* per calcolare il prezzo totale di tutte le pubblicazioni nella libreria.

Scrivi un programma in Java che implementi quanto richiesto e crea un programma di collaudo per verificarne il funzionamento.

```java
public interface Pubblicazione {
    double calcolaPrezzo();
}
```

```java
public class Libro implements Pubblicazione {
    private String titolo;
    private String autore;
    private double prezzo;

    public Libro(String titolo, String autore, double prezzo) {
        this.titolo = titolo;
        this.autore = autore;
        this.prezzo = prezzo;
    }

    @Override
    public double calcolaPrezzo() {

        // durante l'esame ci è stato detto che il prezzo
        // può essere calcolato nel modo che si preferisce
        return prezzo + 42;
    }
}
```

```java
public class Rivista implements Pubblicazione {
    private String titolo;
    private String editore;
    private int numero;
    private double prezzo;

    public Rivista(String titolo, String editore, int numero, double prezzo) {
        this.titolo = titolo;
        this.editore = editore;
        this.numero = numero;
        this.prezzo = prezzo;
    }

    @Override
    public double calcolaPrezzo() {

        // durante l'esame ci è stato detto che il prezzo
        // può essere calcolato nel modo che si preferisce
        return prezzo + 420;
    }
}
```

```java
import java.util.ArrayList;

public class LibreriaOnline {
    private ArrayList<Pubblicazione> pubblicazioni;

    public LibreriaOnline() {
        this.pubblicazioni = new ArrayList<>();
    }

    public void aggiungiPubblicazione(Pubblicazione pubblicazione) {
        pubblicazioni.add(pubblicazione);
    }

    public double calcolaPrezzoTotale() {
        double prezzoTotale = 0;
        for (Pubblicazione pubblicazione : pubblicazioni) {
            prezzoTotale += pubblicazione.calcolaPrezzo();
        }
        return prezzoTotale;
    }
}
```

```java
public class LibreriaOnlineTest {
    public static void main(String[] args) {
        LibreriaOnline libreria = new LibreriaOnline();

        Libro libro1 = new Libro("Il signore degli anelli", "J.R.R. Tolkien", 20);
        Libro libro2 = new Libro("Il ritratto di Dorian Gray", "Oscar Wilde", 15);
        Rivista rivista1 = new Rivista("Focus", "Mondadori", 1, 5);
        Rivista rivista2 = new Rivista("Wired", "Condé Nast", 2, 5);

        libreria.aggiungiPubblicazione(libro1);
        libreria.aggiungiPubblicazione(libro2);
        libreria.aggiungiPubblicazione(rivista1);
        libreria.aggiungiPubblicazione(rivista2);

        System.out.println("Prezzo totale: " + libreria.calcolaPrezzoTotale());
    }
}

/*
    Prezzo totale: 969.0
*/
```

## Esercizio 6

Scrivere un programma in Java il quale, dato uno stack, rimuova i duplicati al suo interno.

**Nota Bene**: è sconsigliata la lavorazione diretta sullo stack di partenza.

```java
import java.util.Stack;

public class RimuoviDuplicatiStack {
    public static void main(String[] args) {

        // Creo uno stack di interi
        Stack<Integer> stack = new Stack<>();

        // Aggiungo alcuni elementi allo stack
        // (anche duplicati)
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(4);
        stack.push(3);
        stack.push(2);
        stack.push(1);
        System.out.println("Stack originale: " + stack);

        // Rimuovo i duplicati dallo stack
        rimuoviDuplicati(stack);
        System.out.println("Stack senza duplicati: " + stack);
    }

    public static void rimuoviDuplicati(Stack<Integer> stack) {
        
        // Creo un secondo stack temporaneo
        // per salvare tutti gli elementi dello stack originale
        // una sola volta, cosi da non avere duplicati
        Stack<Integer> tempStack = new Stack<>();
        while (!stack.isEmpty()) {

            // Rimuovo l'elemento attualmente in cima allo stack originale
            int temp = stack.pop();

            // e se non è già presente nello stack temporaneo
            if (!tempStack.contains(temp)) {

                // lo aggiungo in cima allo stack temporaneo
                tempStack.push(temp);
            }
        }

        // A questo punto lo stack originale è vuoto
        // e nello stack temporaneo sono presenti tutti gli elementi
        // dello stack originale senza duplicati

        // Trasferisco tutti gli elementi dallo stack temporaneo
        // allo stack originale
        while (!tempStack.isEmpty()) {
            stack.push(tempStack.pop());
        }
    }
}

/*
    Stack originale: [1, 2, 3, 4, 4, 3, 2, 1]
    Stack senza duplicati: [1, 2, 3, 4]
*/
```

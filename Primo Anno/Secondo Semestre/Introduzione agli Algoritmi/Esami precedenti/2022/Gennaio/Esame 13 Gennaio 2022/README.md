# <p align="center"> Esame 13 Gennaio 2022 </p>

## Esercizio 1

Si consideri la seguente funzione:

```python
def Exam(n):
    tot = n
    if n <= 1:
        return tot
    j = 80
    while j >= 3:
        tot = tot + j
        j = j − 2
    return tot + Exam(n − j)
```

**a)** Si imposti la relazione di ricorrenza che ne definisce il tempo di esecuzione giustificando dettagliatamente l’equazione ottenuta

viene raggiunto il caso base quando $\Large n <= 1$, con costo $\Large \Theta(1)$, da cui

$$
    -\Large T(n) = \Theta(1), \quad n <= 1
$$

altrimenti, il costo sarà determinato dalla chiamata ricorsiva (di cui analizzeremo il parametro successivamente) e dal ciclo while, del quale verrà studiato il comportamento di seguito

| Iterazione | 0 | 1 | 2 | 3 | $\Large \dots$ | $k$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\Large j$ | 80 | 78 | 76 | 74 | $\Large \dots$ | $\Large 80 - 2k$ |

il ciclo terminerà quando

$$
    \Large 80 - 2k < 3
$$

$$
    \Large 80 - 2k = 2
$$

$$
    \Large -2k = -78
$$

$$
    \Large k = 39
$$

il costo del ciclo sarà costante, ovvero indipendente dalla dimensione dell'input, pari a

$$
    \Large \Theta(39) \implies 39 \Theta(1) \implies \Theta(1)
$$

il costo della chiamata ricorsiva sarà determinato dal parametro $\Large n - j$, dove

$$
    \Large j = 80 - 2*39 = 80 - 78 = 2
$$

quindi il costo della chiamata ricorsiva sarà pari a

$$
    \Large T(n - j) = T(n - 2)
$$

per concludere, la relazione di ricorrenza sarà data da

$$
    \Large -T(n) = T(n - 2) + \Theta(1), \quad n > 1
$$

$$
    \Large -T(n) = \Theta(1), \quad n <= 1
$$

**b)** Si risolva la ricorrenza usando il metodo dell’albero dettagliando i passaggi del calcolo e giustiﬁcando ogni affermazione

                                            Θ(1)        T(n)
                                             /
                                            /
                                          Θ(1)          T(n - 2)
                                           /
                                          /
                                        Θ(1)           T(n - 4)
                                         /
                                        /
                                      Θ(1)             T(n - 2k)

dove k indica il livello in cui ci si trova (considerando il primo livello come livello 0)

di raggiungerà l'ultimo livello dell'albero quando

$$
    \Large n - 2k = 1
$$

$$
    \Large -2k = -n + 1
$$

$$
    \Large 2k = n - 1
$$

$$
    \Large k = \frac{n - 1}{2}
$$

il costo computazionale della funzione sarà pari a

$$
    \Large \Theta(\frac{n - 1}{2}) \implies \Theta(\frac{n}{2}) \implies \Theta(n)
$$

## Esercizio 2

Abbiamo due array ordinati *A* e *B* di n interi distinti;

si vuole sapere se esiste un valore *x* in *A* ed un valore *y* in *B* che differiscono al più 3 in valore assoluto (vale a dire $|x − y| \leq 3$).

Ad esempio:

- per *A = [1, 2, 20, 30]* e *B = [6, 7, 10]* la risposta è negativa.

- per *A = [1, 2, 9, 10, 12]* e *B = [6, 14, 16, 20]* la risposta è positiva (grazie alla coppia (9, 6) o anche (12, 14))

Progettare un algoritmo che risolva il problema restituendo 1 se la risposta è positiva, 0 altrimenti.

Il costo computazionale dell’algoritmo deve essere asintoticamente strettamente inferiore a $\Theta(n^2)$.

Dell’algoritmo proposto

**a)** si dia la descrizione a parole

Usando due indici si scorrono gli array partendo dall'estremità di destra.

Fino a quando non si raggiunge l'estremità di sinistra di uno dei due array, vengono effettuati i seguenti controlli:

- se il valore assoluto della differenza tra l'elemento puntato da *dA* e l'elemento puntato da *dB* è minore o uguale a 3, la funzione restituirà 1

- altrimenti, vuol dire che la differenza tra i 2 elementi è strettamente maggiore di 3, quindi si procede a decrementare l'indice dell'array che punta all'elemento di valore maggiore, in modo da avvicinarsi al valore dell'altro array

si decide arbitrariamente di decrementare l'indice del primo array, in caso di valori uguali puntati dagli indici.

Qualora non dovesse venire trovata nessuna coppia di valori tali che $\Large |x - y| \leq 3$, la funzione restituirà 0.

**b)** si scriva il codice in pseudocodice

```python
def es2(A, B):

    dA = len(A) - 1
    dB = len(B) - 1

    while dA >= 0 and dB >=0:

        if abs(A[dA] - B[dB]) <= 3:
            return 1
        elif A[dA] >= B[dB]:
            dA-=1
        else:
            dB-=1

    return 0
```

**c)** si giustifichi il costo computazionale

ad ogni iterazione del ciclo while, uno dei 2 indici viene decrementato di 1, il caso peggiore in cui si può incorrere è quello in cui non venga mai trovata una coppia di valori tali che $\Large |x - y| \leq 3$, compiendo cosi tutte e le $\Large 2n$ iterazioni, da cui il suo costo computazionale

$$
    \Large \Theta(2n) \implies \Theta(n)
$$

rientrando cosi nel vincolo di costo computazionale richiesto dal testo dell'esercizio.

## Esercizio 3

Si consideri una lista non vuota *L*, in cui ogni elemento è un record a due
campi,

- il campo *val* contenente un intero

- ed il campo *next* con il puntatore al nodo seguente (next vale *None* per l’ultimo record della lista).

Gli interi nella lista sono ordinati in modo non decrescente e bisogna eliminare dalla lista i record contenenti duplicati.

Si consideri ad esempio la lista *L* in ﬁgura; subito sotto viene riportato il risultato dell’operazione di cancellazione.

                        3 --> 3 --> 3 --> 4 --> 4 --> 7 --> 7 --> 7 --> 9 --> 9 --> 9 --> 9

                        3 --------------> 4 --------> 7 --------------> 9

Progettare un algoritmo iterativo che, dato il puntatore *r* alla testa
della lista effettui l’operazione di modiﬁca in tempo $\Large \Theta(n)$ dove n è il numero di elementi presenti nella lista.

Lo spazio di lavoro dell’algoritmo deve essere $O(1)$.

Dell’algoritmo proposto

**a)** si dia la descrizione a parole

Si scorre la lista partendo dalla testa, fino a quando non si raggiunge l'ultimo elemento.

Ad ogni iterazione del ciclo while, viene effettuato il seguente controllo:

- se il valore del nodo attualmente puntato da *r* è uguale al valore del suo nodo successivo, allora il nodo corrente punterà al nodo successivo del nodo successivo, in modo da eliminare il duplicato

- altrimenti, vuol dire che il valore del nodo attualmente puntato da *r* è diverso dal valore del suo nodo successivo, quindi si procede a far puntare *r* al nodo successivo (in modo da avanzare nella lista)

```python
def es3(r):
    while r.next != None:
        if r.val == r.next.val:
            r.next = r.next.next
        else:
            r = r.next
```

**c)** si giustifichi il costo computazionale

il numero di iterazioni del ciclo while è pari al numero di elementi presenti nella lista, da cui il costo computazionale $\Large \Theta(n)$

**d)** si scriva lo pseudocodice di un algoritmo ricorsivo che risolve il problema

```python
def es3(r):
    if r.next == None:
        return
    if r.val == r.next.val:
        r.next = r.next.next
        es3(r)
    else:
        es3(r.next)
```

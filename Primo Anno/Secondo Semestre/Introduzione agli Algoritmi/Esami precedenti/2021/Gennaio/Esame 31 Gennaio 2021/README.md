# <p align="center"> Esame 31 Gennaio 2021 </p>

## Esercizio 1

Si consideri la seguente funzione:

```python
def Exam(n):
    tot = n
    if n <= 1:
        return tot
    j = 512
    while j >= 2:
        k = 0
        while 3*k <= n:
            k = k + 1
        tot = tot + Exam(k)
        j = j/2
    return tot
```

**a)** Si imposti la relazione di ricorrenza che ne definisce il tempo di esecuzione giustificando dettagliatamente l’equazione ottenuta

il caso base verrà raggiunto quando $\Large n \leq 1$, con costo $\Large \Theta(1)$

$$
    \Large -T(n) = \Theta(1), \quad n \leq 1
$$

altrimenti, il costo sarà determinato

- dal primo ciclo while

- dal secondo ciclo while, annidato al primo

- dalla chiamata ricorsiva, presente sempre dentro al primo ciclo

si analizza il comportamento del primo ciclo

<div align="center">

| Iterazione | 0 | 1 | 2 | 3 | $\Large \dots$ | $i$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\Large j$ | 512 | 256 | 128 | 64 | $\Large \dots$ | $\Large \frac{512}{2^i}$ |

</div>

il ciclo terminerà quando

$$
    \Large \frac{512}{2^i} < 2
$$

$$
    \Large \frac{512}{2^i} = 1
$$

$$
    \Large 512 = 2^i
$$

$$
    \Large log_2(512) = i \implies i = 9
$$

il costo del primo ciclo sarà costante, $\Large \Theta(9) \implies \Theta(1)$

si analizza ora il comportamento del secondo ciclo

<div align="center">

| Iterazione | 0 | 1 | 2 | 3 | $\Large \dots$ | $i$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\Large k$ | 0 | 1 | 2 | 3 | $\Large \dots$ | $\Large i$ |
| $\Large 3k$ | 0 | 3 | 6 | 9 | $\Large \dots$ | $\Large 3i$ |

</div>

il ciclo terminerà quando

$$
    \Large 3i = n
$$

$$
    \Large i = \frac{n}{3}
$$

concludendo che il costo del ciclo sia $\Large \Theta(\frac{n}{3}) \implies \Theta(n)$

la chiamata ricorsiva ha come parametro $\Large k$, il quale al termine del secondo ciclo while abbiamo visto essere uguale a $\Large \frac{n}{3}$, quindi il costo della chiamata ricorsiva sarà $\Large T(\frac{n}{3})$.

La chiamata ricorsiva, essendo dentro il primo ciclo while, verrà eseguita 9 volte, quindi il costo totale di tutte le chiamate ricorsive sarà $\Large 9T(\frac{n}{3})$

il costo totale della funzione sarà quindi

$$
    \Large - T(n) = 9T(\frac{n}{3}) + \Theta(n), \quad n > 1
$$

$$
    \Large - T(n) = \Theta(1), \quad n \leq 1
$$

**b)** Si risolva la ricorrenza usando il metodo principale o un altro metodo ricordando che

$$
    \Large \sum_{i=1}^{k} 3^i = \Theta(3^k)
$$

dettagliando i passaggi del calcolo e giustificando ogni affermazione

si generalizza la ricorrenza in

$$
    \Large T(n) = aT(\frac{n}{b}) + f(n)
$$

individuando $\Large a = 9$, $\Large b = 3$ e $\Large f(n) = \Theta(n)$.

$\Large n^{\log_b(a)}$ sarà uguale a $\Large n^{log_3(9)} = n^2$

si rientra nel primo caso del metodo principale, poiché per $\Large \epsilon = 1$ si ha che

$$
    \Large f(n) = \Theta(n^{log_b(a) - \epsilon}) \implies \Theta(n^{2 - 1}) \implies \Theta(n)
$$

quindi il costo totale della funzione sarà

$$
    \Large T(n) = \Theta(n^{log_3(9)}) \implies \Theta(n^2)
$$

## Esercizio 2

Sia *A* un array di dimensione *n* e *B* un array ordinato di dimensione *m*,
contenenti entrambi numeri interi.

Si vuole trovare il numero di interi di *A* che non sono presenti in *B*.

Progettare un algoritmo ricorsivo che risolva il problema con un costo computazionale asintotico strettamente inferiore a $\Theta(n*m)$.

Ad esempio:

per *A = [8, 1, 2, 12, 10, 11, 20, 2]* e *B = [3, 3, 4, 8, 10, 10, 13, 20, 21, 22]*

l’algoritmo deve restituire 5 (i numeri in A e non in B sono infatti 1, 2, 2, 11, 12.

Dell’algoritmo proposto

a) si dia la descrizione a parole,

Per ogni elemento di *A* si effettua una ricerca binaria di quest'ultimo in *B*, usando un contatore per tenere traccia del numero di elementi di *A* che non sono presenti in *B*, ritornandolo una volta finiti di scorrere gli elementi di *A*.

> **nota**: viene richiesto di progettare un algoritmo ricorsivo, in questo caso solo la funzione di *ricerca binaria* lo sarà, in quanto, per la funzione principale, implementare una soluzione *ricorsiva* rispetto ad una *iterativa* senza la
possibilità di utilizzare più *variabili/strutture dati* ausiliarie risulta essere più tedioso.

**b)** si scriva lo pseudocodice,

```python
def es2(A, B):
    cont = 0
    for i in range(len(A)):
        if ric_bin(B, A[i]) == -1:
            cont += 1
    return cont

def ric_bin(B, x):
    s = 0
    d = len(B) - 1
    while s < d:
        m = (s + d) / 2        
        if B[m] < x:
            s = m + 1
        elif B[m] > x:
            d = m - 1
        else:
            return 1
    return - 1
```

**c)** si giustifichi il costo computazionale.

si dimostra brevemente il costo della funzione di ricerca binaria

il costo di tale funzione è determinata dal numero di iterazioni del ciclo while, in quanto il resto delle operazioni sono elementari, si analizza quindi il comportamento del ciclo

<div align="center">

| Iterazione | 0 | 1 | 2 | 3 | $\Large \dots$ | $k$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Lungezza array | $\Large m$ | $\Large \frac{m}{2}$ | $\Large \frac{m}{4}$ | $\Large \frac{m}{8}$ | $\Large \dots$ | $\Large \frac{m}{2^k}$ |

</div>

il ciclo terminerà quando la lunghezza dell'array sarà uguale a 1 (ovvero quando $\Large s = d$)

$$
    \Large \frac{m}{2^k} = 1
$$

$$
    \Large m = 2^k
$$

$$
    \Large log_2(m) = k \implies k = log_2(m)
$$

il costo totale della funzione di ricerca binaria sarà quindi $\Large \Theta(log_2(m))$.

il costo della funzione principale è invece determinato dal ciclo for, che scorre tutti gli elementi di *A*, quindi per $\Large n$ iterazioni compirà $\Large \Theta(log_2(m))$ operazioni al suo interno, da cui il costo

$$
    \Large T(n) = n\Theta(log_2(m)) \implies \Theta(n*log_2(m))
$$

il costo sarà dunque strettamente inferiore a $\Large \Theta(n*m)$.

## Esercizio 3

Si consideri una lista *L*, in cui ogni elemento è un record a due campi,

- il campo *val* contenente un intero

- ed il campo *next* con il puntatore al nodo seguente (*next* vale *None* per l’ultimo record della lista).

Bisogna contare i record della lista contenenti numeri pari.

Si consideri adesempio la lista *L*, per questa lista bisogna la risposta è 6

                    3 --> 5 --> 2 --> 4 --> 4 --> 8 --> 7 --> 7 --> 1 --> 9 --> 2 --> 2 --> None

Progettare un algoritmo ricorsivo che, dato il puntatore *r* alla testa
della lista effettui l’operazione di conteggio in tempo $\Large \Theta(n)$ dove n è il numero di elementi presenti nella lista.

Dell’algoritmo proposto

**a)** si dia la descrizione a parole,

Si scorre ricorsivamente una sola volta tutta la lista, controllando ogni volta se il valore del campo *val* del record corrente è pari, tenendone traccia usando le chiamate ricorsive.

**b)** si scriva lo pseudocodice,

```python
def es3(L):
    if L == None:
        return 0
    if L.val % 2 == 0:
        return 1 + es3(L.next)
    return es3(L.next)
```

**c)** si giustifichi il costo computazionale risolvendo la ricorsione che viene fuori dall’algoritmo utilizzando uno dei metodi di soluzione visti a lezione.

il caso base verrà raggiunto quando $\Large L = None$, ovvero quando la lungezza della lista sarà uguale a 0, con costo $\Large \Theta(1)$

$$
    \Large -T(n) = \Theta(1), \quad n = 0
$$

altrimenti, il costo sarà determinato dalle 2 chiamate ricorsive.

Si nota come entrambe le chiamate ricorsive abbiano lo stesso parametro e di come ne venga eseguita solo una tra le 2 (a seconda del valore del campo *val* del record corrente), quindi si può dire che il costo totale delle chiamate ricorsive sia $\Large T(n-1)$.

$$
    \Large -T(n) = T(n-1) + \Theta(1), \quad n \geq 1
$$

che aggiunta al caso base diventa

$$
    \Large -T(n) = T(n-1) + \Theta(1), \quad n \geq 1
$$

$$
    \Large -T(n) = \Theta(1), \quad n = 0
$$

si decide di risolvere la ricorrenza usando il metodo iterativo, quindi si studia il comportamento delle chiamate ricorsive

$$
    \Large T(n) = T(n-1) + \Theta(1)
$$

$$
    \Large T(n) = [T(n-2) + \Theta(1)] + \Theta(1) \implies T(n-2) + 2\Theta(1)
$$

$$
    \Large T(n) = \{[T(n-3) + \Theta(1)] + \Theta(1)\} + \Theta(1) \implies T(n-3) + 3\Theta(1)
$$

$$
    \Large T(n) = T(n-k) + k\Theta(1)
$$

il caso base verrà raggiunto quando

$$
    \Large n - k = 0
$$

$$
    \Large k = n
$$

dunque il costo della funzione sarà uguale a

$$
    \Large T(n) = T(n-n) + n\Theta(1)
$$

$$
    \Large T(n) = T(0) + \Theta(n)
$$

$$
    \Large T(n) = \Theta(1) + \Theta(n) \implies \Theta(n)
$$

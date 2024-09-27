# <p align="center"> Esame 21 Ottobre 2021 </p>

# <p align="center"> Esercizio 1 </p>

Si consideri la seguente funzione:

```python
def Exam(n):
    tot = n
    if n <= 1:
        return tot
    tot = tot + Exam(n − 1)
    b = n − 1
    j = n
    while j >= 0:
        tot = tot + j
        j = j − 2
    return tot + Exam(b)
```

---

**a)** Si imposti la relazione di ricorrenza che ne deﬁnisce il tempo di esecuzione giustiﬁcando dettagliatamente l’equazione ottenuta

Si rientrerà nel caso base per ogni $\Large n \leq 1$, con relativo costo $\Large \Theta(1)$.

$$
    \Large -T(n) = \Theta(1), \quad n \leq 1
$$

Per il caso generale, invece, il costo sarà determinato

- dalle 2 chiamate ricorsive

- dal ciclo while

<br>

- **ciclo while**

  Si analizza il suo comportamento

<div align="center">

| iterazione | 1 | 2 | 3 | $\Large \dots$ | $k$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $j$ | $n$ | $n-2$ | $n-4$ | $\Large \dots$ | $n-2k$ |

</div>

il ciclo while terminerà quando

$$
    \Large j = 0
$$

$$
    \Large n - 2k = 0
$$

$$
    \Large -2k = -n
$$

$$
    \Large 2k = n
$$

$$
    \Large k = \frac{n}{2}
$$

il costo sarà uguale a

$$
    \Large \Theta(\frac{n}{2}) \implies \Theta(n)
$$

- **chiamate ricorsive**

  Effettuate rispettivamente prima e dopo il ciclo while, esse presentato lo stesso parametro $\Large n - 1$, da cui il costo $\Large 2*T(n-1)$

$$
    \Large - T(n) = 2T(n - 1) + \Theta(n) \quad n > 1
$$

$$
    \Large - T(n) = \Theta(1) \quad n \leq 1
$$

---

**b)** Si risolva la ricorrenza usando il metodo di sostituzione e si dimostri così che la soluzione è  $\Large O(n * 2^n)$, commentando opportunamente i passaggi.

1. si elimina preliminarmente la notazione asintotica mediante l'ulitizzo di variabili ausiliarie

riscrivendo $\Large \Theta(n)$ come $\Large n\Theta(1)$

$$
    \Large - T(n) = 2T(n - 1) + c * n \quad n > 1
$$

$$
    \Large - T(n) = d \quad n \leq 1
$$

2. si ipotizza, come richiesto dal testo, che la soluzione sia $\Large T(n) = O(n * 2^n)$, dunque bisognerà dimostrare che

$$
    \Large T(n) \leq c * n * 2^n
$$

con $\Large c$ costante da determinare

- **passo base**

$$
    \Large T(n) = d \leq c * n * 2^n
$$

$$
    \Large d \leq c * n * 2^n
$$

$$
    \Large d \leq c * 1 * 2^1
$$

$$
    \Large d \leq 2c
$$

$$
    \Large c \geq \frac{d}{2}
$$

dunque per ogni $\Large c \geq \frac{d}{2}$, il caso base è soddisfatto

- **passo induttivo**

$$
    \Large T(n) = 2 * c * (n - 1) * 2^{n - 1} + b * n \leq c * n * 2^n
$$

$$
    \Large c * (n - 1) * 2^{n} + b * n \leq cn2^n
$$

$$
    \Large cn2^{n} - c2^{n} + b * n \leq cn2^n
$$

$$
    \Large - c2^{n} + b * n \leq 0
$$

$$
    \Large b * n \leq c2^{n}
$$

$$
    \Large \frac{b * n}{2^{n}} \leq c
$$

dunque per ogni $\Large n$  e per ogni $\Large c$ tali che $\Large c \geq \frac{b * n}{2^{n}}$, il caso ricorsivo (e quindi anche l'ipotesi iniziale) è soddisfatta

<br>

# <p align="center"> Esercizio 2 </p>

Sia dato un array *A* ordinato di *n* interi distinti ed un intero x;

si vuole trovare l’indice in *A* del più piccolo intero maggiore di x.

Progettare un algoritmo iterativo efficiente che risolva il problema.

Se l’array contiene solo elementi minori o uguali ad x, l’algoritmo deve restituire −1.

Ad esempio: per *A = [1, 2, 8, 10, 11, 12, 19]*, assumendo che le posizioni dell’array partano da 0,

- per $x = 7$ l’algoritmo deve restituire 2 (cio è l’indice dell’elemento 8),

- per $x = 30$ l’algoritmo deve restituire −1.

Dell’algoritmo proposto

---

**a)** si dia la descrizione a parole

Le 2 caratteristiche dell'array (ordinato e con tutti elementi distinti) portando inevitabilmente all'utilizzo della ricerca binaria per poter soddisfare la richiesta del testo in modo efficente.

Partendo dall'elemento centrale dell'array (usando un'indice ausiliario *m*)

- se $A[m] > x$, l'elemento cercato (se presente) si troverà nel sub-array di sinistra

- altrimenti, bisognerà cercare nel sub-array di destra

si continuerà a ripetere il procedimento fino a quando il k-esimo sub-array (con $\Large k = log_2(n)$) conterrà un solo elemento, procedendo così all'ultimo controllo

-  se l’elemento è strettamente maggiore di x, viene restituita la posizione di quest'ultimo

- altrimenti, viene restituito -1

---

**b)** si scriva lo pseudocodice

```python
def es2(A, x):
    s = 0
    d = len(A) - 1
    while s < d:
        m = (s + d) / 2
        if A[m] > x:
            d = m
        else:
            l = m + 1
    if A[s] > x:
        return s
    return -1
```

---

**c)** si giustiﬁchi il costo computazionale

il costo dell'algoritmo è determinato dal ciclo while, si analizza il suo comportamento

<div align="center">

| iterazione | 0 | 1 | 2 | $\Large \dots$ | $k$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| lunghezza sub-array | $n$ | $\Large \frac{n}{2}$ | $\Large \frac{n}{4}$ | $\Large \dots$ | $\Large \frac{n}{2^k}$ |

</div>

il ciclo while terminerà quando

$$
    \Large \frac{n}{2^k} = 1
$$

$$
    \Large n = 2^k
$$

$$
    \Large log_2(n) = k \implies k = log_2(n)
$$

il costo dell'algoritmo sarà pari a $\Large \Theta(log_2(n))$

# <p align="center"> Esercizio 3 </p>

Si consideri un albero binario radicato *T* , i cui nodi hanno 

- un campo *val* contenente un intero

- e i campi *left* e *right* con i puntatori ai ﬁgli.

Bisogna modiﬁcare il campo *val* di ciascun nodo in modo che il nuovo risulti la somma del valore originario incrementata dal valore originario degli eventuali ﬁgli.

Si consideri ad esempio l’albero T in ﬁgura a sinistra, a destra viene riportato il risultato della modiﬁca di T .

                        5                              13
                       / \                            /  \
                      /   \                          /    \
                     6     2                        6      9
                          / \                             / \
                         /   \                           /   \
                        4     3                         9     8
                       /     / \                       /     / \
                      /     /   \                     /     /   \
                     5     1     4                   5     1     4

Progettare un algoritmo ricorsivo che, dato il puntatore *r* alla radice di *T* memorizzato tramite record e puntatori, effettui l’operazione di modiﬁca in tempo $O(n)$ dove n è il numero di nodi presenti nell’albero.

Dell’algoritmo proposto

---

**a)** si dia la descrizione a parole

si visita l'albero in pre-order, sommando al valore del nodo corrente la somma dei valori dei suoi figli, se presenti

---

**b)** si scriva lo pseudocodice

```python
def es3(r):
    if r.left != None:
        r.val += r.left.val

    if r.right != None:
        r.val+ = r.right.val

    if r.left != None:
        es3(r.left)

    if r.right != None:
        es3(r.right)
```

---

**c)** si giustiﬁchi il costo computazionale

il costo è quello di una visita in *pre-order*, con equazione di ricorrenza

$$
    \Large - T(n) = T(k) + T(n − k − 1) + \Theta(1), \quad n \geq 1
$$

$$
    \Large - T(n) = \Theta(1), \quad n = 0
$$

dove

- $\Large n$ è il numero di nodi dell'albero

- $\Large k$ è il numero di nodi del sottoalbero sinistro

- e $\Large n-k-1$ è il numero di nodi del sottoalbero destro

Per determinarne il costo, si analizzano caso migliore e caso peggiore:

- **caso peggiore**:

    l'albero è completamente sbilanciato, quindi tutti i suoi nodi sono aggregati o nel sottoalbero sinistro o nel sottoalbero destro, ovvero quando

$$
    \Large k = 0 \vee n - k - 1 = 0
$$

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; • **$\Large k = 0$**

$$
    \Large T(n) = T(0) + T(n - 0 - 1) + \Theta(1) = T(n - 1) + \Theta(1)
$$

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; • **$\Large n - k - 1 = 0$**

$$
    \Large T(n) = T(n - 1) + T(0) + \Theta(1) = T(n - 1) + \Theta(1)
$$

sviluppando la ricorrenza, si ottiene

$$
    \Large T(n) = T(n - 1) + \Theta(1)
$$

$$
    \Large T(n) = T(n - 2) + \Theta(1) + \Theta(1)
$$

$$
    \Large T(n) = T(n - 3) + \Theta(1) + \Theta(1) + \Theta(1)
$$

generalizzabile in

$$
    \Large T(n) = T(n - k) + k\Theta(1)
$$

Verrà raggiunto il caso base quando

$$
    \Large n - k = 0
$$

$$
    \Large k = n
$$

Il costo sarà uguale a

$$
   \Large T(n) = T(n - n) + n\Theta(1) \implies T(0) + n\Theta(1) \implies \Theta(1) + n\Theta(1) \implies \Theta(n)
$$

<br>

- **caso migliore**:
    l'albero è completo, quindi ogni nodo padre ha esattamente 2 figli, ovvero quando sia il sottoalbero sinistro che il sottoalbero destro presentano $\Large \frac{n-1}{2}$ nodi, sostituendo i valori nell'equazione di ricorrenza si ottiene

$$
    \Large T(n) = T(\frac{n-1}{2}) + T(\frac{n-1}{2}) + \Theta(1) \implies 2T(\frac{n}{2}) + \Theta(1)
$$

Generalizzando  la ricorrenza in

$$
    \Large T(n) = aT(\frac{n}{b}) + f(n)
$$

vengono individuati $\Large a = 2$, $\Large b = 2$ e $\Large f(n) = \Theta(1)$.

$\Large n^{\log_b(a)}$ sarà uguale a $\Large n^{\log_2(2)} \implies n^1 \implies n$

Si ricade nel primo caso del metodo principale, poichè per $\Large \epsilon = 1$, $\Large f(n)$ risulta essere in $\Large O(n^{\log_b(a)-\epsilon}) \implies O(n^1-1) \implies O(n^0) \implies O(1)$.

Si conclude che

$$
    \Large T(n) = \Theta(n^{\log_b(a)}) = \Theta(n)
$$

Avendo trovato come caso peggiore $\Large T(n) = O(n)$ e come caso migliore $\Large T(n) = \Omega(n)$, per le proprietà della notazione asintotica il costo computazionale dell'algoritmo sarà uguale a

$$
    \Large T(n) = \Theta(n)
$$

Viene dunque rispettato il vincolo per il quale il costo computazionale dell’algoritmo debba essere uguale a $\Large O(n)$.

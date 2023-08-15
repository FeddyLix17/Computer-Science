# <p align="center"> Esame 21 Ottobre 2021 </p>

## Esercizio 1

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

**a)** Si imposti la relazione di ricorrenza che ne deﬁnisce il tempo di esecuzione giustiﬁcando dettagliatamente l’equazione ottenuta.

il caso base verrà raggiunto quando $\Large n \leq 1$, con tempo di esecuzione $\Large \Theta(1)$

$$
    \Large -T(n) = \Theta(1), \quad n \leq 1
$$

altrimenti, il tempo di esecuzione sarà determinato da

- il costo delle 2 chiamate ricorsive, con parametri $\Large n-1$ e $\Large b$ (che analizzando il codice si vede essere pari sempre a $\Large n-1$), da cui

$$
    \Large T(n - 1) + T(b) \implies T(n - 1) + T(n - 1) \implies 2T(n - 1)
$$
- il costo del ciclo while, del quale si analizzerà il comportamento di seguito

| iterazione | 1 | 2 | 3 | $\Large \dots$ | $k$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $j$ | $n$ | $n-2$ | $n-4$ | $\Large \dots$ | $n-2k$ |

il ciclo while terminerà quando $\Large j = 0$, ovvero quando

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

il costo del ciclo while sarà dunque pari a

$$
    \Large \Theta(\frac{n}{2}) \implies \Theta(n)
$$

il tempo di esecuzione totale sarà dunque pari a

$$
    \Large -T(n) = 2T(n - 1) + \Theta(n) \quad n > 1
$$

$$
    \Large -T(n) = \Theta(1) \quad n \leq 1
$$

**b)** Si risolva la ricorrenza usando il metodo di sostituzione e si dimostri così che la soluzione è 
$O(n * 2^n)$, commentando opportunamente i passaggi.

1. si elimina preliminarmente la notazione asintotica mediante l'ulitizzo di variabili ausiliarie

riscrivendo $\Large \Theta(n)$ come $\Large n\Theta(1)$
$$
    \Large -T(n) = 2T(n - 1) + c * n \quad n > 1
$$

$$
    \Large -T(n) = d \quad n \leq 1
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

## Esercizio 2

Sia dato un array *A* ordinato di *n* interi distinti ed un intero x;

si vuole trovare l’indice in *A* del più piccolo intero maggiore di x.

Progettare un algoritmo iterativo eﬃciente che risolva il problema.

Se l’array contiene solo elementi minori o uguali ad x, l’algoritmo deve restituire −1.

Ad esempio: per *A = [1, 2, 8, 10, 11, 12, 19]*, assumendo che le posizioni dell’array partano da 0,

- per $x = 7$ l’algoritmo deve restituire 2 (cio è l’indice dell’elemento 8),

- per $x = 30$ l’algoritmo deve restituire −1.

Dell’algoritmo proposto

**a)** si dia la descrizione a parole,

Le 2 caratteristiche dell'array (ordinato e con tutti elementi distinti) portando inevitabilmente all'utilizzo della ricerca binaria per poter soddisfare la richiesta del testo in modo efficente.

partendo dall'elemento centrale dell'array (usando un'indice ausiliario *m*)

- se $A[m] > x$, l'elemento cercato (se presente) si troverà nel sub-array di sinistra

- altrimenti, bisognerà cercare nel sub-array di destra

si continuerà a ripetere il procedimento fino a quando il k-esimo sub-array (con $\Large k = log_2(n)$) conterrà un solo elemento, procedendo così all'ultimo controllo

-  se l’elemento è strettamente maggiore di x, viene restituita la posizione di quest'ultimo

- altrimenti, viene restituito -1


**b)** si scriva lo pseudocodice,

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

**c)** si giustiﬁchi il costo computazionale.

il costo computazionale è pari a quello della [ricerca binaria](https://www.geeksforgeeks.org/complexity-analysis-of-binary-search/), di seguito lo si giustifica brevemente

il costo dell'algoritmo è determinato dal ciclo while, si analizza il suo comportamento

| iterazione | 0 | 1 | 2 | $\Large \dots$ | $k$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| lunghezza sub-array | $n$ | $\Large \frac{n}{2}$ | $\Large \frac{n}{4}$ | $\Large \dots$ | $\Large \frac{n}{2^k}$ |

il ciclo while terminerà quando

$$
    \Large \frac{n}{2^k} = 1
$$

ovvero, come detto prima, quando
$$
    \Large n = 2^k
$$

$$
    \Large log_2(n) = k \implies k = log_2(n)
$$

il costo dell'algoritmo sarà dunque pari a $\Large \Theta(log_2(n))$

## Esercizio 3

Si consideri un albero binario radicato *T* , i cui nodi hanno 

- un campo val contenente un intero

- e i campi left e right con i puntatori ai ﬁgli.

Bisogna modiﬁcare il campo val di ciascun nodo in modo che il nuovo risulti la somma del valore originario incrementata dal valore originario degli eventuali ﬁgli.

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

**a)** si dia la descrizione a parole,

si visita l'albero in pre-order, sommando al valore del nodo corrente la somma dei valori dei suoi figli, se presenti

**b)** si scriva lo pseudocodice,

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

**c)** si giustiﬁchi il costo computazionale.

il costo computazionale è pari a quello della visita in pre-order, di seguito lo si giustifica brevemente

ad ogni chiamata ricorsiva il numero dei nodi si dimezza (vengono contate anche le visite ai nodi *None*), la ricorrenza sarà dunque

$$
    \Large T(n) = 2T(\frac{n}{2}) + \Theta(1) \quad n > 1
$$

$$
    \Large T(n) = \Theta(1) \quad n \leq 1
$$

usando il teorema principale

si generalizza l'equazione in

$$
    \Large T(n) = aT(\frac{n}{b}) + f(n)
$$

dove $\Large a = 2$, $\Large b = 2$ e $\Large f(n) = \Theta(1)$

$\Large n^{\log_b(a)}$ sarà uguale a $\Large n^{\log_2(2)} = n^1 = n$

si rientra nel primo caso, dato che $\Large f(n) = \Theta(1)$ rientra in $\Large O(n^{log_b(a) - \epsilon})$ per qualche $\Large \epsilon > 0$

dunque il costo computazionale dell'algoritmo è pari a
$$
    \Large T(n) = \Theta(n^{\log_b(a)}) = \Theta(n)
$$

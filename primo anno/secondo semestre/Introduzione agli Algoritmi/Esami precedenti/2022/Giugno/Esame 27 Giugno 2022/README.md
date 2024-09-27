# <p align="center"> Esame 27 Giugno 2022 </p>

## <p align="center"> Esercizio 1

Si consideri la seguente funzione:

```python
def Exam(A, n):
    b = 1
    if n <= 2:
        return b
    i = 1
    while i <= 8:
        b = b * Exam(A, n/2)
        i+=1
    for i in range(n-1):
        A[i]+=A[i+1]
    return b
```

che viene richiamata la prima volta così:

```python
Exam(A, len(A))
```

---

**a)** Si imposti la relazione di ricorrenza che ne definisce il tempo di esecuzione giustificando dettagliatamente l’equazione ottenuta.

Si raggiungerà il caso base quando $\Large n \leq 2$, con relativo costo $\Large \Theta(1)$.

$$
    \Large -T(n) = \Theta(1), \quad n \leq 2
$$

Altrimenti, il costo sarà determinato rispettivamente dal ciclo while, il ciclo for e dalla chiamata ricorsiva.

- **Ciclo while**: <br> si analizza il suo comportamento al fine di determinarne il costo

<div align="center">

| Iterazione | 0 | 1 | 2 | 3 | $\Large \dots$ | $k$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\Large i$ | 1 | 2 | 3 | 4 | $\Large \dots$ | $\Large k + 1$ |

</div>

il ciclo terminerà quando

$$
    \Large k + 1 = 9
$$

$$
    \Large k = 9 - 1 \implies k = 8
$$

concludendo che il costo sia costante, ovvero $\Large \Theta(1)$.

- **Ciclo for**: <br> il ciclo eseguirà esattamente $\Large n - 2$ iterazioni, dunque con costo $\Large \Theta(n - 2) \implies \Theta(n)$.

- **Chiamata ricorsiva**: <br> la chiamata ricorsiva ha come parametro l'array $\Large A$ e la sua lunghezza dimezzata $\Large (\frac{n}{2})$, il suo costo sarà $\Large T(A, \frac{n}{2})$. <br> Si nota tuttavia come la chiamata ricorsiva venga effettuata all'interno del ciclo while, il quale la eseguirà, come ricavato in precedenza, $\Large 8$ volte. <br> Il costo totale della chiamate ricorsive sarà quindi $\Large 8 T(A, \frac{n}{2})$. <br> La relazione di ricorrenza sarà quindi:

$$
    \Large - T(n) = 8T(\frac{n}{2}) + \Theta(n), \quad n > 2
$$

$$
    \Large - T(n) = \Theta(1), \quad n \leq 2
$$

---

**b)** Si risolva la ricorrenza usando due metodi a scelta, dettagliando i passaggi del calcolo e giustificando ogni affermazione.

Si seglie di usare il metodo principale ed il metodo iterativo per risolvere la ricorrenza.

- **Metodo principale**:

generalizzando l'equazione in

$$
    \Large T(n) = aT(\frac{n}{b}) + f(n)
$$

vengono individuati $\Large a = 8$, $\Large b = 2$ e $\Large f(n) = \Theta(n)$.

$\Large n^{\log_b(a)}$ sarà uguale a $\Large n^{log_2(8)} = n^3$.

Si rientra nel primo caso del metodo principale, poichè scegliendo $\Large \epsilon = 2$, si ha che $\Large f(n) = \Theta(n)$ sia in $\Large O(n^{3 - 2}) = O(n)$.

il costo totale sarà quindi $\Large T(n) = \Theta(n^3)$.

- **Metodo Iterativo**:

si sviluppano le prime chiamate ricorsive

$$
    \Large T(n) = 8T(\frac{n}{2}) + \Theta(n)
$$

$$
    \Large T(n) = 8(8T(\frac{n}{2^2}) + \Theta(\frac{n}{2})) + \Theta(n)
$$

$$
    \Large T(n) = 8^2T(\frac{n}{2^2}) + 8\Theta(\frac{n}{2}) + \Theta(n)
$$

generalizzando in

$$
    \Large T(n) = \sum_{i = 0}^{k} 8^i \Theta(\frac{n}{2^i})
$$

$$
    \Large T(n) = n\sum_{i = 0}^{k} \Theta(\frac{8^i}{2^i})
$$

$$
    \Large T(n) = n\sum_{i = 0}^{k} \Theta(\frac{2^{3i}}{2^i})
$$

$$
    \Large T(n) = n\sum_{i = 0}^{k} \Theta(2^{2i})
$$

le chiamate ricorsive termineranno quando

$$
    \Large \frac{n}{2^k} = 1
$$

$$
    \Large n = 2^k
$$

$$
    \Large \log_2(n) = k \implies k = \log_2(n)
$$

sostituendo k nella sommatoria

$$
    \Large T(n) = n\sum_{i = 0}^{\log_2(n)} (2^{2i})
$$

$$
    \Large T(n) = n\Theta(\frac{2^{2\log_2(n) + 1} - 1}{4 - 1})
$$

$$
    \Large T(n) = n\Theta(\frac{n^2 * 4 - 1}{3})
$$

$$
    \Large T(n) = n\Theta(\frac{4n^2 - 1}{3})
$$

$$
    \Large T(n) = n\Theta(n^2)
$$

$$
    \Large T(n) = \Theta(n^3)
$$

viene confermato il costo ottenuto precedentemente.

## <p align="center"> Esercizio 2

Un array *A* ordinato di $\Large n > 1$ interi distinti ha subito una rotazione di *k* posizioni verso sinistra, $1 \leq k < n$.

Ad esempio,

- per A = [5, 7, 9, 2, 3] il valore di k è 2

- mentre per A = [9, 2, 3, 5, 7] è 4.

Progettare un’algoritmo che, dato l’array *A*, in tempo $O(log(n))$ restituisca il valore di k.

Dell’algoritmo proposto:

---

**a)** si dia la descrizione a parole;

Viene implementata una versione modificata della *ricerca binaria*.

Fino a quando non verra trovato l'elemento maggiore del suo successivo, partendo dall'elemento centrale, la ricerca procederà secondo le seguenti condizioni

- se l'elemento all'estemo sinistro del sub-array corrente è minore del suo elemento centrale, l'elemento da cercare si troverà nel sub-array destro
(ovvero quello compreso tra elemento corrente + 1 ed estremo destro)

- altrimenti, l'elemento si troverà nel sub-array sinistro (ovvero quello compreso tra estremo sinistro ed elemento corrente)

una volta trovato l'elemento maggiore del suo successivo, il numero *k* di rotazioni sarà determinato dalla differenza tra la lunghezza dell'array e l'indice dell'elemento trovato (incrementato di uno dato che inizia da 0).

---

**b)** si scriva lo pseudocodice;

```python
def es2(A):
    s = 0
    d = len(A) − 1
    while True:
        m = (s + d) / 2
        if A[m] > A[m + 1]:
            return len(A) − (m + 1)
        if A[s] < A[m]:
            s = m + 1
        else:
            d = m
```

---

**c)** si giustiﬁchi il costo computazionale.

Il costo computazionale è determinato dal ciclo while, del quale se ne analizzerà il comportamento di seguito

<div align="center">

| Iterazione | 0 | 1 | 2 | 3 | $\Large \dots$ | $k$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| lunghezza sub-array | $\Large n$ | $\Large \frac{n}{2}$ | $\Large \frac{n}{4}$ | $\Large \frac{n}{8}$ | $\Large \dots$ | $\Large \frac{n}{2^k}$ |

</div>

la minima lunghezza che il sub-array potrà assumere sarà $\Large 2$, da cui

$$
    \Large \frac{n}{2^k} = 2
$$

$$
    \Large n = 2^{k + 1}
$$

$$
    \Large \log_2(n) = k + 1
$$

$$
    \Large \log_2(n) - 1 = k \implies k = \log_2(n) - 1
$$

il costo totale sarà quindi $\Large T(n) = \Theta(\log_2(n)-1) \implies \Theta(\log_2(n))$, rispettando così la richiesta dell'esercizio.

## <p align="center"> Esercizio 3

Progettare un algoritmo che, dato il puntatore alla radice di un albero binario di ricerca *T*, modiﬁca il valore di ciascun nodo di *T* in modo che il nuovo valore del nodo risulti la somma di tutte le chiavi (che, in quanto tali, sono tutte distinte) che in *T* avevano un valore maggiore della sua chiave originaria.

Ad esempio l’albero sulla destra è il risultato dell’applicazione dell’algoritmo sull’albero binario di ricerca T riportato a sinistra.

                              10                               61
                            /    \                           /    \
                           /      \                         /      \
                          7       15                       80      20
                         / \     /  \                     /  \     / \
                        /   \   /    \                   /    \   /   \
                       3     9 12    20                87     71 49    0
                                \                                 \
                                 \                                 \
                                 14                                35

Il costo computazionale dell’algoritmo proposto deve essere $\Large \Theta(n)$ dove *n* è il numero di nodi dell’albero.

Dell’algoritmo proposto:

**a)** si dia la descrizione a parole;

Normalmente un albero binario di ricerca viene visitato in-order (in modo da visitare i nodi in ordine crescente).

Dovendo cambiare il valore del nodo corrente con quello dato dalla somma di tutte le chiavi del suo sottoalbero destro, la visita in-order sarà effettuata in modo inverso (ovvero che per ogni nodo, prima verrà visitato il suo sottoalbero destro, poi il nodo stesso e infine il suo sottoalbero sinistro).

Usando una variabile ausiliaria, si somma a quest'ultima il valore del nodo corrente, e la si assegna poi come nuovo valore del nodo corrente.

Per il nodo più a destra dell'albero il valore sarà 0, mentre per ogni altro nodo, il valore sarà la somma di tutte le chiavi presenti nel suo sottoalbero destro.

**b)** si scriva lo pseudocodice;

```python
def es3(T, somma):
    if T != None:
        somma = es3(T.right, somma)
        somma += T.key
        T.key = somma - T.key
        somma = es3(T.left, somma)
    return somma
```

**c)** si giustiﬁchi il costo computazionale.

il costo rimane quello di una visita in-order, con equazione di ricorrenza

<div align="center">

\- $\Large T(n) = T(k) + T(n − k − 1) + \Theta(1)$

\- $\Large T(0) = \Theta(1)$

</div>

dove $\Large n$ è il numero di nodi dell'albero, $\Large k$ è il numero di nodi del sottoalbero sinistro, $\Large n-k-1$ è il numero di nodi del sottoalbero destro.

Per determinarne il costo, si analizzano caso migliore e caso peggiore:

- **caso peggiore**: l'albero è completamente sbilanciato, quindi quando tutti i nodi sono aggregati o nel sottoalbero sinistro o nel sottoalbero destro, ovvero quando $\Large k = 0$ oppure $\Large n - k - 1 = 0$, sostituendo i valori nell'equazione di ricorrenza si ottiene la medesima equazione di ricorrenza del caso migliore

per $\Large k = 0$

$$
\Large T(n) = T(0) + T(n - 0 - 1) + \Theta(1) = T(n - 1) + \Theta(1)
$$

per $\Large n - k - 1 = 0$ (ovvero $\Large k = n - 1$)

$$
    \Large T(n) = T(n - 1) + T(0) + \Theta(1) = T(n - 1) + \Theta(1)
$$

usando il metodo iterativo per risolvere l'equazione di ricorrenza, si ottiene

$$
    \Large T(n) = T(n - 1) + \Theta(1) = [T(n - 2) + \Theta(1)] + \Theta(1)
$$

$$
    \Large T(n) = \{[T(n - 3) + \Theta(1)] + \Theta(1)\} + \Theta(1)
$$

generalizzando con una variabile ausiliaria $k$ in

$$
    \Large T(n) = T(n - k) + k\Theta(1)
$$

verrà raggiunto il caso base quando $\Large n - k = 0$, ovvero quando $\Large k = n$, da cui

$$
   \Large T(n) = T(n - n) + n\Theta(1) = T(0) + n\Theta(1) = \Theta(1) + n\Theta(1) = \Theta(n)
$$

- **caso migliore**: l'albero è completo, quindi quando ogni nodo padre ha esattamente 2 figli, ovvero quando sia il sottoalbero sinistro che il sottoalbero destro hanno $\Large \frac{n-1}{2}$ nodi, sostituendo i valori nell'equazione di ricorrenza si ottiene

$$
    \Large T(n) = T(\frac{n-1}{2}) + T(\frac{n-1}{2}) + \Theta(1) \approx 2T(\frac{n}{2}) + \Theta(1)
$$

utilizzando il metodo principale, si ricade nel primo caso

$\Large T(n) = 2T(\frac{n}{2}) + \Theta(1)$ può essere rappresentata come $T(n) = aT(\frac{n}{b}) + f(n)$

con $\Large a = 2$, $\Large b = 2$ e $\Large f(n) = \Theta(1)$

bisogna dimostrare, per qualche costante $\Large \epsilon > 0$, che $\Large f(n)$ sia in $\Large O(n^{\log_b(a)-\epsilon})$,

dove $\Large n^{\log_b(a)} = n^{\log_2(2)} = n^1 = n$

scegliendo $\Large \epsilon = 1$, $\Large n^{\log_b(a)-\epsilon}$ sarà uguale a $\Large n^0 = 1$, e sapendo che se $\Large f(n) = \Theta(1)$

allora vale anche $\Large f(n) = O(1)$, concludendo che $\Large T(n) = \Theta(n^{\log_b(a)}) = \Theta(n)$

avendo trovato come caso peggiore $\Large T(n) = O(n)$ e come caso migliore $\Large T(n) = \Omega(n)$, si conclude che il costo computazionale dell'algoritmo sia $\Large T(n) = \Theta(n)$

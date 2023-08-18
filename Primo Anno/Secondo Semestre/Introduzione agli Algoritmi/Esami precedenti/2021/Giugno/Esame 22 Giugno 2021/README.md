# <p align="center"> Esame 22 Giugno 2021 </p>

## Esercizio 1

Si consideri la seguente funzione:

```python
def exam(n, k: int):
    prod = 1
    i = k
    while i >= 1:
        prod = prod * i
        if i % 2 == 0:
            i = i/2
        else:
            i = (i - 1)/2
    if n = 1:
        return prod
    return prod * exam(n - 1, k)
```

Si imposti la relazione di ricorrenza che ne deﬁnisce il tempo di esecuzione facendo particolare attenzione al caso base;

si giustiﬁchi l’equazione ottenuta, e la si risolva usando il metodo iterativo ed il metodo di sostituzione, commentando opportunamente i passaggi del calcolo.

Si analizza prima il caso ricorsivo, in quanto la condizione per verificare il caso base è successiva all'esecuzione di codice non elementare.

Nel caso ricorsivo, il costo sarà determinato dal costo della chiamata ricorsiva più quello del ciclo while.

La chiamata ricorsiva ha come parametro $\Large n - 1$, dunque il suo costo sarà $\Large T(n - 1)$.

Si analizza ora il comportamento del ciclo while al fine di determinarnere il costo.

<div align="center">

| Iterazione | 1 | 2 | 3 | $\Large \dots$ | $\Large j$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\Large i$ | $\Large k$ | $\Large \frac{k}{2}$ | $\Large \frac{k}{4}$ | $\Large \dots$ | $\Large \frac{k}{2^j}$ |

</div>

Il ciclo while terminerà quando

$$
    \Large \frac{k}{2^j} = 1
$$

$$
    \Large k = 2^j
$$

$$
    \Large log_2(k) = j \implies j = log_2(k)
$$

dunque il costo del ciclo while sarà $\Large \Theta(log(k))$.

il caso base verrà raggiunto quando $\Large n = 1$, ma essendo verificata la condizione successivamente all'esecuzione del ciclo while, il suo costo invece di essere $\Large \Theta(1)$ sarà $\Large \Theta(log(k))$.

$$
    \Large -T(n) = \Theta(log(k)), \quad n = 1
$$

La ricorrenza finale sarà dunque

$$
    \Large - T(n, k) = T(n - 1, k) + \Theta(log(k)), \quad n > 1
$$

$$
    \Large - T(n, k) = \Theta(log_2(k)), \quad n = 1
$$

Si procede a risolvere la ricorrenza con il metodo iterativo.

$$
    \Large T(n, k) = T(n - 1, k) + \Theta(log(k))
$$

$$
    \Large T(n, k) = [T(n - 2, k) + \Theta(log(k))] + \Theta(log(k)) \\ \implies T(n - 2, k) + 2\Theta(log(k))
$$

$$
    \Large T(n, k) = [T(n - 3, k) + \Theta(log(k))] + 2\Theta(log(k)) \\ \implies T(n - 3, k) + 3\Theta(log(k))
$$

$$
    \Large T(n, k) = T(n - j) + j\Theta(log(k))
$$

le chiamate ricorsive termineranno quando $\Large n - j = 1 \implies j = n - 1$.

$$
    \Large T(n, k) = T(n - (n - 1), k) + (n - 1)\Theta(log(k))
$$

$$
    \Large T(n, k) = T(1, k) + (n)\Theta(log(k))
$$

$$
    \Large T(n, k) = \Theta(log(k)) + \Theta(n * log(k)) \implies \Theta(n * log(k))
$$

## Esercizio 2

Data una sequenza *S* di *n* bit memorizzata in un array *A*, progettare un algoritmo che ordina *S* in tempo $\Theta(n)$.

L’algoritmo deve ordinare in loco.

Dell’algoritmo proposto si dia la descrizione a parole, si scriva lo pseudocodice e si calcoli il costo computazionale.

Per quale motivo è possibile ordinare S in tempo lineare?

Si scorre una prima volta l'array *A* contando il numero di 0, ed una seconda volta sovrascrivendo le prime k posizioni con 0 e le restanti con 1.

```python
def es2(A):
    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            count += 1
    for i in range(len(A)):
        if i < count:
            A[i] = 0
        else:
            A[i] = 1
```

l'algoritmo ha costo $\Large 2*\Theta(n) \implies \Theta(n)$ (in quanto esegue per 2 volte n operazione elementari rispettivamente nei 2 cicli *for*).

È possibile ordinare l'array in tempo lineare in quanto si esso contiene un numero costante di elementi.

## Esercizio 3

Dato un albero binario *T* , radicato nel nodo *r*, deﬁniamo altezza minimale di *T* la minima distanza (cioè il minimo numero di archi) tra *r* e una qualsiasi foglia di *T* .

Progettare un algoritmo che, dato il puntatore alla radice di un albero binario memorizzato tramite record e puntatori, restituisca la sua altezza minimale.

Il costo dell’algoritmo deve essere $O(n)$, dove n è il numero di nodi dell’albero.

Dell’algoritmo proposto si dia la descrizione a parole, si scriva lo pseudocodice e si motivi il costo computazionale.

Quali sono i valori minimo e massimo che l’altezza minimale di *T* può assumere?

Motivare la risposta.

Partendo dalla radice, si procede a visitare ricorsivamente una sola volta tutto l'albero in post-order, restituendo ricorsivamente il minimo tra l'altezza del sottoalbero sinistro e destro.

```python
def es3(T):
    if T == None:
        return 0
    return 1 + min(es3(T.left), es3(T.right))
```

il costo è quello di una visita in post order, con equazione di ricorrenza

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

Viene dunque rispettato il vincolo per il quale il costo computazionale dell’algoritmo debba essere uguale a $\Large O(n)$.

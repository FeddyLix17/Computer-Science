# <p align="center"> Esame 22 Giugno 2021 </p>

## <p align="center"> Esercizio 1 </p>

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

---

Si rientrerà nel caso base quando $\Large n = 1$, ma essendo verificata la condizione successivamente all'esecuzione del ciclo while, il suo costo invece di essere $\Large \Theta(1)$ sarà $\Large \Theta(log(k))$ (successivamente dimostrato).

$$
    \Large - T(n) = \Theta(log(k)), \quad n = 1
$$

Nel caso generale, invece, il costo sarà determinato

- dal costo del ciclo while
- e dal costo della chiamata ricorsiva

- **ciclo while**

    si analizza il suo comportamento

<div align="center">

| Iterazione | 1 | 2 | 3 | $\Large \dots$ | $\Large j$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\Large i$ | $\Large k$ | $\Large \frac{k}{2}$ | $\Large \frac{k}{4}$ | $\Large \dots$ | $\Large \frac{k}{2^j}$ |

</div>

il ciclo terminerà quando

$$
    \Large \frac{k}{2^j} = 1
$$

$$
    \Large k = 2^j
$$

$$
    \Large log_2(k) = j \implies j = log_2(k)
$$

il suo costo sarà uguale a $\Large \Theta(log(k))$.

- **chiamata ricorsiva**
    la chiamata ha come parametro $\Large n - 1, k$, dunque il suo costo sarà uguale a $\Large T(n - 1, k)$.

$$
    \Large - T(n, k) = T(n - 1, k) + \Theta(log(k)), \quad n > 1
$$

$$
    \Large - T(n, k) = \Theta(log_2(k)), \quad n = 1
$$

---

- **metodo iterativo**

$$
    \Large T(n, k) = T(n - 1, k) + \Theta(log(k))
$$

$$
    \Large T(n, k) = T(n - 2, k) + \Theta(log(k)) + \Theta(log(k))
$$

$$
    \Large T(n, k) = T(n - 3, k) + \Theta(log(k)) + \Theta(log(k)) + \Theta(log(k))
$$

generalizzabile in

$$
    \Large T(n, k) = T(n - j) + j\Theta(log(k))
$$

Le chiamate ricorsive termineranno quando $\Large n - j = 1 \implies j = n - 1$.

$$
    \Large T(n, k) = T(n - (n - 1), k) + (n - 1)\Theta(log(k))
$$

$$
    \Large T(n, k) = T(1, k) + (n)\Theta(log(k))
$$

$$
    \Large T(n, k) = \Theta(log(k)) + \Theta(n * log(k)) \implies \Theta(n * log(k))
$$

---

- **metodo di sostituzione**

  Si ipotizza la soluzione $\Large \Theta(n * log(k))$, bisogna dimostrare che l'algoritmo sia in $\Large O(n * log(k))$ e in $\Large \Omega(n * log(k))$.

  Si rimuove la notazione asintotica

$$
    \Large - T(n, k) = T(n - 1, k) + log(k) * \Theta(1), \quad n > 1
$$

$$
    \Large - T(n, k) = log(k) * \Theta(1), \quad n = 1
$$

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; diventa

$$
    \Large - T(n, k) = T(n - 1, k) + log(k) * c, \quad n > 1
$$

$$
    \Large - T(n, k) = log(k) * d, \quad n = 1
$$

---

Per $\Large O(n * log(k))$ bisogna dimostrare che

$$
    \Large T(n, k) \leq e * n * log(k)
$$

per qualche costante $\Large e > 0$

- **caso base** $\Large n = 1$

$$
    \Large d * log(k) \leq e * log(k) \implies d \leq e
$$

- **passo induttivo**

$$
    \Large T(n - 1, k) + log(k) * c \leq e * n * log(k)
$$

sempre per ipotesi, se diamo per vero che $\Large T(n, k) \leq e * n * log(k)$, allora anche $\Large T(n - 1, k) \leq e * (n - 1) * log(k)$ sarà vero.

Sostituendolo nell'equazione diventa

$$
    \Large e * (n - 1) * log(k) + log(k) * c \leq e * n * log(k)
$$

$$
    \Large (e * n - e) * log(k) + log(k) * c \leq e * n * log(k)
$$

$$
    \Large e * n * log(k) - e * log(k) + log(k) * c \leq e * n * log(k)
$$

$$
    \Large log(k) * c \leq e * n * log(k) - e * n * log(k) + e * log(k)
$$

$$
    \Large log(k) * c \leq e * log(k)
$$

$$
    \Large c \leq e
$$

viene dunque dimostrato che per ogni $\Large e > 0$ tale che $\Large e \geq c \wedge e \geq d$, la funzione sarà in $\Large O(n * log(k))$.

---

Per $\Large \Omega(n * log(k))$ bisogna dimostrare che

$$
    \Large T(n, k) \geq f * n * log(k)
$$

per qualche costante $\Large f > 0$

- **caso base** $\Large n = 1$

$$
    \Large d * log(k) \geq f * log(k) \implies d \geq f
$$

- **passo induttivo**

$$
    \Large T(n - 1, k) + log(k) * c \geq f * n * log(k)
$$

sempre per ipotesi, se diamo per vero che $\Large T(n, k) \geq f * n * log(k)$, allora anche $\Large T(n - 1, k) \geq f * (n - 1) * log(k)$ sarà vero.

Sostituendolo nell'equazione diventa

$$
    \Large f * (n - 1) * log(k) + log(k) * c \geq f * n * log(k)
$$

$$
    \Large (f * n - f) * log(k) + log(k) * c \geq f * n * log(k)
$$

$$
    \Large f * n * log(k) - f * log(k) + log(k) * c \geq f * n * log(k)
$$

$$
    \Large log(k) * c \geq f * n * log(k) - f * n * log(k) + f * log(k)
$$

$$
    \Large log(k) * c \geq f * log(k)
$$

$$
    \Large c \geq f
$$

viene dunque dimostrato che per ogni $\Large e > 0$ tale che $\Large e \leq c \wedge f \geq d$, la funzione sarà in $\Large \Omega(n * log(k))$.

Per le proprietà della notazione asintotica, avendo dimostrato che la funzione è sia in $\Large O(n * log(k))$ che in $\Large \Omega(n * log(k))$, si può affermare che il suo costo sia uguale a $\Large \Theta(n * log(k))$.

<br>

## <p align="center"> Esercizio 2 </p>

Data una sequenza *S* di *n* bit memorizzata in un array *A*, progettare un algoritmo che ordina *S* in tempo $\Large \Theta(n)$.

L’algoritmo deve ordinare in loco.

Dell’algoritmo proposto si dia la descrizione a parole, si scriva lo pseudocodice e si calcoli il costo computazionale.

Per quale motivo è possibile ordinare S in tempo lineare?

---

Si scorre una prima volta l'array *A* contando il numero di 0 usando un contatore, ed una seconda volta sovrascrivendo le prime k posizioni (dove $\Large k = count$) con 0 e le restanti con 1.

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

L'algoritmo scorre per 2 volte l'array, compiendo ogni volta $\Large n$ operazioni elementari, da cui il costo

$$
    \Large 2*\Theta(n) \implies \Theta(n)
$$

È possibile ordinare l'array in tempo lineare in quanto si esso contiene un numero costante di elementi.

## <p align="center"> Esercizio 3 </p>

Dato un albero binario *T* , radicato nel nodo *r*, deﬁniamo altezza minimale di *T* la minima distanza (cioè il minimo numero di archi) tra *r* e una qualsiasi foglia di *T* .

Progettare un algoritmo che, dato il puntatore alla radice di un albero binario memorizzato tramite record e puntatori, restituisca la sua altezza minimale.

Il costo dell’algoritmo deve essere $O(n)$, dove n è il numero di nodi dell’albero.

Dell’algoritmo proposto si dia la descrizione a parole, si scriva lo pseudocodice e si motivi il costo computazionale.

Quali sono i valori minimo e massimo che l’altezza minimale di *T* può assumere?

Motivare la risposta.

---

Partendo dalla radice, si procede a visitare ricorsivamente una sola volta tutto l'albero in *post-order* (ovvero visitando prima il sottoalbero sinistro, successivamente il sottoalbero destro e infine il nodo corrente), restituendo ricorsivamente il minimo tra l'altezza del sottoalbero sinistro e destro.

```python
def es3(T):
    if T == None:
        return 0
    return 1 + min(es3(T.left), es3(T.right))
```

il costo è quello di una visita in *post-order*, con equazione di ricorrenza

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

# <p align="center"> Esame 17 Gennaio 2023 </p>

## Esercizio 1
Per la soluzione di un certo problema disponiamo di un
algoritmo iterativo con costo computazionale $\Large \Theta(n^3)$.

Ci viene proposto in alternativa un algoritmo ricorsivo il cui costo è catturato dalla seguente ricorrenza:

<div align="center">

$\Large T(n) = a*T(\frac{n}{2}) + \Theta(\sqrt{n})$ per $n \geq 2$

$\Large T(n) = Θ(1)$ altrimenti

</div>

dove $\Large a$ è una certa costante intera positiva con $\Large a \geq 2$.

Determinare quale sia il valore massimo che la costante intera a può avere perchè l’algoritmo ricorsivo risulti asintoticamente più eﬃciente dell’algoritmo iterativo di cui disponiamo

---
si risolve inizialmente la ricorrenza:

generalizzando l'equazione in $\Large T(n) = a*T(\frac{n}{b}) + f(n)$

s'individuando $\Large a = 2$, $\Large b = 2$ e $\Large f(n) = \Theta(\sqrt{n})$.

si rientra nel primo caso del teorema principale, poichè 

$\Large n^{\log_b(a)} = n^{\log_2(2)} = n^1 = n$

si sceglie una costante $\Large \epsilon$ tale che $f\Large (n)$ sia in $\Large O(n^{\log_b(a)-\epsilon}) = O(n^{1-\epsilon})$.

ad esempio, con $\Large \epsilon = \frac{1}{2}$, si ha che $\Large f(n) = \Theta(\sqrt{n})$ sia in $\Large O(n^{1-\frac{1}{2}}) = O(n^{\frac{1}{2}}) = O(\sqrt{n})$.

dopo aver determinato l'efficenza dell'algoritmo con il minore valore possibile di $\Large a$, si determina il valore massimo di $\Large a$ per cui l'algoritmo risulti asintoticamente più efficiente dell'algoritmo iterativo (più efficente di $\Large  \Theta(n^3)$).

siccome per $\Large a \geq 2$ troveremo sempre un valore di $\Large \epsilon > 0$ tale che $\Large f(n)$ sia in $\Large O(n^{\log_b(a)-\epsilon}) $, bisognerà analizzare solamente $\Large \Theta(n^{\log_b(a)})$ (soluzione del primo caso del teorema principale).

| $\Large a$ | $\Large 2$ | $\Large 3$ | $\Large 4$ | $\Large 5$ | $\Large 6$ | $\Large 7$ | $\Large 8$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $\Large \log_b(a)$ | $\Large 1$ | $\Large 1.58$ | $\Large 2$ | $\Large 2.32$ | $\Large 2.58$ | $\Large 2.81$ | $\Large 3$ |
| $\Large \Theta(n^{\log_b(a)})$ | $\Large \Theta(n)$ | $\Large \Theta(n^{1.58})$ | $\Large \Theta(n^2)$ | $\Large \Theta(n^{2.32})$ | $\Large \Theta(n^{2.58})$ | $\Large \Theta(n^{2.81})$ | $\Large \Theta(n^3)$ |

si conclude come per far si che l'algoritmo risulti asintoticamente più efficiente di $\Large \Theta(n^3)$, $\Large a$ debba essere necessariamente $\Large \leq 7$.


## Esercizio 2
Dati due arrays $\Large A$ e $\Large B$, rispettivamente di $\Large n$ ed $\Large m$ interi distinti, con $\Large m < n$, si vuole sapere se l’array $\Large A$ contenga l’array $\Large B$ come sottoarray.

Ad esempio, se $\Large A = [5, 9, 1, 3, 4, 8, 2]$, per $\Large B = [3, 4, 8]$ la risposta è SI mentre per
$\Large B = [3, 8, 2]$ o B = $[\Large 9, 6, 8]$ la risposta è NO

Progettare un algoritmo che, dati gli arrays $\Large A$ e $\Large B$, restituisca $\Large 1$ se la risposta
al problema è SI, $\Large 0$ altrimenti. 

Il costo computazionale dell’algoritmo deve essere $\Large O(n)$

Dell’algoritmo proposto:

**a)** si dia la descrizione a parole

La condizione necessaria per poter dire che $\Large A$ contenga $\Large B$ come sottoarray è che $\Large B$ sia un sottoinsieme di $\Large A$.

Per verificarlo si scorre l'array $\Large A$ controllando inizialmente se il primo elemento di $\Large B$ è presente in $\Large A$. 

In caso di riscontro, si continua a scorrere $\Large A$ a partire dall'indice successivo a quello in cui è stato trovato il primo elemento di $\Large B$, stavolta però si scorre in parallelo anche $\Large B$ (partendo dal suo secondo elemento) usando un secondo indice e controllando ogni volta
che gli elementi di $\Large A$ e $\Large B$ coincidano.

Se non sono stati trovati elementi diversi tra loro durante tutto lo scorrimento di $\Large B$, la funzione restituisce $\Large 1$, anche se non dovesse essere stato concluso lo scorrimento di $\Large A$.

In qualsiasi altro caso, ad esempio se il primo elemento di $\Large B$ non sia proprio presente in $\Large A$, o se sono stati trovati elementi diversi tra loro durante lo scorrimento in parallelo, la funzione restituisce $\Large 0$.

**b)** si scriva lo pseudocodice

```python
def es2(A, B):
    for i in range(len(A)):
        if A[i] == B[0]:
            z = i + 1
            for j in range(1, len(B)):
                if A[z] != B[j]:
                    return 0
                z+=1
            return 1
    return 0
```

**c)** si giustiﬁchi il costo computazionale

Il caso peggiore si ha quando $\Large A$ non contiene $\Large B$ come sottoarray, dovendo scorrere tutto $\Large A$ una sola volta per verificarlo, effettuando tutte operazioni con costo costante $\Large \Theta(1)$ per ogni elemento.

Dunque viene rispettato il vincolo di costo computazionale $\Large O(n)$.

## Esercizio 3

Sia dato un albero binario $\Large T$, in cui ogni nodo $\Large p$ ha
tre campi:

- il campo valore $\Large p.val$
- il campo col puntatore al ﬁglio sinistro $\Large p.sx$
- e il campo col puntatore al ﬁglio destro $\Large p.dx$

in mancanza di ﬁglio il puntatore vale $\Large None$.

Progettare un algoritmo ricorsivo che, dato il puntatore $\Large p$ alla radice dell’albero binario $\Large T$, restituisca $\Large 1$ se tutti i nodi dell’albero hanno lo stesso valore, $\Large 0$ altrimenti.

Il costo computazionale dell’algoritmo deve essere $\Large O(n)$, dove n è il numero di nodi dell’albero.

Dell’algoritmo proposto:

**a)** si dia la descrizione a parole

Per verificare che tutti i nodi dell'albero abbiano lo stesso valore, si controlla che il valore del nodo corrente sia uguale a quello dei suoi figli, se presenti.

Si visita l'albero in pre-order, dunque visitando prima il nodo corrente, poi il sottoalbero sinistro e infine quello destro.

Ogni volta che si arriva ad una foglia, se tutti i nodi visitati fino a quel momento avevano lo stesso valore, si restituisce $\Large 1$, altrimenti $\Large 0$.

Ciò garantisce che, se tutti i nodi presentano lo stesso valore, la funzione restituirà $\Large 1$ mentre se ci dovessere essere anche solo un nodo con valore diverso dagli altri, la funzione dovrà restituire necessariamente $\Large 0$.

**b)** si scriva lo pseudocodice

```python
def es3(p):
    if p == None:
        return 1
    if p.sx != None and p.sx.val != p.val:
        return 0
    if p.dx != None and p.dx.val != p.val:
        return 0
    return es3(p.sx) and es3(p.dx)
```
**c)** si giustifichi il costo computazionale

il costo computazionale dell'algoritmo  quello di una visita completa di un albero, riconducibile alla seguente equazione di ricorrenza

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
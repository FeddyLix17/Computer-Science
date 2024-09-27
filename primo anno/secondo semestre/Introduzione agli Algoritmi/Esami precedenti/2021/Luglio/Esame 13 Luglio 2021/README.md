# <p align="center"> Esame 13 Luglio 2021 </p>

## <p align="center"> Esercizio 1 </p>

Si consideri la seguente funzione:

```python
def Exam(n):
    if n <= 2:
        return 2 * n
    b = n/2
    tot = n * n
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            tot = tot + i - j
    for i in range(1, 5):
        for j in range(1, 5):
            if i = j:
                tot = tot + Exam(b)
            else:
                tot = tot + i - j
    return tot
```

---

**a)** Si imposti la relazione di ricorrenza che ne definisce il tempo di esecuzione
giustificando l’equazione ottenuta

Si rientrerà nel caso base per ogni $\Large N \leq 2$, con relativo costo $\Large \Theta(1)$.

Nel caso generale, invece, il costo sarà determinato

- dal primo ciclo for

- dal secondo ciclo for, annidato al primo

- dal terzo ciclo for

- dal quarto ciclo for, annidato al terzo

- dalla chiamata ricorsiva, annidata al quarto ciclo for

<br>

- **primo for**

  il ciclo eseguirà $\Large n$ iterazioni, da cui il costo $\Large \Theta(n)$ 

- **secondo for**

    il numero di iterazioni del ciclo dipenderà dal valore attuale di $\Large i$, ad esempio

    - per $\Large i = 1$, il ciclo verrà eseguito 1 volta (in quanto $\Large j$ è già uguale ad $\Large i$)
    - per $\Large i = 2$, il ciclo verrà eseguito 2 volte (una con $\Large j = 1$, una con $\Large = 2$)
    - per $\Large i = 3$, il ciclo verrà eseguito 3 volte (una con $\Large j = 1$, una con $\Large j = 2$, una con $\Large j = 3$)

    generalizzabile in
  
$$
    \Large \sum_{i=1}^{n} i
$$

Trattandosi di una [progressione aritmetica](https://it.wikipedia.org/wiki/Progressione_aritmetica), il costo sarà uguale a

$$
    \Large \Theta(\frac{n(n+1)}{2}) \implies \Theta(\frac{n^2 + n}{2}) \implies \Theta(n^2 + n) \implies \Theta(n^2)
$$

- **terzo for**

  il ciclo eseguirà $\Large 4$ iterazioni, da cui il costo $\Large \Theta(4) \implies \Theta(1)$

- **quarto for**

  il ciclo eseguirà $\Large 16$ iterazioni (ovvero per 4 volte eseguirà 4 iterazioni), da cui il costo $\Large \Theta(16) \implies \Theta(1)$

- **chiamata ricorsiva**

  la chiamata presenta come parametro $\Large b = \frac{n}{2}$, da cui il singolo costo $\Large T(\frac{n}{2})$.

  Nonostante sia annidata al quarto ciclo for, la chiamata ricorsiva sarà ripetuta 4 volte invece di 16 (ovvero solo quando $\Large i = j$)

$$
    \Large - T(n) = 4T(\frac{n}{2}) + \Theta(n^2), \quad n > 2
$$

$$
    \Large - T(n) = \Theta(1), \quad n \leq 2
$$

---

**b)** Si risolva l’equazione usando il metodo iterativo, commentando opportunamente i passaggi del calcolo

Sviluppando la ricorrenza si ottiene

$$
    \Large T(n) = 4T(\frac{n}{2}) + \Theta(n^2)
$$

$$
    \Large T(n) = 4(4T(\frac{n}{2^2}) + \Theta(\frac{n}{2})^2) + \Theta(n^2)
$$

$$
    \Large T(n) = 4^2T(\frac{n}{2^2}) + 4\Theta(\frac{n}{2})^2 + \Theta(n^2)
$$

$$
    \Large T(n) = 4^2T(\frac{n}{2^2}) + \Theta(n^2) + \Theta(n^2)
$$

$$
    \Large T(n) = 4^2T(\frac{n}{2^2}) + 2\Theta(n^2)
$$


generalizzabile in

$$
    \Large T(n) = 4^kT(\frac{n}{2^k}) + k\Theta(n^2)
$$

Le chiamate ricorsive termineranno quando 

$$
    \Large \frac{n}{2^k} = 1 \implies n = 2^k \implies \log_2(n) = k \implies k = \log_2(n)
$$

il costo della funzione sarà uguale a 

$$
    \Large T(n) = 4^{\log_2(n)}T(\frac{n}{2^{\log_2(n)}}) + \log_2(n)\Theta(n^2)
$$

$$
    \Large T(n) = 2^{2\log_2(n)}T(1) + \Theta(n^2 * \log_2(n))
$$

$$
    \Large T(n) = 2^{2\log_2(n)}\Theta(1) + \Theta(n^2 * \log_2(n))
$$

$$
    \Large T(n) = \Theta(n^2) + \Theta(n^2\log_2(n))
$$

$$
    \Large T(n) = \Theta(n^2*\log_2(n))
$$

---

**c)** Si risolva l’equazione usando il metodo principale, speciﬁcando quale caso del teorema si applica e perchè oppure per quale motivo non si può applicare il teorema

generalizzando la ricorrenza in $\Large T(n) = aT(\tfrac{n}{b}) + f(n)$

vengono individuati $\Large a = 4$, $\Large b = 2$ e $\Large  f(n) = \Theta(n^2)$.

Si rientra nel secondo caso del metodo principale, poichè $\Large f(n) = \Theta(n^{\log_b(a)})$.

Il costo della funzione sarà uguale a $\Large T(n) = \Theta(n^2*\log_2(n))$

<br>

## <p align="center"> Esercizio 2 </p>

Progettare un algoritmo che, dato un array *A* di n interi distinti i cui
elementi sono all’inizio in ordine crescente e da un certo punto in poi in ordine
decrescente, restituisce in tempo $\Large O(log(n))$ il massimo intero presente nell’array.

Ad esempio:

per *A = [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]* l’algoritmo deve restituire il valore *500*.

Dell’algoritmo proposto

---

**a)** si dia la descrizione a parole

È possibile fare uso della ricerca binaria per trovare il punto in cui l’array passa da ordine crescente a ordine decrescente (ovvero la posizione dell'elemento massimo presente).

Usando 2 puntatori inizializzati rispettivamente all'estremo sinistro e destro dell'array, si controlla l'elemento centrale

- Se l’elemento centrale è maggiore dell’elemento successivo ad esso, si continuerà a cercare l'elemento massimo nel sub-array sinistro (tra la coda e l'elemento precedente a quello centrale corrente) 

- altrimenti, si continuerà a cercarlo nel sub-array destro (tra l'elemento successivo a quello centrale corrente e la testa) 

Viene ripetuto lo stesso processo fino a quando non si otterrà un sub-array contente un unico elemento (quello ricercato), restituendolo come valore di ritorno della funzione.

---

**b)** si scriva lo pseudocodice

```python
def es2(A):
    s = 0
    d = len(A) - 1
    while s < d:
        m = (s + d) // 2
        if A[m] > A[m + 1]:
            d = m - 1
        else:
            s = m + 1
    return A[s]
```

---

**c)** si calcoli il costo computazionale

Il costo rimane quello della ricerca binaria, ovvero $\Large \Theta(log(n))$, dimostrato brevemente di seguito.

Il costo è determinato dal solo ciclo while, si analizza il suo comportamento

<div align="center">

| Iterazione | 0 | 1 | 2 | 3 | $\Large \dots$ | $\Large k$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Lunghezza sub-array | $\Large n$ | $\Large \frac{n}{2}$ | $\Large \frac{n}{4}$ | $\Large \frac{n}{8}$ | $\Large \dots$ | $\Large \frac{n}{2^k}$ |

</div>

il ciclo terminerà quando

$$
    \Large \frac{n}{2^k} = 1 \implies n = 2^k \implies k = \log_2(n)
$$

il costo totale della funzione sarà uguale a $\Large \Theta(\log_2(n))$.

Viene rispettato il vincolo di $\Large O(log(n))$ richiesto dal testo.

<br>

## <p align= "center"> Esercizio 3 </p>

Dato un albero binario *T*, radicato e con *n* nodi, deﬁniamo un nodo *u* di *T* equilibrato se il sottoalbero sinistro di *u* e il sottoalbero destro di *u* hanno entrambi lo stesso numero di nodi.

Progettare un algoritmo che, dato il puntatore *r* alla radice di un albero binario memorizzato tramite record e puntatori, restituisca in tempo $\Large O(n)$ il numero dei suoi nodi equilibrati.

---

**a)** si dia la descrizione a parole

Si procede a visitare l'albero in post-order (ovvero visitando prima il sottoalbero sinistro, successivamente il sottoalbero destro ed infine il nodo corrente).

Si tiene conto ricorsivamente, per ogni nodo, del numero di nodi dei suoi 2 sottoalberi rispettivamente, incrementando il numero di nodi equilibrati in caso siano uguali.

Il tutto restituendo ogni volta il numero di nodi presente ed il numero di nodi equilibrati come coppia di valori. 

Il primo valore di questa coppia sarà quello richiesto dall'esercizio.

---

**b)** si scriva lo pseudocodice

```python
def es3(r):    
    if r == None:
        return (0,0)

    eqS, sx_nodes = es3(r.left)
    eqD, dx_nodes = es3(r.right)
    eq = eqS + eqD

    if sx_nodes == dx_nodes:
        eq += 1
    return eq, sx_nodes + dx_nodes + 1
```

---

**c)** si motivi il costo computazionale

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

Il valore massimo di nodi equilibrati che l’albero T può avere è n, poichè se l’albero binario è completo allora tutti i suoi nodi saranno equilibrati.

Il valore minimo, invece, è 1.

Se l'albero binario è sbilanciato o a destra o a sinistra, l'unico nodo equilibrato sarà la sua foglia.

L'unico caso in cui il numero di nodi equilibrati sarà uguale a 0 è quando l'albero è vuoto.

# <p align= "center"> Esame 13 Luglio 2021 </p>

- ## Esercizio 1 (10 punti)

Si consideri la seguente funzione:

```python
def Exam(n):
    if n <= 2: return 2 * n;                # Θ(1)
    b = n/2;                                # Θ(1)
    tot = n * n;                            # Θ(1)  
    for i in range(1, n + 1):               # Θ(n)
        for j in range(1, i + 1):           # Θ(n)
            tot = tot + i - j;              # Θ(1)
    for i = 1 to 4:                         # Θ(1)
        for j = 1 to 4:                     # Θ(1)
            if i = j: tot = tot + Exam(b)   # T(n/2)
            else: tot = tot + i - j;        # Θ(1)
    return tot                              # Θ(1)
```

**a)** per impostare la relazione di ricorrenza si analizza il codice

1. nei primi 2 cicli for annidati, si analizza il loro comportamento per determinarne il costo. <br>

- per $i = 1$, il ciclo for annidato viene eseguito 1 volte in quanto $j$ è già  uguale ad $i$
- per $i = 2$, il ciclo for interno viene eseguito 2 volte (una con $j=1$, una con $j=2$)
- per $i = 3$, il ciclo for interno viene eseguito 3 volte in quanto (una con $j=1$, una con $j=2$, una con $j=3$)
- per $i = n$, il ciclo for interno viene eseguito n volte in quanto una con $j=1$, una con $j=2$, una con $j=3$, $...$ , una con $j=n$)

quindi il costo dei 2 cicli for annidati è pari a 

$$ \sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \frac{n^2}{2} + \frac{n}{2} = \Theta(n^2) $$

2. negli altri 2 cicli for annidati avviene una chiamata ricorsiva, che di per se ha un costo pari a $T(\frac{n}{2})$ , ma essendo eseguita 4 volte (solo quando $i=j$), avrà un costo pari a  $4T(\frac{n}{2})$

quindi la relazione di ricorrenza è $T(n) = 4T(n/2) + \Theta(n^2)$

con caso base  $T(2) = \Theta(1)$


$$
    \begin{cases}
    T(n) = 4T(\frac{n}{2}) + \Theta(n^2)\\
    T(1) = \Theta(1)
    \end{cases}
$$

**b)** usando il metodo iterativo per risolvere la ricorrenza, si ha che:

$$
    T(n) = 4T(\tfrac{n}{2}) + \Theta(n^2)\\
    T(n) = 4(4T(\tfrac{n}{2^2}) + \Theta(\tfrac{n}{2})^2) + \Theta(n^2)\\
    = 4^2T(\tfrac{n}{2^2}) + 4\Theta(\tfrac{n}{2})^2 + \Theta(n^2)\\
    = 4^2T(\tfrac{n}{2^2}) + \Theta(n^2) +\Theta(n^2)\\
    = 4^2T(\tfrac{n}{2^2}) + 2\Theta(n^2)\\
$$


da cui la generalizzazione $T(n) = 4^kT(\tfrac{n}{2^k}) + k\Theta(n^2)$

sapendo che $T(1) = \Theta(1)$, si ha che $\tfrac{n}{2^k} = 1 \implies n = 2^k \implies k = \log_2(n)$

il costo totale è uguale a $T(n) = 4^{\log_2(n)}T(\tfrac{n}{2^{\log_2(n)}}) + \log_2(n)\Theta(n^2)$

$$
    T(n) = 2^{2\log_2(n)}T(1) + \Theta(n^2\log_2(n))\\
    = 2^{2\log_2(n)}\Theta(1) + \Theta(n^2\log_2(n))\\
    = \Theta(n^2) + \Theta(n^2\log_2(n))\\
    = \Theta(n^2\log_2(n))
$$


**c)** per risolvere l'equazione di ricorrenza usando il metodo principale si generalizza in

$$
    \begin{cases}
        T(n) = aT(\tfrac{n}{b}) + f(n)\\
        T(1) = \Theta(1)
    \end{cases}
$$

dove $a = 4$, $b = 2$ e $f(n) = \Theta(n^2)$

si rientra nel caso in cui $f(n) = \Theta(n^{\log_b(a)})$ con $\log_b(a) = \log_2(4) = 2$
il costo totale sarà quindi uguale a $T(n) = \Theta(n^2\log_2(n))$


- ## Esercizio 2 (10 punti)
Progettare un algoritmo che, dato un array *A* di n interi distinti i cui
elementi sono all’inizio in ordine crescente e da un certo punto in poi in ordine
decrescente, restituisce in tempo *O(log n)* il massimo intero presente nell’array. <br>
Ad esempio: per *A = [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]* l’algoritmo deve
restituire il valore *500*

**a)** L’algoritmo da proggettare sfrutterà la ricerca binaria per trovare il punto in cui l’array passa da ordine crescente a ordine decrescente (nonchè valore massimo di quest'ultimo). <br> 
1. S'impostano due puntatori, testa e coda, rispettivamente all'estremo destro e sinistro dell’array.

2. Si calcola l’indice mid come la media di testa e coda. <br> 
Se l’elemento all’indice mid è maggiore dell’elemento successivo ad esso, significa che l'elemento più grande dell'array si trova tra la coda e mid, quindi s'imposta la testa = mid.

3. In caso contrario, l'elemento più grande dell'array si troverà tra mid + 1 e la testa, quindi s'imposta la coda a mid + 1.

4. Questo processo viene ripetuto finché l'indice della coda non sarà uguale all'indice della testa (ovvero quando il sub-array sarà composto solo dall'elemento che stavamo cercando).
5. A questo punto, l’algoritmo restituisce l’elemento trovato

**b)** 

```python
def find_max(A):
    coda = 0
    testa = len(A) - 1
    while coda < testa:
        mid = (coda + testa) / 2
        if A[mid] > A[mid + 1]:
            testa = mid
        else:
            coda = mid + 1
    return A[coda]
```

**c)** Per determinare la complessità dell'algoritmo, si analizza il ciclo while tenendo traccia della dimensione del sub-array in ogni iterazione. <br>

| k | 1 | 2 | 3 | ... |
|:----------:|:----------:| :----------:| :----------:| :----------:|
| len(A) | n | $\tfrac{n}{2}$ | $\tfrac{n}{4}$ | $\tfrac{n}{2^k}$ |

ricordando che esso terminerà quando la lunghezza del sub-array sarà 1, si ha che

$$
    \frac{n}{2^k} = 1 \implies n = 2^k \implies k = \log_2(n)
$$

quindi il costo totale sarà uguale a $\Theta(\log_2(n))$, o $O(\log_2(n))$ come richiesto dal testo



- ## Esercizio 3 (10 punti)

Dato un albero binario *T*, radicato e con *n* nodi, deﬁniamo un nodo *u* di
*T* equilibrato se il sottoalbero sinistro di *u* e il sottoalbero destro di *u* hanno
entrambi lo stesso numero di nodi. <br>
Progettare un algoritmo che, dato il puntatore *r* alla radice di un albero
binario memorizzato tramite record e puntatori, restituisca in tempo *O(n)* il
numero dei suoi nodi equilibrati.

**a)** L’algoritmo da progettare sfrutterà una visita in post-ordine per scorrere l’albero e controllare se ogni nodo è equilibrato. <br>

1. Per prima cosa l'algoritmo controlla se ci si trova su una foglia, in tal caso, restituisce una tupla contenente due zeri, indicando che non ci sono nodi e nessun nodo equilibrato nel sottoalbero radicato al nodo dato.

2. Se il nodo non è None, la funzione chiama ricorsivamente se stessa sui figli sinistro e destro del nodo corrente per ottenere il numero totale di nodi e il numero di nodi equilibrati nei rispettivi sottoalberi. <br>
La funzione quindi calcola il numero totale di nodi e il numero di nodi equilibrati nel sottoalbero radicato al nodo corrente sommando i valori restituiti dalle chiamate ricorsive sui figli sinistro e destro. <br>
Se il numero di nodi nei sottoalberi sinistro e destro è uguale, il conteggio dei nodi equilibrati viene incrementato di uno per includere il nodo corrente.

3. Infine, la funzione restituisce una tupla contenente il numero totale di nodi e il numero di nodi equilibrati nel sottoalbero radicato al nodo corrente.



**b)** 

```python
def multiplecounter(r):
    if r == None:
        return (0, 0)
    
    nodi_sinistra, nodi_sinistra_bilanciati = multiplecounter(r.left)
    nodi_destra, nodi_destra_bilanciati = multiplecounter(r.right)
    nodi_totali = 1 + nodi_sinistra + nodi_destra
    nodi_totali_bilanciati = nodi_sinistra_bilanciati + nodi_destra_bilanciati

    if nodi_sinistra == nodi_destra:
        nodi_totali_bilanciati += 1

    return (nodi_totali, nodi_totali_bilanciati)
```


**c)** si motivi il costo computazionale

l'algoritmo visita ogni nodo dell'albero (in post-order) una volta sola, quindi il costo totale è uguale a $\Theta(n)$, o $O(n)$ come richiesto dal testo

**Domanda:** Qual è il numero minimo e qual'è il numero massimo di nodi equilibrati che
l’albero T pu`o avere? Motivare la risposta. <br>

Il numero minimo di nodi equilibrati in assoluto che un albero binario può avere è 0. <br>
Ovviamente si tratta del caso estremo in cui l’albero sia vuoto (cioè non ha nodi). <br>
Se in un caso più comune l’albero abbia almeno un nodo, allora il minor numero di nodi equilibrati che un albero binario non vuoto può avere è 1. <br>
Ciò è dovuto al fatto che un albero binario non vuoto avrà almeno un nodo/almeno un nodo foglia e per definizione un nodo foglia è equilibrato (essendo che entrambi i loro sottoalberi sono vuoti, quindi hanno lo stesso numero di nodi (0)). <br>

Il numero massimo di nodi equilibrati che un albero binario può avere è uguale al numero totale di nodi dell’albero stesso. <br>
Si verifica quando l’albero è perfettamente bilanciato, quando tutti i livelli dell’albero sono completamente riempiti.
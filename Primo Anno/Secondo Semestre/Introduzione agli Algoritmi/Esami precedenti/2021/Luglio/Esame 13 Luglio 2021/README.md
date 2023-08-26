# <p align= "center"> Esame 13 Luglio 2021 </p>

## <p align= "center"> Esercizio 1 </p>

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

## <p align= "center"> Esercizio 2 </p>

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

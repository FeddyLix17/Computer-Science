# <p align="center"> Esame 31 Gennaio 2023 </p>

## <p align="center"> Esercizio 1 </p>
Si consideri il seguente algoritmo ricorsivo che, dato un array $A$ di dimensione
$n$, verifica se esistono due indici diversi $\Large i$ e $\Large j$ compresi nell’intervallo $\Large [0, n − 1]$ tali che $\Large A[i] = j$ e $\Large A[j] = i$:

```python
def IndiciValori(A, sx, dx):
    if (sx >= dx): return False     #Θ(1)
    else:
        trovato = False       
        centro = (sx + dx) / 2

        for i in range(sx, centro + 1): 
            for j in range(centro + 1, dx + 1):
                if (A[i] == j) and (A[j] == i): trovato = True

    trovato1 = IndiciValori(A, sx, centro)
    trovato2 = IndiciValori(A, centro + 1, dx)
    return trovato or trovato1 or trovato2
```

---

**a)** per impostare l'equazione di ricorrenza si analizza il codice

- si hanno $2$ chiamate ricorsive alla fine con parametro $\Large \frac{n}{2}$
- si analizzano attentamente i $2$ cicli for annidati per determinarne il loro costo
- il primo ciclo for ha un range che va da $sx$ a $centro$ eseguendo $centro - sx + 1$ iterazioni
- il secondo ciclo for ha un range che va da $centro + 1$ a $dx$ eseguendo $dx - centro - 1$ iterazioni

per il momento il loro costo *teorico* è $\Large \Theta((centro - sx + 1) *(dx - centro -1))$

dal codice si nota come $centro$ sia ugualmente a $\Large \frac{sx + dx}{2}$, modificando il costo in

$$ 
    \Large \Theta( ( \frac{sx + dx}{2} - sx + 1) * (dx - \frac{sx + dx}{2} -1))
$$

$$
    \Large \Theta( ( \frac{dx + sx -2sx + 2}{2}) * (\frac{- sx -dx + 2dx -2}{2}))
$$

$$
    \Large \Theta( ( \frac{dx - sx + 2}{2}) * (\frac{dx - sx - 2}{2}))
$$

sempre dal codice si vede come $dx$ indichi la fine dell'array e $sx$ l'inizio, potendo affermare che la lunghezza $n$ dell'array sarà data da $dx - sx + 1$, modificando nuovamente il costo in

$$
    \Large \Theta( ( \frac{n + 1}{2}) * (\frac{n - 3}{2}))
$$

$$
    \Large \Theta( \frac{n^2 -3n +n - 3}{4})
$$

$$
    \Large \Large \Theta( \frac{n^2 -2n -3}{4}) \implies \Theta(n^2) + \Theta(n) \implies \Theta(n^2)
$$

si conclude che il costo dei 2 cicli for annidati sia $\Large \Theta(n^2)$.

L'equazione di ricorrenza sarà data dalla somma di tutti i costi trovati,

$$
    \Large T(n) = T(\frac{n}{2}) + T(\frac{n}{2}) + \Theta(n^2) \implies T(n) = 2T(\frac{n}{2}) + \Theta(n^2)
$$

con caso base $\Large T(1) = \Theta(1)$ (ovvero quando $\Large sx \geq dx$, condizione soddisfatta dalla dimensione del sub-array uguale a 1)

<div align="center">

\- $\Large T(n) = 2T(\frac{n}{2}) + \Theta(n^2),\ n > 1$

\- $\Large T(1) = \Theta(1),\ n \leq 1$

</div>

---

**b)** i 2 metodi scelti per risolvere l'equazione di ricorrenza sono il metodo principale e il metodo dell'albero

- **Metodo Principale**

    generalizzando l'equazione in $\Large T(n) = aT(\frac{n}{b}) + f(n)$

    vengono individuati i parametri $\Large a = 2$, $\Large b = 2$ e $\Large f(n) = \Theta(n^2)$,

    
    avendo $\Large n^{\log_b a} = n^{\log_2 2} = n$, si ricade nel terzo caso poichè

    $\Large f(n) = \Theta(n^2)$ è in $\Large \Omega(n^{log_b(a) + \epsilon})$ con $\Large \epsilon > 0$ (ad esempio $\Large \epsilon = 1$)

    viene anche rispettata la seconda condizione del terzo caso $\Large a\*f(\frac{n}{b}) \leq c\*f(n)$
    
    con $\Large 0 < c < 1$ in quanto $\Large 2*\Theta((\frac{n}{2})^2) \leq c*\Theta(n^2)$

    ad esempio scegliendo $\Large c = \frac{1}{2}$ si ha

$$
    \Large 2*\Theta((\frac{n}{2})^2) \leq \frac{1}{2}*\Theta(n^2)
$$

$$ 
    \Large 2*\Theta((\frac{n}{2})^2) \leq \frac{1}{2}*\Theta(n^2)
$$

$$ 
    \Large 2\Theta(\frac{n^2}{4}) \leq \Theta(\frac{n^2}{2})
$$

$$ 
    \Large \Theta(\frac{n^2}{2}) \leq \Theta(\frac{n^2}{2})
$$

concludendo che $\Large T(n) = \Theta(n^2)$

- **Metodo dell'albero**

    si disegna l'albero di ricorsione

                             T(n)                                       Θ(n^2)
                            /    \                                      /   \
                           /      \                                    /     \
                          /        \                                  /       \
                       T(n/2)     T(n/2)                        Θ((n/2)^2)   Θ((n/2)^2)
                        /  \       /  \                             / \       / \
                       /    \     /    \                           /   \     /   \
                      /      \   /      \                         /     \   /     \
                T(n/2^2)    ... ...   T(n/2^2)            Θ((n/2^2)^2)  ... ...  Θ((n/2^2)^2)


    si nota come il costo di ogni livello sia dato da $\Large 2^{i}\Theta((\frac{n}{2^{i}})^2)$ con $i$ che indica il livello dell'albero (nel metodo dell'albero si parte dal livello 0)

    il numero dei livelli è regolato dalla condizione $\Large \frac{n}{2^i} = 1$ che indica quando si arriva al caso base, ovvero quando $\Large n = 2^i \implies i = \log_2(n)$

    il costo totale sarà dato dalla somma di tutti i costi dei livelli, ovvero

$$ 
    \Large \sum_{i=0}^{\log_2(n)} \Theta((\frac{n}{2^i})^2)
$$

$$ 
    \Large \Theta(n^2) *\sum_{i=0}^{\log_2(n)} \Theta(\frac{1}{2^{2i}})
$$

$$ 
    \Large \Theta(n^2) *\sum_{i=0}^{\log_2(n)} (\frac{1}{4^i})
$$

$$ 
    \Large \Theta(n^2)
$$

anche tramite l'utilizzo di un secondo metodo si conferma che $\Large T(n) = \Theta(n^2)$

<br>

## <p align="center"> Esercizio 2 </p>
Scrivere un algoritmo *ElementoPiuFrequente* che, dato un array $A$ di $n$ interi, compresi tra $1$ e $10n$ restiuisce il valore più presente all’interno dell’array, a parità di occorrenze va restituito il valore minimo.

Ad esempio, se $A = [2, 6, 8, 5, 2, 3, 6, 8, 9, 5, 8, 1, 2]$, allora la risposta è $2$ in quanto $2$ ed $8$ sono gli unici valori che compaiono $3$ volte all’interno dell’array, mentre gli altri valori compaiono al più 2 volte.

Il costo computazionale dell’algoritmo proposto deve essere $\Theta(n)$.

Dell’algoritmo proposto:

---

**a)** si scriva lo pseudocodice opportunamente commentato

```python
def ElementoPiuFrequente(A):
    # similmente all'algoritmo di ordinamento CountingSort, si crea un array 
    # di dimensione 10n + 1 per memorizzare le occorrenze di ogni valore 
    # compreso tra 1 e 10n presenti nell'array A
    occorrenze = [0] * (10*len(A) + 1) # Θ(1)
    
    # inizializzo la variabile max che conterrà il numero maggiore di occorrenze
    # aggiornato ad ogni iterazione dell'array A
    max = 0 # Θ(1)

    # inizializzo la variabile elemento che conterrà il valore più frequente
    # nonchè il valore da restituire alla fine dell'algoritmo
    elemento = 0 # Θ(1)

    # itero l'array A
    for i in range(len(A)): # Θ(n)

        # incremento di 1 l'occorrenza del valore A[i] nell'array occorrenze
        # ad esempio se A[i] = 5, allora occorrenze[A[1]] = occorrenze[5] += 1
        occorrenze[A[i]] += 1 # Θ(1)

        # controllo se il valore di occorrenze[A[i]] sia maggiore di max
        if occorrenze[A[i]] > max: # Θ(1)

            # in caso aggiorno max con quest'ultimo
            # mantenere aggiornato max garantisce il poter
            # iterare l'array occorrenze una sola volta
            max = occorrenze[A[i]] # Θ(1)

            # assieme a max viene aggiornato anche elemento
            # con il valore di A[i] che ha più occorrenze
            elemento = A[i] # Θ(1)
        
        # se invece occorrenze[A[i]] è uguale a max
        # come richiesto dall'esercizio bisogna
        # selezionare il valore minore tra i due 
        elif occorrenze[A[i]] == max: # Θ(1)
            elemento = min(elemento, A[i]) # Θ(1)
    
    # finito di iterare l'array A, si restituisce elemento
    return elemento # Θ(1)
```

---

**b)** si giustifichi il costo computazionale

il costo computazionale dell'algoritmo è $\Large \Theta(n)$ in quanto si itera l'array $\Large A$ una sola volta, e per ogni iterazione si eseguono operazioni in tempo costante $\Large \Theta(1)$.

<br>

## <p align="center"> Esercizio 3 </p>
Sia $\Large L$ una lista concatenata semplicemente puntata data tramite il puntatore $\Large p$ alla sua testa e contenenti chiavi intere positive.

Ogni record è composto da due campi:

- il campo $key$ che contiene il valore del nodo
- ed il campo $next$ che contiene il puntatore al nodo successivo della lista se questo esiste, il valore None altrimenti.

Si progetti un algoritmo ricorsivo con costo computazionale $\Large O(n)$ che restituisca un puntatore al primo elemento della lista la cui chiave sia esattamente uguale alla somma delle chiavi di tutti gli elementi precedenti;

se un tale elemento non esiste, verrà ritornato $\Large None$.

Ad esempio, per la lista $p\Large  \rightarrow 1 \rightarrow 2 \rightarrow 3 \rightarrow 6$ verrà restituito un puntatore al record contenente l’informazione $3$;

si noti che anche il record contenente l’informazione $6$ soddisfa la richiesta di avere la chiave pari alla somma dei precedenti, ma il record contenente 3 lo precede.

Dell’algoritmo proposto:

---

**a)** si scriva lo pseudocodice opportunamente commentato

```python
def SommaPrecedenti(p, somma):
    # se si arriva all'ultimo elemento della lista, 
    # viene restituito None
    if p == None:   # Θ(1)
        return None

    # controllo se la somma dei nodi precedenti
    # è uguale alla chiave
    if somma == p.key: # Θ(1)
        # restituendo in caso proprio il puntatore al nodo corrente
        return p

    # altrimenti si richiama ricorsivamente la funzione
    # passando come parametro il puntatore al nodo successivo
    # e la somma dei nodi precedenti più la chiave del nodo corrente
    return SommaPrecedenti(p.next, somma + p.key) # T(n-1)
```

---

**(b)** si giustiﬁchi il costo computazionale trovando e risolvendo l’equazione di ricorrenza.

per impostare l'equazione di ricorrenza si analizza il codice

- si ha una sola chiamata ricorsiva alla fine con parametro $p.next$, con tempo di esecuzione $T(n-1)$
- tutte le altre operazioni eseguite all'interno della funzione presentano tempo costante $\Theta(1)$

l'equazione di ricorrenza sarà quindi

$$ 
    \Large T(n) = T(n-1) + \Theta(1)
$$

con caso base $\Large T(0) = \Theta(1)$ (ovvero quando $\Large p = None$ e quindi la lista è vuota)

<div align="center">

\- $\Large T(n) = T(n-1) + \Theta(1),\ n > 1$

\- $\Large T(0) = \Theta(1),\ n \leq 1$

</div>

risolvendo l'equazione con il metodo iterativo si ottiene

$$ 
    \Large T(n) = T(n-1) + \Theta(1) = [T(n-2) + \Theta(1)] + \Theta(1)
$$

$$ 
    \Large T(n) = \{[T(n-3) + \Theta(1)] + \Theta(1)\} + \Theta(1)
$$

generalizzando in

$$ 
    \Large T(n) = T(n-k) + k*\Theta(1)
$$

si arriva al caso base quando $\Large n-k = 0 \implies k = n$ da cui

$$ 
    \Large T(n) = T(n - n) + n*\Theta(1)
$$

$$ 
    \Large T(n) = T(0) + n*\Theta(1)
$$

$$ 
    \Large T(n) = \Theta(1) + n*\Theta(1)
$$

$$ 
    \Large T(n) = \Theta(n)
$$

viene cosi rispettato il vincolo di costo computazionale $\Large O(n)$ richiesto dall'esercizio.

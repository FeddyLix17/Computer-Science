# <p align="center"> Esame 8 Settembre 2021 </p>

- ## Esercizio 1 (10 punti)
    Si consideri la seguente funzione:

```python
def Exam(n):
    tot = n                 # Θ(1)
    if n <= 4:              # Θ(1)
        return tot
    b = n / 4               # Θ(1)
    tot += Exam(b)          # T(n/4)
    j = 1                   # Θ(1)
    while j * j <= n:       # Θ(√n)
        tot += j            # Θ(1)
        j += 1              # Θ(1)
   return tot + Exam(b)    # T(n/4)
```

<b> a) </b>  per trovare l'equazione di ricorrenza che ne deﬁnisce il tempo di esecuzione,
si analizza l'intero codice.

1. Le due chiamate ricorsive hanno hanno come parametro b, che è pari a $\frac{n}{4}$, quindi il loro tempo di esecuzione è $T(\frac{n}{4})$
2. Il ciclo while ha come condizione di uscita j * j ≤ n, quindi per uscire $j^2$ dovrà essere uguale a $n + 1$, <br> ad ogni iterazione,
etichettata con la lettera k, si nota la seguente relazione

| k | 0 | 1 | 2 | 3 | . . . |
| :-: | :-: | :-: | :-: | :-: | :-: |
| j | 1 | 2 | 3 | 4 | k + 1 |
| j<sup>2</sup> |  1 | 4 | 9 | 16 | (k + 1)<sup>2</sup> |

s'imposta l'equazione

$$  (k + 1)^2 = n + 1 $$

e risolvendola

$$ 
    k + 1 = \sqrt{n + 1} \implies
    k = \sqrt{n + 1} - 1 \implies
    k \approx \sqrt{n}
$$ 

si conclude che il costo del ciclo while è $\Theta(\sqrt n)$ <br>
L'equazione di ricorrenza sarà data da

$$ T(n) = T(\frac{n}{4}) + T(\frac{n}{4}) + \Theta(\sqrt n) = 2T(\frac{n}{4}) + Θ(\sqrt n)$$

$$
    \begin{cases}
    T(n) = 2T(\frac{n}{4}) + Θ(\sqrt n)\\
    T(1) = \Theta(1)
    \end{cases}
$$

<b> b) </b> Ricavata l'equazione di ricorrenza nel punto a), si risolve con il metodo dell'albero


                            T(n)                                                         Θ(√n)
                          /      \                                                      /     \
                         /        \                                                    /       \
                        /          \                                                  /         \
                    T(n/4)        T(n/4)                                        Θ(√n/4)         Θ(√n/4)
                   /      \      /      \                                      /       \       /       \
                  /        \    /        \                                    /         \     /         \
                 /          \  /          \                                  /           \   /           \
               T(n/16)    ... ...       ...                              Θ(√n/4^2)      ... ...         ...

si nota che

0. al livello 0, il costo è $\Theta(\sqrt n)$
1. al livello 1, il costo di un nodo è  $\Theta(\frac{\sqrt n}{4})$ mentre il costo totale del livello è $4\Theta(\frac{\sqrt n}{4})$
2. al livello 2, il costo di un nodo è $\Theta(\frac{\sqrt n}{16})$ mentre il costo totale del livello è $4\Theta(\frac{\sqrt n}{16})$
3. al livello k, il costo di un nodo è $\Theta(\frac{\sqrt n}{4^k})$ mentre il costo totale del livello è $2^k \Theta(\frac{\sqrt n}{4^k})$
            
$$ 
    2^k(\Theta(\sqrt\frac{n}{4^k}) \implies
    2^k(\frac{\sqrt{n}}{2^k}) \implies
    \sqrt n \implies
    \Theta(\sqrt n) 
$$

per trovare l'esatto numero di livelli dell'albero, s'imposta  l'equazione 

$$ 
    \frac{n}{4^k} = 1 \implies
    n = 4^k \implies
    \log_4(n) = k \implies
    k = \log_4(n) 
$$

si conclude che il numero di livelli è $\log_4(n)$ <br>

per trovare il costo totale dell'albero, si sommano i costi di tutti i livelli

$$ 
    \sum_{i=0}^{\log_4(n) - 1} \sqrt{n} \implies
    \sqrt{n} \sum_{i=0}^{\log_4(n) - 1} 1 \implies
    \sqrt{n}\log_4(n)
$$

il costo totale dell'algoritmo sarà quindi $\Theta(\sqrt{n}\log_4(n))$

- ## Esercizio 2 (10 punti)

Progettare un algoritmo che, dati tre array $A$, $B$ e $C$ ordinati e contenenti ciascuno $n$ interi distinti, stampi in tempo $O(n)$ gli interi che compaiono nell’intersezione dei tre array. <br>
L’algoritmo proposto deve utilizzare spazio di lavoro $\Theta(1)$. <br>
Ad esempio: <br>
per $A = [1, 2, 3, 4, 5, 6]$, $B = [1, 4, 5, 6, 8, 9]$ e $C = [2, 4,     6, 7, 8, 9]$ <br>
l’algoritmo deve stampare gli elementi $4$ e $6$. <br>
Dell’algoritmo proposto:

<b> a) </b> si dia la descrizione a parole <br>

L'algoritmo da proggettare è una variante dell'algoritmo di intersezione tra due array ordinati,  che sfrutta il fatto che gli array sono ordinati per scorrerli in modo lineare. <br>
Si sfrutta la proprietà di intersezione tra due array ordinati, ovvero che se l'elemento di un array è maggiore dell'elemento dell'altro array ad uno stesso indice, allora bisognerà incrementare solo l'indice dell'elemento minore. <br>
Bisogna riadattare questa proprietà per tre array, usando un terzo indice per scorrere il terzo array. <br>

1. Si inizializzano tre indici, $i$, $j$, e $k$, corrispondenti rispettivamente agli indici di $A$, $B$ e $C$, impostandoli a $0$
2. Confronto gli elementi i $A[i]$, $B[j]$ e $C[k]
3. Nel caso in cui tutti e 3 gli elementi siano uguali, si stampa l'elemento in questione incrementando successivamente tutti e 3 gli indici
4. Nel caso invece in cui ci sia almeno un elemento diverso, viene calcolato il minor valore tra i 3 e si incrementa solo l'indice dell'array dove si trova quest'ultimo
5. In questo modo anche se i 3 indici saranno uguali solo inizialmente non si corre il rischio di saltare un elemento che potrebbe essere nell'intersezione.
6. Vengono ripetuti questi confronti con gli indici aggiornati man mano fino a quando uno degli indici supera la lunghezza dell'array.
    
<b> b) </b> 
    
```python
def intersezione(A, B, C):
    i = 0           #Θ(1)
    j = 0           #Θ(1)
    k = 0           #Θ(1)
    while i < len(A) and j < len(B) and k < len(C):   #Θ(n)
        if A[i] == B[j] and B[j] == C[k]:
            print(A[i])
            i += 1  
            j += 1  
            k += 1 
        else:                                   #Θ(1)
            minimo = min(A[i], B[j], C[k])
            if minimo == A[i]:
                i += 1
            elif minimo == B[j]:                
                j += 1
            else:
                k += 1
 ```

<b> c) </b> Per determinare il costo effettivo si analizza il costo del ciclo while. <br>
        
1. Il caso migliore si verifica quando tutti e 3 gli array sono identici, quindi il ciclo while verrà eseguito $n$ volte, dove è rappresenta la lunghezza dell'array, con costo finale $\Omega(n)$
2. Il caso peggiore si verifica quando gli array non hanno nessun elemento in comune tra tutti e 3, ma sapendo che ad ogni iterazione almeno un indice viene incrementato, si deduce che il ciclo while verrà eseguito al massimo $3n$ volte, con costo totale sarà $O(3n)$ = $O(n)$

Per definizione delle notazioni asintotiche, se una funzione $f(n)$ è sia in $\Omega(n)$ che in $O(n)$, allora sarà anche in $\Theta(n)$, quindi il costo computazionale dell'algoritmo è $\Theta(n)$
ed utilizza uno spazio di lavoro pari a $\Theta(1)$ in quanto lavora sugli array in input senza crearne di nuovi usando solo 3 indici.

<b> d) </b> si dia un’idea di quello che accadrebbe al costo computazionale se si volesse generalizzarlo a $\Theta(n)$ array <br>

Se si volesse generalizzare l’algoritmo per trovare l’intersezione di $\Theta(n)$ array ordinati di lunghezza $n$, chiaramente il costo computazionale aumenterebbe. <br>
In questo caso, l’algoritmo avrebbe bisogno di $\Theta(n)$ indici, e ad ogni iterazione del ciclo while dovrebbe confrontare $\Theta(n)$ valori per trovarne il minimo o comunque per verificare se tutti gli elementi di quella iterazioni sono uguali o meno, aumentando il costo di ogni iterazione del ciclo while da $\Theta(1)$ a $\Theta(n)$ <br>

1. Il caso migliore avrebbe costo $\Omega(n^2)$ in quanto dovremmo confrontare per n volte n elementi uguali
2. Il caso peggiore avrebbe costo $O(n^3)$ in quanto dovremmo confrontare per n volte n elementi diversi, quindi n<sup>2</sup> volte per trovare il minimo aggiungte agli n controlli per trovare quale indice incrementare

- ## Esercizio 3 (10 punti)

Si consideri un albero binario radicato $T$ , i cui nodi hanno un campo valore contenente un intero. <br>
Bisogna modiﬁcare l’albero in modo che i nodi fratelli scambino tra loro il valore. <br>
Si consideri ad esempio l’albero $T$ in ﬁgura a sinistra, a destra viene riportato il risultato della modiﬁca di $T$. <br>

                            5                                                           5
                           / \                                                         / \            
                          /   \                                                       /   \
                         6     2                                                     2     6
                              / \                                                         / \
                             /   \                                                       /   \
                            4     3                                                     3     4
                           /     / \                                                   /     / \
                          /     /   \                                                 /     /   \
                         5     1     4                                               5     4     1

Progettare un algoritmo che, dato il puntatore $r$ alla radice di $T$ memorizzato tramite record e puntatori, effettui l’operazione di modiﬁca in tempo $O(n)$ dove $n$ è il numero di nodi presenti nell’albero. <br>
Ogni nodo dell’albero è memorizzato in un record contenente il campo val con il valore del nodo e i campi $left$ e $right$ con i puntatori ai ﬁgli di sinistra e destra, rispettivamente. <br>

<b> a) </b> L'algoritmo $scambia\ fratelli$ prende come input il puntatore $r$ alla radice dell'albero binario radicato $T$. <br> 
L'algoritmo è ricorsivo e si basa sul fatto che se un nodo ha entrambi i figli, allora scambia i valori dei figli e richiama ricorsivamente la funzione prima sul figlio sinistro e poi sul figlio destro. <br>
L'algoritmo termina quando tutto l'albero sarà stato visitato
    
<b> b) </b>

```python
def scambia_fratelli(r):
    if r.left:
        scambia_fratelli(r.left)

    if r.right:
        scambia_fratelli(r.right)

    if r.left and r.right:
        r.left.val, r.right.val = r.right.val, r.left.v
```

<b> c) </b> il costo computazionale dell'algoritmo è $\Theta(n)$ in quanto vengono semplicemente visitati tutti i nodi dell'albero una sola volta (in postorder) e le operazioni che vengono effettuare su di essi hanno costo $\Theta(1)$

# <p align="center"> Esame 8 Settembre 2021 </p>

## <p align="center"> Esercizio 1 </p>

Si consideri la seguente funzione:

```python
def Exam(n):
    tot = n
    if n <= 4:
        return tot
    b = n / 4
    tot += Exam(b)
    j = 1
    while j * j <= n:
        tot += j
        j += 1
   return tot + Exam(b)
```

---

**a)** Si imposti la relazione di ricorrenza che ne definisce il tempo di esecuzione giustificando l’equazione ottenuta.

Si rientrerà nel caso base per ogni $\Large n \leq 4$, con relativo costo $\Large \Theta(1)$.

$$
    \Large - T(n) = \Theta(1), \quad n \leq 4
$$

Per il caso generale, invece, il costo sarà determinato

- dal ciclo while
- dalle 2 chiamate ricorsive, rispettivamente prima e dopo il ciclo while

<br>

- **chiamate ricorsive**
  
  Le due chiamate hanno entrambe come parametro b,  pari a $\Large \frac{n}{4}$, il loro costo sarà uguale a $\Large 2*T(\frac{n}{4})$

- **ciclo while**

  si analizza il suo comportamento

<div align="center">

| k | 0 | 1 | 2 | 3 | . . . |
| :-: | :-: | :-: | :-: | :-: | :-: |
| j | 1 | 2 | 3 | 4 | k + 1 |
| $\Large j^2$|  1 | 4 | 9 | 16 | $(\Large k + 1)^2$ |

</div>

Il ciclo terminerà quando

$$
    \Large (k + 1)^2 > n
$$

$$
    \Large (k + 1)^2 = n + 1
$$

$$
    \Large k + 1 = \sqrt{n + 1}
$$

$$
    \Large k = \sqrt{n + 1} - 1
$$

il costo sarà uguale a $\Large \Theta(\sqrt{n + 1} - 1) \implies \Theta(\sqrt{n})$

$$
    \Large - T(n) = 2T(\frac{n}{4}) + \Theta(\sqrt{n}), \quad n > 4
$$

$$
    \Large - T(n) = \Theta(1), \quad n \leq 4
$$

---

**b)** Si risolva l’equazione usando il metodo dell’albero, dettagliando i passaggi del calcolo e giustificando ogni affermazione.

Si sviluppa l'albero di ricorsione

                            T(n)                                                         Θ(√n)
                          /      \                                                      /     \
                         /        \                                                    /       \
                        /          \                                                  /         \
                    T(n/4)        T(n/4)                                        Θ(√(n/4))         Θ(√(n/4))
                   /      \      /      \                                      /       \       /       \
                  /        \    /        \                                    /         \     /         \
                 /          \  /          \                                  /           \   /           \
               T(n/16)    ... ...       ...                              Θ(√(n/4^2))      ... ...         ...

0. al livello 0, il costo è $\Large \Theta(\sqrt{n})$
1. al livello 1, il costo di un nodo è  $\Large \Theta(\sqrt{\frac{n}{4}})$ mentre il costo totale del livello è $\Large 2\Theta(\sqrt{\frac{n}{4}}$
2. al livello 2, il costo di un nodo è $\Large \Theta(\sqrt{\frac{n}{16}})$ mentre il costo totale del livello è $\Large 4\Theta(\sqrt{\frac{n}{16}})$
3. al livello k, il costo di un nodo è $\Large \Theta(\sqrt{\frac{n}{4^k}})$ mentre il costo totale del livello sarà $\Large 2^k \Theta(\sqrt{\frac{n}{4^k}})$

sviluppandolo diventa

$$ 
    \Large 2^k (\sqrt{\frac{n}{4^k}})
$$

$$
    \Large 2^k (\frac{\sqrt{n}}{2^{k}})
$$

$$
    \Large \sqrt{n} 
$$

Le chiamate ricorsive termineranno quando

$$ 
    \Large \frac{n}{4^k} = 1
$$

$$
    \Large n = 4^k
$$ 

$$
    \Large \log_4(n) = k \implies k = \log_4(n) 
$$

Il numero di livelli sarà uguale a $\Large \log_4(n)$.

Il costo totale della funzione sarà dato dalla somma dei costi di tutti i livelli, ovvero

$$ 
    \Large \Theta(\sqrt{n} * \log_4(n)) \implies \Theta(\sqrt{n} * \log(n))
$$

<br>

## <p align="center"> Esercizio 2 </p>

Progettare un algoritmo che, dati tre array $A$, $B$ e $C$ ordinati e contenenti ciascuno $n$ interi distinti, stampi in tempo $O(n)$ gli interi che compaiono nell’intersezione dei tre array.

L’algoritmo proposto deve utilizzare spazio di lavoro $\Theta(1)$.

Ad esempio:

per $A = [1, 2, 3, 4, 5, 6]$, $B = [1, 4, 5, 6, 8, 9]$ e $C = [2, 4, 6, 7, 8, 9]$

l’algoritmo deve stampare gli elementi $4$ e $6$.

Dell’algoritmo proposto:

---

**a)** si dia la descrizione a parole

Si utilizzano 3 indici per scorrere i 3 array rispettivamente e fino a quando non si finirà di scorrerne almeno uno

- se i 3 elementi presenti ai corrispettivi indici sono uguali, esso verrà stampato e i 3 indici saranno tutti incrementati

- altrimenti, viene incrementato solo l'indice dell'elemento minore tra i 3 

---

**b)**  si scriva lo pseudocodice
    
```python
def es2(A, B, C):
    i = 0
    j = 0
    k = 0
    while i < len(A) and j < len(B) and k < len(C):
        if A[i] == B[j] and B[j] == C[k]:
            print(A[i])
            i += 1  
            j += 1  
            k += 1 
        else:
            cur_min = min(A[i], B[j], C[k])
            if cur_min == A[i]:
                i += 1
            elif cur_min == B[j]:                
                j += 1
            else:
                k += 1
 ```

---

**c)** si giustifichi formalmente il costo computazionale

Il costo dell'algoritmo è determinato dal ciclo while, del quale si analizzerà il comportamento di seguito

- **caso migliore**

  Si verifica quando tutti e 3 gli array sono identici, per i quali verranno eseguite $\Large n$ iterazioni, dove $\Large n$ rappresenta la lunghezza dell'array, con costo $\Large \Omega(n)$

- **caso peggiore**

  Si verifica quando gli array non hanno nessun elemento in comune tra loro, per i quali verranno eseguite al più $\Large 3*n$ iterazioni,  con costo  $\Large O(3n) \implies O(n)$

Avendo trovato caso migliore $\Large \Omega(n)$ e caso peggiore $\Large O(n)$, per le proprietà della notazione asintotica, il costo computazionale dell'algoritmo sarà uguale a $\Theta(n)$.

L'algoritmo utilizza uno spazio di lavoro pari a $\Theta(1)$ in quanto lavora in loco senza l'utilizzo di altre strutture dati.

---

**d)** si dia un’idea di quello che accadrebbe al costo computazionale se si volesse generalizzarlo a $\Large \Theta(n)$ array

Se si volesse generalizzare l’algoritmo per trovare l’intersezione di $\Large \Theta(n)$ array ordinati di lunghezza $\Large n$, chiaramente il costo computazionale aumenterebbe.

In questo caso, l’algoritmo avrebbe bisogno di $\Large \Theta(n)$ indici, e ad ogni iterazione del ciclo while dovrebbe confrontare $\Large \Theta(n)$ valori per trovarne il minimo o comunque per verificare che tutti gli elementi di quella iterazioni siano uguali o meno, aumentando il costo di ogni iterazione del ciclo while da $\Large \Theta(1)$ a $\Large \Theta(n)$.

- **caso migliore**

  Se tutti i $\Large \Theta(n)$ array fossero identici, il costo sarebbe di $\Large \Omega(n^2)$, in quanto bisognerebbe solo confrontare per n volte n elementi uguali

- **caso peggiore**

  Se invece tutti i $\Large \Theta(n)$ array non avessero nessun elemento in comune tra loro, costo sarebbe di $\Large O(n^3)$, in quanto bisognerebbe confrontare per n volte n elementi diversi, quindi $\Large n^2$ controlli per trovare il minimo aggiunte agli n controlli per trovare quale indice incrementare

<br>

## <p align="center"> Esercizio 3 </p>

Si consideri un albero binario radicato $T$ , i cui nodi hanno un campo valore contenente un intero.

Bisogna modiﬁcare l’albero in modo che i nodi fratelli scambino tra loro il valore.

Si consideri ad esempio l’albero $T$ in ﬁgura a sinistra, a destra viene riportato il risultato della modiﬁca di $T$.

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

Progettare un algoritmo che, dato il puntatore $r$ alla radice di $T$ memorizzato tramite record e puntatori, effettui l’operazione di modiﬁca in tempo $O(n)$ dove $n$ è il numero di nodi presenti nell’albero.

Ogni nodo dell’albero è memorizzato in un record contenente il campo val con il valore del nodo e i campi $left$ e $right$ con i puntatori ai ﬁgli di sinistra e destra, rispettivamente.

---

**a)** si dia la descrizione a parole

Viene visitato l'albero in post-order, ovvero visitando prima il sottoalbero sinistro, poi quello destro ed infine il nodo corrente

Se il nodo corrente presenta entrambi i figli, allora vengono scambiati i corrispettivi valori.

---

**b)** si scriva lo pseudocodice

```python
def es3(r):
    if r.left:
        es3(r.left)
    if r.right:
        es3(r.right)
    if r.left and r.right:
        r.left.val, r.right.val = r.right.val, r.left.val
```

---

**c)** si giustifichi formalmente il costo computazionale

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

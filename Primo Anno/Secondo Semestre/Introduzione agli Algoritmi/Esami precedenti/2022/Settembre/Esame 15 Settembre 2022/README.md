# <p align="center"> Esame 15 Settembre 2022 </p>

## Esercizio 1

Si supponga di avere un algoritmo speciale in grado di eseguire la fusione di
due sottoarray ordinati di $\Large \frac{n}{2}$ elementi ciascuno in $\Large O(\sqrt{n})$ operazioni.

Quanto sarebbe, in questo caso, il costo computazionale dell’algoritmo di Merge Sort?

**a)** Si imposti la relazione di ricorrenza che definisce il tempo di esecuzione giustificando dettagliatamente l’equazione ottenuta

L'equazione di ricorrenza è la seguente:

$$
    \Large -\ T(n) = 2T(\frac{n}{2}) + O(\sqrt{n}), \quad n > 1
$$

$$
    \Large -\ T(1) = \Theta(1), \quad n = 1
$$

**b)** Si risolva la ricorrenza usando due metodi a scelta, dettagliando i passaggi del calcolo e giustiﬁcando ogni affermazione

L'eqauzione può essere generalizzata come

$$
    \Large T(n) = aT(\frac{n}{b}) + f(n)\\
$$

dove $\Large a = 2$, $\Large b = 2$ e $\Large f(n) = O(\sqrt{n})$.

$\Large n^{\log_b(a)}$ sarà uguale a $\Large n^{\log_2(2)} = n$.

Si ricade così nel primo caso del teorema della ricorrenza, poichè segliendo ad esempio $\Large \epsilon = 0.5$

si dimostra come $\Large f(n) = O(\sqrt{n})$ sia uguale a

$$
    \Large O(n^{\log_b(a) - \epsilon})
$$

$$
    \Large O(n^{\log_2(2) - 0.5})
$$

$$
    \Large O(n^{1 - 0.5})
$$

$$
    \Large O(n^{0.5}) = O(n^{\frac{1}{2}}) = O(\sqrt{n}), \quad \epsilon > 0
$$

il costo computazionale dell'algoritmo sarà quindi

$$
    \Large \Theta(n^{\log_b(a)}) = \Theta(n^{\log_2(2)}) = \Theta(n)
$$

L'esercizio chiede di risolvere la ricorrenza usando due metodi, si sceglie di usare il metodo iterativo per confermare che il risultato sia $\Large \Theta(n)$.

Dopo una iterazione, il costo computazionale dell'algoritmo sarà

$$
    \Large T(n) = 2T(\frac{n}{2}) + O(\sqrt{n})
$$

dopo due iterazioni, invece sarà uguale a

$$
    \Large T(n) = 2[2T(\frac{n}{4}) + O(\sqrt{\frac{n}{2}})] + O(\sqrt{n}) =
$$

$$
    \Large = 4T(\frac{n}{4}) + 2O(\sqrt{\frac{n}{2}}) + O(\sqrt{n})
$$

volendo generalizzare, dopo $\Large k$ iterazioni, il costo computazionale sarà

$$
    \Large T(n) = 2^kT(\frac{n}{2^k}) + \sum_{i=0}^{k-1}2^iO(\sqrt{\frac{n}{2^i}})
$$

verrà raggiunto il caso base quando $\Large \frac{n}{2^k} = 1$, ovvero quando $\Large k = \log_2(n)$.

Sostituendo $\Large k$ con $\Large \log_2(n)$, si ottiene

$$
    \Large T(n) = 2^{\log_2(n)}T(\frac{n}{2^{\log_2(n)}}) + \sum_{i=0}^{\log_2(n)-1}2^iO(\sqrt{\frac{n}{2^i}})
$$

$$
    \Large T(n) = nT(1) + \sum_{i=0}^{\log_2(n)-1}2^i \sqrt{\frac{n}{2^i}}
$$

$$
    \Large T(n) = n\Theta(1) + \sum_{i=0}^{\log_2(n)-1} \sqrt{2^i} \sqrt{n}
$$

$$
    \Large T(n) = \Theta(n) + \sqrt{n} \sum_{i=0}^{\log_2(n)-1} \sqrt{2^i}
$$

$$
    \Large T(n) = \Theta(n) + \sqrt{n} \sum_{i=0}^{\log_2(n)-1} (2^{\frac{1}{2}})^i
$$

considerando la formula

$$
    \Large \sum_{i=0}^{n} r^i = \frac{r^{n+1} - 1}{r - 1}
$$

si riadatta al nostro caso ottenendo

$$
    \Large \sum_{i=0}^{\log_2(n)-1} (2^{\frac{1}{2}})^i = \frac{(2^{\frac{1}{2}})^{\log_2(n)} - 1}{2^{\frac{1}{2}} - 1}
$$

riprendendo l'equazione precedente

$$
    \Large T(n) = \Theta(n) + \sqrt{n} (\frac{(2^{\frac{1}{2}})^{\log_2(n)} - 1}{2^{\frac{1}{2}} - 1})
$$

$$
    \Large T(n) = \Theta(n) + \sqrt{n} (\frac{n^{\frac{1}{2}} - 1}{2^{\frac{1}{2}} - 1})
$$

$$
    \Large T(n) = \Theta(n) + \sqrt{n} (\frac{\sqrt{n} - 1}{\sqrt{2} - 1})
$$

$$
    \Large T(n) = \Theta(n) + \frac{n - \sqrt{n}}{\sqrt{2} - 1}
$$

$$
    \Large T(n) = \Theta(n) + \Theta(\frac{n - \sqrt{n}}{\sqrt{2} - 1})
$$

$$
    \Large T(n) = \Theta(n) + \Theta(n)  - \Theta(\sqrt{n}) = \Theta(n)
$$
viene così confermato che il costo computazionale dell'algoritmo sia $\Large \Theta(n)$.

## Esercizio 2

Sia dato un array $A$ contenente $n$ interi distinti e ordinati in modo crescente.

Progettare un algoritmo che, in tempo $O(\log(n))$, individui la
posizione più a sinistra nell’array per cui si ha $A[i] \neq i$, l’algoritmo restituisce $-1$ se una tale posizione non esiste.

Ad esempio, per $A = [0, 1, 2, 3, 4]$ l’algoritmo deve restituire $-1$, per $A = [0, 5, 6, 20, 30]$ la risposta deve essere $1$ e per $A = [-3, 1, 2, 3, 6]$ la risposta deve essere $0$.

Dell’algoritmo proposto:

**a)** si dia la descrizione a parole

L'algoritmo da implementare è una variante di ricerca binaria.

- si controlla inizialmente che il primo elemento dell'array sia uguale al suo indice, poichè se non dovesse esserlo, l'elemento cercato sarà proprio quest'ultimo. <br>
Ciò serve anche a sapere che per ogni altro elemento uguale al suo indice presente all'interno dell'array, tutti gli altri elementi precedenti ad esso saranno a loro volta uguali al loro indice.
- una volta concluso il controllo del primo elemento, si passa a l'elemento centrale dell'array.
    - se il valore dell'elemento corrente è uguale al suo indice, la ricerca proseguirà nel sub-array di destra
    - altrimenti, la ricerca proseguirà nel sub-array di sinistra
- vengono ripetuti i passaggi fino a quando non si ha un sub-array con un unico elemento, ritornando -1 se quest'ultimo è uguale al suo indice, altrimenti viene ritornato l'indice dell'elemento di quel sub-array (come richiesto dall'esercizio).

**b)** si scriva lo pseudocodice

```python
def es2(A):
    i = 0
    j = len(A) - 1

    if A[0] != 0:
        return 0

    while i < j:
        m = (i + j) / 2
        if A[m] == m:
            i = m + 1
        else:
            j = m

    if A[i] == i:
        return -1
    return i
```

**c)** si giustifichi il costo computazionale

Il costo computazionale dell'algoritmo è determinato dal ciclo while (dato che tutte le altre operazioni hanno costo $\Large \Theta(1)$ ).

Si analizza quindi il comportamento del ciclo while

<div align="center">

|N Iterazione | 0 | 1 | 2 | 3 | $\Large \dots$ | k |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Lunghezza array | n | $\Large \frac{n}{2}$ | $\Large \frac{n}{4}$ | $\Large \frac{n}{8}$ | $\Large \dots$ | $\Large \frac{n}{2^k}$ |

</div>

il ciclo while terminerà quando $\Large i = j$, ovvero quando la lunghezza del sub-array sarà uguale a 1 $(\Large \frac{n}{2^k} = 1)$, da cui $\Large k = \log_2(n)$.

Viene dunque rispettato il costo dell'algoritmo richiesto dall'esercizio, ovvero $\Large O(\log(n))$.

## Esercizio 3
Progettare un algoritmo che, dato il puntatore alla radice di un albero binario $T$ avente per chiavi degli interi, veriﬁca se l’albero è un albero binario di ricerca.

Ad esempio, l’algoritmo per l’albero sulla sinistra deve restituire *True* mentre per l’albero sulla destra deve restituire *False* (infatti nel sottoalbero di sinistra del nodo con chiave 3 è presente un nodo con chiave 4)

                            10                              3
                          /    \                         /     \
                         /      \                       /       \
                        7       15                     2        10
                       / \     /  \                   / \      /  \
                      /   \   /    \                 /   \    /    \
                     3     9 12    20               1     4  6     20
                              \                               \
                               \                               \
                                14                               8

Il costo computazionale dell’algoritmo proposto deve essere $\Theta(n)$ dove n è il
numero di nodi dell’albero.

Dell’algoritmo proposto

**a)** si dia la descrizione a parole

Un *albero binario di ricerca (Binary Search Tree)* è un albero binario in cui i nodi sono organizzati in modo tale che, per ogni nodo

- tutti i nodi del sottoalbero sinistro abbiano chiavi minori della chiave del nodo 
- e tutti i nodi del sottoalbero destro abbiano chiavi maggiori della chiave del nodo.

Per verificare che l'albero rispetti queste proprietà, lo si visita

**b)** si scriva lo pseudocodice

```python
def es3(r):

    # per verificare che l'albero sia un albero binario di ricerca
    # lo si visita in-order appendendo le chiavi in una lista ausiliaria
    Nodi_Albero = []
    es3_InOrder(r, Nodi_Albero)

    # si controlla che la lista ausiliaria sia totalmente ordinata
    for i in range(1,len(Nodi_Albero)):

        # nel caso ci sia anche solo un elemento non ordinato
        # vuol dire che l'albero non è un albero binario di ricerca
        if Nodi_Albero[i] <= Nodi_Albero[i-1]:
            return False

    # altrimenti l'albero è un albero binario di ricerca
    return True

def es3_InOrder(r, A):
    if not r:
        return
    es3_InOrder(r.left, A)
    A.append(r.key)
    es3_InOrder(r.right, A)
```

**c)** si giustifichi il costo computazionale

Si analizza il il costo di entrambe le funzioni

- **es3_InOrder**: l'equazione di ricorrenza è determinata

    - dal caso base, ovvero quando il nodo è nullo, con costo $\Large \Theta(1)$

    - dal caso generale, in cui sono presenti

        - un'istruzione elementare (costo $\Theta(1)$ )
        - due chiamate ricorsive, (una per il sotto-albero sinistro e una per il sotto-albero destro) con rispettivi costi $T(k)$ e $T(n-k-1)$, dove

            - $k$ è il numero di nodi del sotto-albero sinistro
            - e $n-k-1$ è il numero di nodi del sotto-albero destro.

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

$\Large T(n) = 2T(\frac{n}{2}) + \Theta(1)$ può essere rappresentata come $\Large T(n) = aT(\frac{n}{b}) + f(n)$

con $\Large a = 2$, $\Large b = 2$ e $\Large f(n) = \Theta(1)$

bisogna dimostrare, per qualche costante $\Large \epsilon > 0$, che $\Large f(n)$ sia in $\Large O(n^{\log_b(a)-\epsilon})$,

dove $\Large n^{\log_b(a)} = n^{\log_2(2)} = n^1 = n$

scegliendo $\Large \epsilon = 1$, $\Large n^{\log_b(a)-\epsilon}$ sarà uguale a $\Large n^0 = 1$, e sapendo che se $\Large f(n) = \Theta(1)$

allora vale anche $\Large f(n) = O(1)$, concludendo che $\Large T(n) = \Theta(n^{\log_b(a)}) = \Theta(n)$

avendo trovato come caso peggiore $\Large T(n) = O(n)$ e come caso migliore $\Large T(n) = \Omega(n)$, si conclude che il costo computazionale dell'algoritmo sia $\Large T(n) = \Theta(n)$

si conclude che il costo computazionale della funzione sia $\Large \Theta(n)$

- **es3**: il costo della funzione è principalmente determinato

    - dal costo della funzione **es3_InOrder**, ovvero $\Large \Theta(n)$

    - dal costo del ciclo for, con anch'esso costo $\Large \Theta(n)$, in quanto vengono eseguite per $\Large n$ volte delle operazioni elementari

dunque il costo computazionale sarà dato da

$$
    \Large T(n) = \Theta(n) + \Theta(n) = \Theta(n)
$$

rispettando cosi la richiesta dell'esercizio

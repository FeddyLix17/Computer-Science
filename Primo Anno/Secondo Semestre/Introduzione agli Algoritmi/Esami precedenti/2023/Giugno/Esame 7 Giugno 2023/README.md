# <p align="center"> Esame 7 Giugno 2023 </p>

## Esercizio 1
Si consideri la seguente funzione:
```python
def Es1(n):
    if n < 5:
        return n
    s = k = n
    while k > 1:
        s += k
        k = k / 3
    return s + Es1(n − 1)
```

**a)** Si analizza il codice per impostare la relazione di ricorrenza che ne definisce il tempo di esecuzione

- si rientra nel caso base per $n < 5$, con costo $\Theta(1)$, quindi $T(n) = \Theta(1)$ per $n < 5$
- altrimenti, il costo della funzione è dato dalla somma del costo del ciclo *while* e quello della singola chiamata ricorsiva con parametro $n-1$

il ciclo while ha inizio con $k = n$, e termina quando $k = 1$, utilizzando una variabile ausiliaria $z$ per indicare il numero di iterazioni del ciclo, si analizza il valore di $k$ dopo ogni iterazione:

<div align="center">

| Iterazione | 0 | 1 | 2 | 3 | ... | $z$ |
|:----------:| :---: | :---: | :---: | :---: | :---: | :---: |
| $k$ | $n$ | $\Large\frac{n}{3}$ | $\Large\frac{n}{3^2}$ | $\Large\frac{n}{3^3}$ | ... | $\Large\frac{n}{3^z}$ |

</div>

il ciclo termina quando $k = 1$, ovvero quando $\large\frac{n}{3^z} = 1$

$$\frac{n}{3^z} = 1 \implies n = 3^z \implies z = \log_3(n)$$

trovato il numero di iterazioni del ciclo while in relazione all'input $n$, si conclude che il costo di quest'ultimo sia logaritmico, ovvero $\Theta(\log(n))$.
Unito al costo della singola chiamata ricorsiva con parametro $n-1$, si ottiene l'equazione $T(n) = T(n-1) + \Theta(\log(n))$ per $n \geq 5$.

In conclusione, la relazione di ricorrenza che definisce il tempo di esecuzione della funzione sarà data da

<div align="center">

\- $T(n) = T(n-1) + \Theta(\log(n))$ , $n \geq 5$

\- $T(n) = \Theta(1)$ , $n < 5$

</div>

**b)** Si risolve la ricorrenza con la possibilità di utilizzare un metodo a scelta tra quelli trattati durante il corso, si sceglie di usare il metodo iterativo

si sviluppa la ricorrenza per analizzare il suo andamento

$$
    T(n) = T(n-1) + \Theta(\log(n))
$$

$$
    T(n) = [T(n-2) + \Theta(\log(n-1))] + \Theta(\log(n))
$$

$$
    T(n) = \{[T(n-3) + \Theta(\log(n-2))] + \Theta(\log(n-1))\} + \Theta(\log(n))
$$

generalizzabile usando una variabile ausiliare $k$ in 

$$
    T(n) = T(n-k) + \sum_{i=0}^{k-1} \Theta(\log(n-i))
$$

verrà raggiunto il caso base quando $n-k < 5$, ovvero quando $n - k = 4$ da cui $k = n - 4$

$$
    T(n) = T(n - (n - 4)) + \sum_{i=0}^{n-4-1} \Theta(\log(n-i))
$$

$$
    T(n) = T(4) + \sum_{i=0}^{n-5} \Theta(\log(n-i))
$$

$$
    T(n) = \Theta(1) + \sum_{i=0}^{n-5} \Theta(\log(n-i))
$$

$$
    T(n) = \Theta(1) + [log(n) + log(n-1) + log(n-2) + ... + log(5)]
$$

per le proprietà dei logaritmi $log(a) + log(b) = log(ab)$, quindi la sommatoria estesa può essere riscritta come $log(n(n-1)(n-2)...(5)) = log(\Large\frac{n!}{4!})$, in quanto bisogna escludere $log(4), log(3), log(2)$ e $log(1)$ ottendendo infine $T(n) = \Theta(1) + \Theta(log(\Large\frac{n!}{4!}))$ = $\Theta(log(n!))$

usando [l'approssimazione di Stirling](https://math.stackexchange.com/questions/140961/why-is-logn-on-log-n), si dimostra che $log(n!) = \Theta(nlog(n))$,

concludendo che $T(n) = \Theta(nlog(n))$

## Esercizio 2

Dato un array $A$ di $n$ interi compresi tra $0$ a $50$, sapendo che nell’array sono certamente presenti dei duplicati, si vuole determinare la distanza massima tra le posizioni di due elementi duplicati in A.

Ad esempio per $A = [3, 3, 4, 6, 6, 3, 5, 5, 5, 6, 6, 9, 9, 1]$ i soli elementi che in A si ripetono sono 3, 6 e 9.

- La distanza massima tra duplicati del $3$ è $5$,

- la distanza massima tra duplicati del $6$ è $7$,

- la distanza massima tra duplicati del $9$ è $1$.

quindi la risposta per l’array $A$ è $7$.

Progettare un algoritmo che, dato $A$, in tempo $\Theta(n)$ restituisca
la distanza massima tra le posizioni con elementi duplicati.
Dell’algoritmo proposto:

**a)** si scriva lo pseudocodice opportunamente commentato

```python
def es2(A):
    # creo un array C di 51 elementi inizializzandoli a 0, i quali conterranno 
    # rispettivamente l'indice della prima occorrenza dell'elemento i-esimo 
    # (che sappiamo essere un numero compreso tra 0 e 50) di A ad esempio 
    # se A = [2, 4, 3, 0, 1], C = [3, 4, 0, 2, 1]
    # in quanto A[0] = 2, C[A[0]] = C[2] = 0, A[1] = 4, C[A[1]] = C[4] = 1, ecc...
    C = [0] * 51

    # avendo la certezza che in A siano presenti duplicati, inizializzo la
    # distanza m tra due elementi duplicati a 1 invece che a 0, 
    # in quanto distanza minima possibile tra due elementi
    m = 1

    # scorro A
    for i in range(len(A)):
        if C[A[i]] == 0:
            # se C[A[i]] = 0, significa che è la prima occorrenza dell'elemento i-esimo di A
            # quindi salvo l'indice i in C[A[i]]
            C[A[i]] = i
        else:
            # altrimenti, significa che l'elemento i-esimo di A è già stato incontrato 
            # in precedenza, quindi bisognerà calcolare la distanza tra l'indice i e l'indice 
            # salvato in C[A[i]], aggiornando m se la distanza appena calcolata
            # risulta maggiore della massima distanza trovata finora
            m = max(m, i - C[A[i]])

    # finito di scorrere A, restituisco la distanza massima trovata
    return m
```
**b)** si giustifichi il costo computazionale

il costo computazionale dell'algoritmo è $\Theta(n)$, in quanto si scorre l'array $A$ una sola volta, eseguendo operazioni elementari, quindi tutte con costo $\Theta(1)$, per ogni elemento di $A$

## Esercizio 3

Dato il puntatore $r$ al nodo radice di un albero binario non vuoto, progettare un algoritmo ricorsivo che in tempo $\Theta(n)$ calcoli il numero di nodi che hanno esatta mente $2$ figli e chiave pari.

Ad esempio, per l’albero in figura, 

                                                     0
                                                  /     \
                                                 /       \
                                                2         5
                                               / \       / \
                                              /   \     /   \
                                             1     7   6    -40
                                                  /         / 
                                                 /         /
                                                9        -35



l’algoritmo deve restituire
2, per la presenza dei nodi con chiavi $2$ e $0$.

L’albero è memorizzato tramite puntatori e record di tre campi:

- il campo key contenente il valore
- ed i campi left e right con i puntatori al figlio sinistro e al figlio destro, rispettivamente (questi puntatori valgono None in mancanza del figlio).

Dell’algoritmo proposto:

**a)** si scriva lo pseudocodice opportunamente commentato

```python
def es3(r):
    # visito l'albero in post-ordine, quindi visitando il
    # sottoalbero sinistro, il sottoalbero destro e infine la radice.
    # se arrivo ad una foglia, restituisco 0, perché sicuramente non avrà
    # 2 figli e chiave pari
    if r == None:
        return 0
    
    # uso una variabile ausiliaria a per contare il numero di nodi che hanno
    # esattamente 2 figli e chiave pari, inizializzandola per 
    # ogni chiamata ricorsiva a 0
    a = 0
    if r.key % 2 == 0 and r.left != None and r.right != None:
        # se la chiave del nodo corrente è pari e ha esattamente 2 figli,
        # incremento a di 1
        a+= 1

    # restituisco ricorsivamente la somma del numero di nodi che hanno
    # esattamente 2 figli e chiave pari del sottoalbero sinistro, del
    # sottoalbero destro e del nodo corrente
    return a + es3(r.left) + es3(r.right)
```
**b)** si giustifichi il costo computazionale

il costo computazionale dell'algoritmo è appunto quello di una visita completa di un albero in post-ordine, riconducibile alla seguente equazione di ricorrenza

<div align="center">

\- $T(n) = T(k) + T(n − k − 1) + \Theta(1)$

\- $T(0) = \Theta(1)$

</div>

dove $n$ è il numero di nodi dell'albero, $k$ è il numero di nodi del sottoalbero sinistro, $n-k-1$ è il numero di nodi del sottoalbero destro.

Per determinarne il costo, si analizzano caso migliore e caso peggiore:

- **caso peggiore**: l'albero è completamente sbilanciato, quindi quando tutti i nodi sono aggregati o nel sottoalbero sinistro o nel sottoalbero destro, ovvero quando $k = 0$ oppure $n - k - 1 = 0$, sostituendo i valori nell'equazione di ricorrenza si ottiene la medesima equazione di ricorrenza del caso migliore

    - per $k = 0$

    $$
        T(n) = T(0) + T(n - 0 - 1) + \Theta(1) = T(n - 1) + \Theta(1)
    $$

    - per $n - k - 1 = 0$ (ovvero $k = n - 1$)

    $$
        T(n) = T(n - 1) + T(0) + \Theta(1) = T(n - 1) + \Theta(1)
    $$

usando il metodo iterativo per risolvere l'equazione di ricorrenza, si ottiene

$$
    T(n) = T(n - 1) + \Theta(1) = [T(n - 2) + \Theta(1)] + \Theta(1)
$$

$$
    T(n) = \{[T(n - 3) + \Theta(1)] + \Theta(1)\} + \Theta(1)
$$

generalizzando con una variabile ausiliaria $k$ in

$$
    T(n) = T(n - k) + k\Theta(1)
$$

verrà raggiunto il caso base quando $n - k = 0$, ovvero quando $k = n$, da cui

$$
    T(n) = T(n - n) + n\Theta(1) = T(0) + n\Theta(1) = \Theta(1) + n\Theta(1) = \Theta(n)
$$

- **caso migliore**: l'albero è completo, quindi quando ogni nodo padre ha esattamente 2 figli, ovvero quando sia il sottoalbero sinistro che il sottoalbero destro hanno $\Large\frac{n-1}{2}$ nodi, sostituendo i valori nell'equazione di ricorrenza si ottiene

$$
T(n) = T(\frac{n-1}{2}) + T(\frac{n-1}{2}) + \Theta(1) \approx 2T(\frac{n}{2}) + \Theta(1)
$$

utilizzando il metodo principale, si ricade nel primo caso

$T(n) = 2T(\frac{n}{2}) + \Theta(1)$ può essere rappresentata come $T(n) = aT(\frac{n}{b}) + f(n)$

con $a = 2$, $b = 2$ e $f(n) = \Theta(1)$

bisogna dimostrare, per qualche costante $\epsilon > 0$, che $f(n)$ sia in $O(n^{\log_b(a)-\epsilon})$,

dove $n^{\log_b(a)} = n^{\log_2(2)} = n^1 = n$

scegliendo $\epsilon = 1$, $n^{\log_b(a)-\epsilon}$ sarà uguale a $n^0 = 1$, e sapendo che se $f(n) = \Theta(1)$

allora vale anche $f(n) = O(1)$, concludendo che $T(n) = \Theta(n^{\log_b(a)}) = \Theta(n)$

avendo trovato come caso peggiore $T(n) = O(n)$ e come caso migliore $T(n) = \Omega(n)$, si conclude che il costo computazionale dell'algoritmo sia $T(n) = \Theta(n)$
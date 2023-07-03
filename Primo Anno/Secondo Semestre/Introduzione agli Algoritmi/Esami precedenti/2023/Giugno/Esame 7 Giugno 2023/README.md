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

- si rientra nel caso base per $\Large n < 5$, con costo $\Large \Theta(1)$, quindi $\Large T(n) = \Theta(1)$ per $\Large n < 5$
- altrimenti, il costo della funzione è dato dalla somma del costo del ciclo *while* e quello della singola chiamata ricorsiva con parametro $\Large n-1$

il ciclo while ha inizio con $\Large k = n$, e termina quando $\Large k = 1$, utilizzando una variabile ausiliaria $\Large z$ per indicare il numero di iterazioni del ciclo, si analizza il valore di $\Large k$ dopo ogni iterazione:

<div align="center">

| Iterazione | 0 | 1 | 2 | 3 | ... | $z$ |
|:----------:| :---: | :---: | :---: | :---: | :---: | :---: |
| $k$ | $n$ | $\Large\frac{n}{3}$ | $\Large\frac{n}{3^2}$ | $\Large\frac{n}{3^3}$ | ... | $\Large\frac{n}{3^z}$ |

</div>

il ciclo termina quando $\Large k = 1$, ovvero quando $\Large \frac{n}{3^z} = 1$

$$
\Large \frac{n}{3^z} = 1 \implies n = 3^z \implies z = \log_3(n)
$$

trovato il numero di iterazioni del ciclo while in relazione all'input $\Large n$, si conclude che il costo di quest'ultimo sia logaritmico, ovvero $\Large \Theta(\log(n))$.
Unito al costo della singola chiamata ricorsiva con parametro $\Large n-1$, si ottiene l'equazione

$\Large T(n) = T(n-1) + \Theta(\log(n))$ per $\Large n \geq 5$.

In conclusione, la relazione di ricorrenza che definisce il tempo di esecuzione della funzione sarà data da

<div align="center">

\- $\Large T(n) = T(n-1) + \Theta(\log(n))$ , $\Large n \geq 5$

\- $\Large T(n) = \Theta(1)$ , $\Large n < 5$

</div>

**b)** Si risolve la ricorrenza con la possibilità di utilizzare un metodo a scelta tra quelli trattati durante il corso, si sceglie di usare il metodo iterativo

si sviluppa la ricorrenza per analizzare il suo andamento

$$
    \Large T(n) = T(n-1) + \Theta(\log(n))
$$

$$
    \Large T(n) = [T(n-2) + \Theta(\log(n-1))] + \Theta(\log(n))
$$

$$
    \Large T(n) = \{[T(n-3) + \Theta(\log(n-2))] + \Theta(\log(n-1))\} + \Theta(\log(n))
$$

generalizzabile usando una variabile ausiliare $k$ in 

$$
    \Large T(n) = T(n-k) + \sum_{i=0}^{k-1} \Theta(\log(n-i))
$$

verrà raggiunto il caso base quando $\Large n-k < 5$, ovvero quando $\Large n - k = 4$ da cui $\Large k = n - 4$

$$
    \Large T(n) = T(n - (n - 4)) + \sum_{i=0}^{n-4-1} \Theta(\log(n-i))
$$

$$
    \Large T(n) = T(4) + \sum_{i=0}^{n-5} \Theta(\log(n-i))
$$

$$
    \Large T(n) = \Theta(1) + \sum_{i=0}^{n-5} \Theta(\log(n-i))
$$

$$
    \Large T(n) = \Theta(1) + [log(n) + log(n-1) + log(n-2) + ... + log(5)]
$$

per le proprietà dei logaritmi $\Large log(a) + log(b) = log(ab)$, quindi la sommatoria estesa può essere riscritta come $\Large log(n(n-1)(n-2)...(5)) = log(\Large\frac{n!}{4!})$, in quanto bisogna escludere $\Large log(4), log(3), log(2)$ e $\Large log(1)$ ottendendo infine $\Large T(n) = \Theta(1) + \Theta(log(\Large\frac{n!}{4!}))$ = $\Theta(log(n!))$

usando [l'approssimazione di Stirling](https://math.stackexchange.com/questions/140961/why-is-logn-on-log-n), si dimostra che $\Large log(n!) = \Theta(nlog(n))$,

concludendo che $\Large T(n) = \Theta(nlog(n))$

## Esercizio 2

Dato un array $\Large A$ di $\Large n$ interi compresi tra $\Large 0$ a $\Large 50$, sapendo che nell’array sono certamente presenti dei duplicati, si vuole determinare la distanza massima tra le posizioni di due elementi duplicati in $\Large A$.

Ad esempio per $\Large A = [3, 3, 4, 6, 6, 3, 5, 5, 5, 6, 6, 9, 9, 1]$ i soli elementi che in $\Large A$ si ripetono sono $\Large 3$, $\Large 6$ e $\Large 9$.

- La distanza massima tra duplicati del $\Large 3$ è $\Large 5$,

- la distanza massima tra duplicati del $\Large 6$ è $\Large 7$,

- la distanza massima tra duplicati del $\Large 9$ è $\Large 1$.

quindi la risposta per l’array $\Large A$ è $\Large 7$.

Progettare un algoritmo che, dato $\Large A$, in tempo $\Large \Theta(n)$ restituisca
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

il costo computazionale dell'algoritmo è $\Large \Theta(n)$, in quanto si scorre l'array $\Large A$ una sola volta, eseguendo operazioni elementari, quindi tutte con costo $\Large \Theta(1)$, per ogni elemento di $\Large A$

## Esercizio 3

Dato il puntatore $\Large r$ al nodo radice di un albero binario non vuoto, progettare un algoritmo ricorsivo che in tempo $\Large \Theta(n)$ calcoli il numero di nodi che hanno esatta mente $\Large 2$ figli e chiave pari.

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



l’algoritmo deve restituire $\Large 2$, per la presenza dei nodi con chiavi $\Large 2$ e $\Large 0$.

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

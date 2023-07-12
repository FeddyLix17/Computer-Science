# <p align="center"> Esame 5 Luglio 2023 </p>


## Esercizio 1

Si consideri la seguente funzione

```python
def es1(n):
    s = 0
    if n > 4:
        m = n / 2
        s = es1(n / 4) + es1(m - n / 4)
        i = 1
        while i * i <= n:
            i += 1
            s += i
    return s
```

**a)** La relazione di ricorrenza sarà data da

- il costo delle 2 chiamate ricorsive, con parametri $\Large \frac{n}{4}$ e $\Large m - \frac{n}{4}$, dove $\Large m = \frac{n}{2}$, da cui il secondo parametro sarà $\Large \frac{n}{2} - \frac{n}{4} \implies \frac{2n - n}{4} \implies \frac{n}{4}$ <br> <br> il costo di queste 2 chiamate ricorsive sarà quindi $\Large 2T\left(\frac{n}{4}\right)$


- il costo del ciclo while, determinato dalla condizione di uscita $\Large i * i > n$, usando una variabile ausiliaria $k$ si analizza il suo comportamento

<div align="center">

| N iterazione | 0 | 1 | 2 | 3 | ... | k |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| i | 1 | 2 | 3 | 4 | ... | $k + 1$ |
| $i^2$ | 1 | 4 | 9 | 16 | ... | $(k + 1)^2$ |

</div>

il ciclo while terminerà quando $\Large i^2 > n$, quindi quando $\Large (k + 1)^2 > n$, da cui

$$
    \Large (k + 1)^2 = n + 1
$$

$$
    \Large k + 1 = \sqrt{n + 1}
$$

$$
    \Large k = \sqrt{n + 1} - 1
$$

il costo del ciclo while sarà quindi $\Large \Theta (\sqrt{n + 1} - 1) \implies \Theta (\sqrt{n})$

calcolati tutti costi necessari, la relazione di ricorrenza finale sarà

$$
    - T(n) = 2T\left(\frac{n}{4}\right) + \Theta (\sqrt{n}),\ n > 4
$$

$$
    - T(n) = \Theta(1),\ n \leq 4
$$

** b)** Si prova a risolvere la ricorrenza usando il metodo principale

generalizzando la ricorrenza in $\Large T(n) = aT\left(\frac{n}{b}\right) + f(n)$,

si individuano i parametri $\Large a = 2$, $\Large b = 4$ e $\Large f(n) = \Theta (\sqrt{n})$

$ \Large n^{\log_b a}$ sarà uguale a $\Large n^{\log_4 2} = n^{\frac{1}{2}} = \sqrt{n}$

si rientra nel caso in cui $\Large f(n) = \Theta (n^{\log_b a})$, quindi nel secondo caso del metodo principale

il costo totale dell'algoritmo sarà quindi $\Large T(n) = \Theta (n^{\log_b a} \log n) = \Theta (\sqrt{n} \log n)$

## Esercizio 2

In un array ordinato $A$ di $n$ interi compaiono tutti gli interi da $0$ a $n-2$.

Esiste dunque nell'array un unico elemento duplicato.


Si progetti un algoritmo ITERATIVO che, dato $A$, in tempo $\Theta(log(n))$ restituisca l'elemento duplicato.

Ad esempio, per $A = [0, 1, 2, 3, 4, 4, 5, 6, 7]$ l'algoritmo deve restituire 4.

Dell'algoritmo proposto:

a) si scriva il codice python opportunamente commentato

```python
def es2(A):
    # è possibile sfruttare l'efficenza della ricerca binaria
    # in quanto l'array è già ordinato
    # e sapendo che gli elementi dell'array sono tutti distinti e presenti tranne uno
    # una metà degli elementi dell'array avrà indice uguale al proprio valore

    # si inizializzano i due indici left e right rappresentanti
    # rispettivamente l'indice iniziale e finale dell'array-subarray
    left = 0
    right = len(A) - 1

    # si continua a ciclare finchè left e right non saranno uguali
    # quindi quando ci sarà un subarray di un solo elemento
    # che sarà proprio l'elemento duplicato
    while left < right:

        # si calcola il centro dell'array-subarray
        mid = (left + right) / 2

        # se l'elemento in posizione mid è uguale al suo indice
        # l'elemento duplicato si trova nella parte destra
        if A[mid] == mid:
            left = mid + 1

        # altrimenti si trova nella parte sinistra
        else:
            right = mid

    # una volta usciti dal ciclo while
    # left e right saranno uguali
    # quindi possono essere scelti entrambi per restituire l'elemento duplicato
    # in questo caso si sceglie left
    return A[left]
```

**b)** si giustifichi il costo computazionale

il costo computazionale dell'algoritmo è regolato principalmente dal ciclo while, in quanto il resto delle operazioni sono tutte con costo $\Theta(1)$

- il ciclo while ha come condizione di uscita $\Large left < right$, ovvero quando la lunghezza dell'array n sarà 1 con left e right che puntano alla stessa posizione

si analizza la lunghezza dell'array ad ogni iterazione del ciclo while
usando una variabile ausiliaria $k$

<div align="center">

| N iterazione | 0 | 1 | 2 | 3 | ... | k |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| lunghezza array | n | $\Large \frac{n}{2}$ | $\Large \frac{n}{4}$ | $\Large \frac{n}{8}$ | ... | $\Large \frac{n}{2^k}$ |

</div>

il ciclo while terminerà quando $\Large \frac{n}{2^k} = 1$, da cui

$$
    \Large \frac{n}{2^k} = 1
$$

$$
    \Large n = 2^k
$$

$$
    \Large \log_2(n) = k \implies k = \log_2(n)
$$

il costo del ciclo while, nonchè costo finale dell'algoritmo, sarà quindi $\Large \Theta(\log_2(n))$

## Esercizio 3

Data una lista puntata, diremo che i due record che occupano le posizioni (2i -1)-esima e 2i-esima (i>=1) vengono accorpati eliminando dalla lista quello in posizione pari, e trasformando la chiave del record in posizione dispari nella somma dei due elementi accorpati.

Se lista ha un numero dispari di nodi, allora l'ultimo nodo, che non può accorparsi, viene semplicemente eliminato.

Sia dato il puntatore p al nodo di testa di una lista puntata memorizzata tramite puntatori a nodi a due campi:

- il campo key contiene il valore
- ed il campo next contenente il puntatore al nodo successivo (il campo next dell'ultimo nodo della lista vale None).

Si progetti un algoritmo RICORSIVO che, in tempo $\Theta(n)$, ne accorpi a coppie tutti i suoi nodi (il primo con il secondo, il terzo col quarto ecc.).

Ad esempio, la lista seguente va modificata come in figura:


                                3 --> 2 --> 8 --> -4 --> 6 --> 1 --> 2
                                5 --------> 4 ---------> 7

dell'algoritmo proposto:

a) si scriva lo pseudocodice opportunamente commentato

```python
def es3(p):
    # se si finisce di scorrere la lista o se si arriva ad un nodo
    # che non presenta un nodo successivo accorpabile ad esso
    # si restituisce None per fare in modo che il nodo precedente
    # non punti ad esso (facendolo puntare a None)
    if p == None or p.next == None:
        return None

    # mentre finchè si sta scorrendo la lista
    else:
        # partendo dalla testa accorpo il nodo corrente con il successivo
        # sommando le chiavi dei due nodi
        p.key += p.next.key

        # facendo puntare il nodo corrente al nodo successivo del successivo
        # in modo da "eliminare" il nodo appena accorpato
        # eseguendo ricorsivamente le seguenti operazioni
        # per ogni nodo pari
        p.next = es3(p.next.next)
    
    # ritorno ricorivamente il puntatore al nodo
    # della chiamata ricorsiva corrente
    # cosi da avere alla fine la nuova lista accorpata
    # con puntatore alla sua testa
    return p
```

**b)** si giustifichi il costo computazionale

l'equazione di ricorrenza dell'algoritmo è regolata principalmente dalla ricorsione, in quanto il resto delle operazioni sono tutte con costo $\Theta(1)$

la chiamata ricorsiva ha come parametro $\Large p.next.next$, quindi ad ogni chiamata viene eseguito un salto di 2 nodi, portando ad un a riduzione della lunghezza della lista di 2, da cui

$$
    \Large - T(n) = T(n - 2) + \Theta(1)
$$

unito al caso base, nel quale si rientrerà quando la lunghezza della lista sarà 0, (ovvero quando si finisce di scorrere la lista o quando si arriva ad un nodo che non presenta un nodo successivo accorpabile ad esso)

$$
    \Large - T(n) = \Theta(1),\ n = 0
$$

si ottiene l'equazione di ricorrenza finale

$$
    \Large - T(n) = T(n - 2) + \Theta(1),\ n \geq 1
$$

$$
    \Large - T(n) = \Theta(1),\ n = 0
$$

usando il metodo iterativo si sviluppa la ricorrenza

$$
    \Large T(n) = T(n - 2) + \Theta(1)
$$

$$
    \Large T(n) = [T(n - 4) + \Theta(1)] + \Theta(1)
$$

$$
    \Large T(n) = \{[T(n - 6) + \Theta(1)] + \Theta(1)\} + \Theta(1)
$$

generalizzabile in

$$
    \Large T(n) = T(n - 2k) + k\Theta(1)
$$

verrà ragginto il caso base quando $\Large n - 2k = 0$, da cui

$$
    \Large n - 2k = 0
$$

$$
    \Large n = 2k
$$


$$
    \Large \frac{n}{2} = k \implies k = \frac{n}{2}
$$

sostituendo k nell'equazione di ricorrenza

$$
    \Large T(n) = T(n - 2(\frac{n }{2})) + \frac{n}{2}\Theta(1)
$$

$$
    \Large T(n) = T(n - n) + \Theta(\frac{n}{2})
$$

$$
    \Large T(n) = T(0) + \Theta(n)
$$

$$
    \Large T(n) = \Theta(1) + \Theta(n) \implies \Theta(n)
$$

viene rispettata la richiesta di costo $\Large \Theta(n)$ dell'algoritmo
# <p align="center"> Esame 12 Settembre 2023 </p>

## <p align="center"> Esercizio 1 </p>

Siano:

$$
    \Large T(n) = 8*T(\frac{n}{2}) + \Theta(n^2)
$$

la funzione di costo di un algoritmo ricorsivo A, e

$$
    \Large T(n) = b*T (\frac{n}{4}) + \Theta(n^2)
$$

la funzione di costo di un altro algoritmo ricorsivo A′, dove b è una costante intera positiva, e per entrambe le ricorrenze vale

$$
    \Large T(1) = \Theta(1)
$$

Qual è il minimo valore intero della costante b che rende A asintoticamente più veloce di A′?

Dettagliare il ragionamento ed i passaggi del calcolo, giustificando ogni affermazione.

---

Applicando il teorema principale alla ricorrenza di A, ovvero

$$
    \Large T(n) = 8*T(\frac{n}{2}) + \Theta(n^2), \quad n > 1
$$

$$
    \Large T(n) = \Theta(1), \quad n = 1
$$

vengono individuati $\Large a = 8$, $\Large b = 2$ e $\Large f(n) = \Theta(n^2)$.

$\Large n^{\log_b(a)}$ sarà uguale a $\Large n^{\log_2(8)} \implies n^3$

e scegliendo una costante $\Large \epsilon = 1$ viene rispettata la condizione del primo caso per la quale

$$
    \Large f(n) = O(n^{3 - \epsilon}) \implies f(n) = O(n^1) \implies f(n) = O(n^2)
$$

concludendo che il costo dell'algoritmo A sia uguale a

$$
    \Large \Theta(n^{\log_b(a)}) \implies \Theta(n^3)
$$

Ora applicando il teorema anche alla ricorrenza di A', ovvero

$$
    \Large T(n) = b*T(\frac{n}{4}) + \Theta(n^2), \quad n > 1
$$

$$
    \Large T(n) = \Theta(1), \quad n = 1
$$

vengono individuati $\Large a = 4$ e $\Large f(n) = \Theta(n^2)$.

Bisognerà trovare il minimo valore intero di b per il quale

$$
    \Large log_a(b) \implies log_4(b) > 3
$$

cosi da rendere il costo dell'algoritmo A asintoticamente più veloce di A'.

Sapendo che $\Large log_4(64) = 3$, si conclude che il minimo valore intero di b sia 65.

<br>

## <p align="center"> Esercizio 2 </p>

Dato un array *A* di *n* interi, si scriva un algoritmo iterativo *MaxSequenzaElementiUguali* che calcoli il numero di elementi della più lunga porzione di *A* costituita interamente da elementi consecutivi uguali tra loro.

Ad esempio, se *A = [5, 7, 3, 3, 8, 9, 9, 9, 5, 3, 2, 2]*, allora la risposta è *3* in quanto la porzione *[9, 9, 9]* è la più lunga formata da elementi consecutivi tutti uguali.

Dell’algoritmo proposto:

---

a) si scriva lo pseudocodice opportunamente commentato

```python
def es2(A):

    # indice ultimo elemento dell'array
    n = len(A) - 1

    # indice di scorrimento dell'array
    i = 0

    # valore di ritorno dela funzione
    res = 0

    # finchè non si finisce di scorrere l'array
    while i < n:
        # ci si prepara a contare la sequenza corrente
        curres = 1

        # una volta trovata una sequenza, finchè non si finisce
        # di scorrere l'array e l'elemento corrente continua
        # ad essere uguale al successivo
        while i < n and A[i] == A[i + 1]:  
            # si incrementa il contatore della sequenza corrente
            curres += 1

            # continuando a scorrere l'array
            i += 1

        # una volta finita la sequenza corrente, si aggiorna il valore di ritorno
        res = max(res, curres)

        # e si continua a scorrere l'array
        i += 1

    # una volta finito di scorrere l'array, si ritorna il valore maggiore trovato
    return res
```

---

b) si calcoli formalmente il costo computazionale

Indipendentemente

- dal caso migliore (tutti gli elementi sono uguali)

- e dal caso peggiore (tutti gli elementi sono diversi)

i 2 cicli while combinati compiranno sempre n iterazioni, con tutte operazioni elementari al loro interno, concludendo che il costo computazionale dell'algoritmo sia uguale a $\Large \Theta(n)$.

<br>

## <p align="center"> Esercizio 3 </p>

Dato un albero binario non vuoto a valori interi *T* ed un suo nodo *v*, il costo del cammino *radice-v* è definito come la somma dei valori dei nodi nel percorso che va dalla radice al nodo *v* (estremi inclusi).

Vogliamo calcolare il costo del massimo cammino *radice-foglia* di *T*.

Ad esempio nell’albero binario in figura, la risposta è 18, infatti
nell’albero sono presenti quattro diversi cammini radice-foglia
di costo 3, 18, 11 e −70, rispettivamente.

Dato il puntatore *r* al nodo radice di un albero binario non
vuoto a valori interi *T*, progettare un algoritmo ricorsivo che, in tempo $\Large \Theta(n)$, risolva il problema.

L’albero è memorizzato tramite puntatori e record a tre campi:

- il campo *key* contenente il valore

- ed i campi *left* e *right* con i puntatori al figlio sinistro e al figlio destro, rispettivamente (questi puntatori valgono *None* in mancanza del figlio).

Dell’algoritmo proposto:

---

a) si scriva lo pseudocodice opportunamente commentato

```python
def es3(r):

    if r.left:
        cs = es3(r.left)
    
    if r.right:
        cd = es3(r.right)
    
    return max(cs + r.key, cd + r.key)
```

---

b) si giustifichi formalmente il costo computazionale

L'equazione di ricorrenza dell'algoritmo è quella di una visita di un albero, ovvero

$$
    \Large T(n) = T(k) +  T(n - k - 1) + \Theta(1), \quad n > 1
$$

$$
    \Large T(n) = \Theta(1), \quad n = 1
$$

dove

- k è il numero di nodi del sottoalbero sinistro

- e n - k - 1 è il numero di nodi del sottoalbero destro.

Si prova dimostrare, usando il metodo di sostituzione, che il costo dell'algoritmo sia uguale a $\Large \Theta(n)$.

Rimuovendo la notazione asintotica, si ottiene

$$
    \Large T(n) = T(k) +  T(n - k - 1) + c, \quad n > 1
$$

$$
    \Large T(n) = d, \quad n = 1
$$

dove c e d sono costanti.

Bisognerà dimostrare rispettivamente che l'algoitmo sia in $\Large O(n)$ che in $\Large \Omega(n)$.

Per $\Large O(n)$, bisognerà dimostrare che

$$
    \Large T(n) \leq e*n
$$

- *passo base* con $\Large n = 1$

$$
    \Large d \leq e \implies e \geq d
$$

- *passo induttivo*

$$
    \Large T(n) \leq e*n
$$

$$
    \Large T(k) +  T(n - k - 1) + c \leq e*n
$$

dando per assunto che siano vere anche le condizioni

$$
    \Large T(k) \leq e*k
$$

e

$$
    \Large T(n - k - 1) \leq e*(n - k - 1)
$$

si ottiene il nuovo passo induttivo da dimostrare

$$
    \Large e*k + e*(n - k - 1) + c \leq e*n
$$

$$
    \Large e*k + e*n - e*k - e + c \leq e*n
$$

$$
    \Large - e + c \leq 0
$$

$$
    \Large - e \leq -c
$$

$$
    \Large e \geq c
$$

siccome esisterà sempre una costante $\Large e$ tale che

$$
    \Large e \geq c \quad \land \quad e \geq d
$$

si può concludere che l'algoitmo sia in $\Large O(n)$.

Allo stesso modo l'algoritmo sarà in $\Large \Omega(n)$ per ogni costante $\Large e$ tale che

$$
    \Large e \leq c \quad \land \quad e \leq d
$$

concludendo infine che l'algoitmo sia in $\Large \Theta(n)$.

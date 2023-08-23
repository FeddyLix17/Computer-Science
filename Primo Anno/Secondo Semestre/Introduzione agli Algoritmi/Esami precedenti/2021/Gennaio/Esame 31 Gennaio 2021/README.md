# <p align="center"> Esame 31 Gennaio 2021 </p>

## <p align="center"> Esercizio 1 </p>

Si consideri la seguente funzione:

```python
def Exam(n):
    tot = n
    if n <= 1:
        return tot
    j = 512
    while j >= 2:
        k = 0
        while 3*k <= n:
            k = k + 1
        tot = tot + Exam(k)
        j = j/2
    return tot
```

---

**a)** Si imposti la relazione di ricorrenza che ne definisce il tempo di esecuzione giustificando dettagliatamente l’equazione ottenuta

si rientrerà nel caso base per ogni $\Large n \leq 1$, con relativo costo $\Large \Theta(1)$

$$
    \Large -T(n) = \Theta(1), \quad n \leq 1
$$

il costo del caso generale, invece, sarà determinato

- dal primo ciclo while

- dal secondo ciclo while (annidato al primo)

- dalla chiamata ricorsiva (annidata al primo ciclo)

<br>

- **primo while**

    si analizza il suo comportamento

<div align="center">

| Iterazione | 0 | 1 | 2 | 3 | $\Large \dots$ | $i$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\Large j$ | 512 | 256 | 128 | 64 | $\Large \dots$ | $\Large \frac{512}{2^i}$ |

</div>

il ciclo terminerà quando

$$
    \Large \frac{512}{2^i} = 1
$$

$$
    \Large 512 = 2^i
$$

$$
    \Large log_2(512) = i \implies i = 9
$$

il costo del primo ciclo sarà uguale a $\Large \Theta(9) \implies \Theta(1)$

- **secondo while**

    si analizza il suo comportamento

<div align="center">

| Iterazione | 0 | 1 | 2 | 3 | $\Large \dots$ | $i$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\Large k$ | 0 | 1 | 2 | 3 | $\Large \dots$ | $\Large i$ |
| $\Large 3k$ | 0 | 3 | 6 | 9 | $\Large \dots$ | $\Large 3i$ |

</div>

il ciclo terminerà quando

$$
    \Large 3i = n
$$

$$
    \Large i = \frac{n}{3}
$$

il costo del secondo ciclo sarà uguale a $\Large \Theta(\frac{n}{3}) \implies \Theta(n)$

- **chiamata ricorsiva**

    La chiamata ricorsiva ha come parametro $\Large k$, il quale al termine del secondo ciclo while sarà uguale a $\Large \frac{n}{3}$, il costo della singola chiamata ricorsiva sarà uguale a $\Large T(\frac{n}{3})$.

    La chiamata ricorsiva, essendo dentro il primo ciclo while, verrà eseguita 9 volte, quindi il costo totale delle chiamate ricorsive sarà uguale a $\Large 9T(\frac{n}{3})$.

$$
    \Large - T(n) = 9T(\frac{n}{3}) + \Theta(n), \quad n > 1
$$

$$
    \Large - T(n) = \Theta(1), \quad n \leq 1
$$

---

**b)** Si risolva la ricorrenza usando il metodo principale o un altro metodo ricordando che

$$
    \Large \sum_{i=1}^{k} 3^i = \Theta(3^k)
$$

dettagliando i passaggi del calcolo e giustificando ogni affermazione

Generalizzando la ricorrenza in

$$
    \Large T(n) = aT(\frac{n}{b}) + f(n)
$$

vengono individuati $\Large a = 9$, $\Large b = 3$ e $\Large f(n) = \Theta(n)$.

$\Large n^{\log_b(a)}$ sarà uguale a $\Large n^{log_3(9)} \implies n^2$

rientrando nel primo caso del metodo principale, poiché per $\Large \epsilon = 1$ si ha che

$$
    \Large f(n) = \Theta(n^{log_b(a) - \epsilon}) \implies \Theta(n^{2 - 1}) \implies \Theta(n)
$$

il costo totale della funzione sarà uguale a

$$
    \Large T(n) = \Theta(n^{log_3(9)}) \implies \Theta(n^2)
$$

## <p align="center"> Esercizio 2 </p>

Sia *A* un array di dimensione *n* e *B* un array ordinato di dimensione *m*,
contenenti entrambi numeri interi.

Si vuole trovare il numero di interi di *A* che non sono presenti in *B*.

Progettare un algoritmo ricorsivo che risolva il problema con un costo computazionale asintotico strettamente inferiore a $\Large \Theta(n*m)$.

Ad esempio:

per *A = [8, 1, 2, 12, 10, 11, 20, 2]* e *B = [3, 3, 4, 8, 10, 10, 13, 20, 21, 22]*

l’algoritmo deve restituire 5 (i numeri in A e non in B sono infatti 1, 2, 2, 11, 12.

Dell’algoritmo proposto

---

a) si dia la descrizione a parole

Per ogni elemento di *A* si effettua una ricerca binaria di quest'ultimo in *B*, usando un contatore per tenere traccia del numero di elementi di *A* che **non** sono presenti in *B*, ritornandolo una volta finiti di scorrere gli elementi di *A*.

> **nota**: viene richiesto di progettare un algoritmo ricorsivo, in questo caso solo la funzione di *ricerca binaria* lo sarà, in quanto, per la funzione principale, implementare una soluzione *ricorsiva* rispetto ad una *iterativa* senza la possibilità di utilizzare *strutture dati* di appoggio risulta essere più tedioso.

---

**b)** si scriva lo pseudocodice

```python
def es2(A, B):
    cont = 0
    for i in range(len(A)):
        if ric_bin(B, A[i], 0, len(B) - 1) == -1:
            cont += 1
    return cont

def ric_bin(B, x, s, d):
    m = (s + d) // 2
    if d >= s:
        if array[m] == x:
            return m
        elif array[m] > x:
            return ric_bin(B, x, s, m - 1)
        else:
            return ric_bin(B, x, m + 1, d)
    else:
        return -1
```

---

**c)** si giustifichi il costo computazionale

- ***ric_bin***

    L'equazione di ricorrenza è data da

$$
    \Large - T(m) = T(\frac{m}{2}) + \Theta(1), \quad m > 1
$$

$$
    \Large - T(m) = \Theta(1), \quad m = 1
$$

dove $\Large m$ è la lunghezza dell'array $\Large B$.

Sviluppando la ricorrenza con il metodo iterativo

$$
    \Large T(m) = T(\frac{m}{2}) + \Theta(1)
$$

$$
    \Large T(m) = T(\frac{m}{2^2}) + \Theta(1) + \Theta(1)
$$

$$
    \Large T(m) = T(\frac{m}{2^3}) + \Theta(1) + \Theta(1) + \Theta(1)
$$

generalizzabile in

$$
    \Large T(m) = T(\frac{m}{2^k}) + k\Theta(1)
$$

Si rientrerà nel caso base quando

$$
    \Large \frac{m}{2^k} = 1
$$

$$
    \Large m = 2^k
$$

$$
    \Large log_2(m) = k \implies k = log_2(m)
$$

il costo della funzione di sarà uguale a 

$$ 
    \Large T(m) = T(\frac{m}{2^{log_2(m)}}) + log_2(m)\Theta(1)
$$

$$
    \Large T(m) = T(1) + \Theta(log_2(m))
$$

$$
    \Large T(m) = \Theta(1) + \Theta(log_2(m))
$$

$$
    \Large T(m) = \Theta(log_2(m))
$$

- ***es2***

il costo della funzione è determinato dal ciclo for, il quale scorre tutti gli elementi di *A*, dunque per $\Large n$ iterazioni, dove $\Large n$ è la lunghezza dell'array $\Large A$, compirà $\Large \Theta(log_2(m))$ operazioni al suo interno, da cui

$$
    \Large T(n) = n\Theta(log_2(m)) \implies \Theta(n*log_2(m))
$$

rimanendo strettamente inferiore a $\Large \Theta(n*m)$.

## <p align="center"> Esercizio 3 </p>

Si consideri una lista *L*, in cui ogni elemento è un record a due campi:

- il campo *val* contenente un intero

- ed il campo *next* con il puntatore al nodo seguente (*next* vale *None* per l’ultimo record della lista)

Bisogna contare i record della lista contenenti numeri pari.

Si consideri adesempio la lista *L*, per questa lista bisogna la risposta è 6

                    3 --> 5 --> 2 --> 4 --> 4 --> 8 --> 7 --> 7 --> 1 --> 9 --> 2 --> 2 --> None

Progettare un algoritmo ricorsivo che, dato il puntatore *r* alla testa della lista effettui l’operazione di conteggio in tempo $\Large \Theta(n)$ dove n è il numero di elementi presenti nella lista.

Dell’algoritmo proposto

---

**a)** si dia la descrizione a parole

Si scorre ricorsivamente una sola volta tutta la lista, controllando ogni volta se il valore del campo *val* del record corrente è pari, tenendone traccia usando le chiamate ricorsive.

**b)** si scriva lo pseudocodice,

```python
def es3(L):
    if L == None:
        return 0
    if L.val % 2 == 0:
        return 1 + es3(L.next)
    return es3(L.next)
```

**c)** si giustifichi il costo computazionale risolvendo la ricorsione che viene fuori dall’algoritmo utilizzando uno dei metodi di soluzione visti a lezione.

Si rientrerà nel caso base quando $\Large L = None$, ovvero quando la lungezza della lista sarà uguale a 0, con relativo costo $\Large \Theta(1)$.

$$
    \Large -T(n) = \Theta(1), \quad n = 0
$$

Il costo del caso generale, invece, sarà determinato dalle 2 chiamate ricorsive.

Entrambe le chiamate ricorsive presentano lo stesso parametro e ad ogni iterazione ne verrà eseguita solo una tra le 2 (a seconda del valore del campo *val* del record corrente), si può dire che il costo totale delle chiamate ricorsive sia $\Large T(n-1)$.

L'equazione di ricorrenza sarà data da

$$
    \Large -T(n) = T(n-1) + \Theta(1), \quad n \geq 1
$$

$$
    \Large -T(n) = \Theta(1), \quad n = 0
$$

Si decide di risolvere la ricorrenza usando il metodo iterativo, sviluppando la ricorrenza

$$
    \Large T(n) = T(n-1) + \Theta(1)
$$

$$
    \Large T(n) = T(n-2) + \Theta(1) + \Theta(1)
$$

$$
    \Large T(n) = T(n-3) + \Theta(1) + \Theta(1)\ + \Theta(1)
$$

generalizzabile in

$$
    \Large T(n) = T(n-k) + k\Theta(1)
$$

Il caso base verrà raggiunto quando

$$
    \Large n - k = 0
$$

$$
    \Large k = n
$$

il costo della funzione sarà uguale a

$$
    \Large T(n) = T(n-n) + n\Theta(1)
$$

$$
    \Large T(n) = T(0) + \Theta(n)
$$

$$
    \Large T(n) = \Theta(1) + \Theta(n)
$$

$$
    \Large T(n) = \Theta(n)
$$



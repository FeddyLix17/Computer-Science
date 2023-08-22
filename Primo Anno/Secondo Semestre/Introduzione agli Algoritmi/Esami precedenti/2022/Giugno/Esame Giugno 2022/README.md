# <p align="center"> Esame Giugno 2022 </p>

## <p align="center"> Esercizio 1 </p>

Per la soluzione di un certo problema disponiamo di un algoritmo iterativo con costo computazionale $\Large \Theta(n^2)$.

Ci viene proposto in alternativa un algoritmo ricorsivo il cui costo è catturato dalla seguente ricorrenza:

$$
    \Large T(n) = a * T(\frac{n}{4}) + \Theta(1), \quad n \geq 4
$$

$$
    \Large T(n) = \Theta(1) \quad \text{altrimenti}
$$

Dove a è una certa costante intera positiva con $\Large a \geq 2$.

Determinare qual'è il valore massimo che la costante intera a può avere perchè l’algoritmo ricorsivo risulti asintoticamente più efficiente dell’algoritmo iterativo di cui disponiamo. **Motivare bene la vostra risposta**.

---

Generalizzando la ricorrenza in $\Large T(n) = a * T(\frac{n}{b}) + f(n)$,

vengono individuati $\Large b = 4\ \text{e}\ \Large f(n) = \Theta(1)$.

$\Large n^{\log_b(a)}$ sarà uguale a $\Large n^{\log_4(a)}$.

Per ogni $\Large 0 < \epsilon <\log_4(a)$, si rientrerà nel primo caso del metodo principale (ovvero quello in cui $\Large f(n)$ sia in $\Large O(n^{\log_b(a) - \epsilon})$ ), con costo $\Large \Theta(n^{\log_4(a)})$.

Fino a quando $\Large n^{\log_4(a)} < n^2$, l'algoritmo ricorsivo sarà asintoticamente più efficiente di quello iterativo.

$$
    \Large n^{\log_4(a)} < n^2
$$

$$
    \Large \log_4(a) < 2
$$

$$
    \Large a < 4^2
$$

$$
    \Large a < 16
$$

Il valore massimo che la costante intera *a* potrà assumere affinchè l’algoritmo ricorsivo risulti asintoticamente più efficiente dell’algoritmo iterativo sarà 15.

---

## <p align="center"> Esercizio 2 </p>

Sia *A* un array di *n* interi.

Con la coppia ordinata $(i, j),\ 0 < i < j < n,$ rappresentiamo il suo sottoarray che parte dall’elemento in posizione *i* e termina con l’elemento in posizione *j*, deﬁniamo valore di un sottoarray come la somma dei suoi elementi.

Progettare un algoritmo che, dato un array A di interi positivi ed un intero positivo *s*, restituisce la coppia ordinata che rappresenta il sottoarray di *A* più a sinistra che ha valore *s*.

Se un tale sottoarray non esiste, la funzione deve restituire *None*.

L’algoritmo deve avere costo computazionale $O(n)$.

Ad esempio, per *A = [1, 3, 5, 2, 9, 3, 3, 1, 6]*

- con *s = 7* l’algoritmo deve restituire la coppia $(2, 3)$ (ci sono infatti in A tre sottoarray con valore 7 le cui coppie nell’ordine da sinistra a destra sono $(2, 3), (5, 7), (7, 8)$).

- con *s = 21* l’algoritmo deve restituire *None* in quanto *A* non ha sottoarray con valore 21.

Dell’algoritmo proposto:

---

**a)** si dia la descrizione a parole;

Si utilizzano due indici *i* e *j* per tenere traccia dei 2 estremi del sottoarray corrente ed una variabile *somma* per tenere traccia della somma tra tutti i suoi elementi.

Partendo dal sottoarray più a sinistra (ovvero quello composto solamente dal primo elemento dell'array), si procederà secondo la seguente logica:

- viene calcolata la somma del sottoarray corrente

- se la somma corrente è minore di *s*, si incrementa *j* di 1 in modo da aggiungere un nuovo elemento al sottoarray corrente

- se la somma corrente è maggiore di *s*, l'indice *i* verrà incrementato fino a quando la somma del sottoarray risultante non tornerà ad essere minore di *s*

- se la somma corrente è uguale a *s*, si restituisce la coppia ordinata $(i, j)$ (se non dovesse venire trovata nessuna somma uguale a *s*, verrá restituito *None*)

---

**b)** si scriva lo pseudocodice;

```python
def es2(A, s):
    i = 0
    j = 0
    somma = 0
    while j < len(A):
        somma += A[j]
        while somma > s:
            somma -= A[i]
            i += 1
        if somma == s:
            return (i, j)
        j += 1
    return None
```

---

**c)** si giustiﬁchi il costo computazionale.

Ad ogni iterazione dei due cicli while, viene incrementato di 1+ almeno uno dei due indici *i* e *j*.

Nel caso peggiore in cui non venga trovata alcuna somma uguale a *s*, entrambi gli indici verranno incrementati fino a raggiungere la lunghezza dell'array *A*, per un totale di $\Large 2n$ iterazioni, da cui costo computazionale 

$$
    \Large O(2n) \implies O(n)
$$

---

## <p align="center"> Esercizio 3 </p>

Si consideri una lista concatenata dove ogni nodo ha 2 campi,

- il campo *key* contenente un intero

- ed il campo *next* con il puntatore al nodo seguente (*next* vale *None* per l’ultimo nodo della lista).

Bisogna aggiornare i puntatori della lista in modo da creare una nuova lista
priva dei nodi con valore superiore a 10 e in cui i nodi rimanenti appaiono in ordine inverso rispetto all’originale.

Ad esempio per la lista di seguito a sinistra la funzione deve restituire la lista di seguito a destra:

             11 --> 10 --> 3 --> 7 --> 11 --> 12 --> 4 --> 15         4 --> 7 --> 3 --> 10

Progettare un algoritmo che, dato il puntatore *p* alla testa della lista, risolve il problema in tempo $\Theta(n)$ dove n è il numero di nodi della lista originaria.

Lo spazio di lavoro dell’algoritmo proposto deve essere $\Theta(1)$ (in altri termini non è possibile deﬁnire e utilizzare altre liste o nodi).

Dell’algoritmo proposto:

---

**a)** si dia la descrizione a parole

Viene inizializzato un puntatore *q* il quale, al termine della funzione, punterà alla testa della nuova lista.

Iterando la lista originaria, per ogni nodo

- se la sua chiave ha valore superiore a 10, lo si "elimina" facendo puntare il nodo precedente al successivo del nodo corrente

- altrimenti, lo si inserisce alla testa della lista punta da *q* nel seguente modo:

    - si salva il puntatore al nodo successivo del nodo corrente in una variabile temporanea *t*

    - si fa puntare il nodo successivo del nodo corrente a *q*

    - si fa puntare *q* al nodo corrente

    - si fa puntare il nodo corrente a *t* (ovvero al suo nodo successivo che era stato salvato in precedenza)

> per quanto possa sembrare confusionario, si può ottenere una rappresentazione visiva di quanto descritto usando strumenti come [python tutor](http://pythontutor.com/visualize.html#mode=edit)

Al termine della funzione, *q* punterà alla testa della nuova lista e verrà restituito come valore di ritorno.

---

**b)** si scriva lo pseudocodice

```python
def es3(p):
    q = None
    while p != None:
        if p.key > 10:
            p = p.next
    else:
        t = p.next
        p.next = q
        q = p
        p = t
    return q
```

---

**c)** si giustiﬁchi il costo computazionale

Viene visitata una sola volta tutta la lista, da cui il costo computazionale $\Large \Theta(n)$.

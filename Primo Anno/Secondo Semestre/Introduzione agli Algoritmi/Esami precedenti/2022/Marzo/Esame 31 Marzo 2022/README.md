# <p align="center"> Esame 31 Marzo 2022 </p>

## Esercizio 1

Si consideri la seguente funzione:

```python
def Exam(n):
    tot = 1
    if n <= 1:
        return tot
    j = 63
    while j > 0:
        k = 0
        while 3 * k <= n:
            k = k + 1
        tot = tot + 2 * Exam(k)
        j = j − 7
    while k > 0:
        for i in range(1, n):
            tot = tot − 1
        k = k − 1
return tot
```

**a)** Si imposti la relazione di ricorrenza che ne definisce il tempo di esecuzione giustificando dettagliatamente l’equazione ottenuta

si analizza ogni blocco di codice separatamente

il caso base sarà raggiunto quando $\Large n \leq 1$ con conseguente costo $\Large \Theta(1)$, da cui 

$$
    \Large T(n) = \Theta(1), \quad n \leq 1
$$

il costo del caso generale è invece determinato principalmente dai 3 cicli while e la chiamata ricorsiva annidata tra uno di essi

- **primo while**

    il ciclo inizia con $\Large j = 63$, si analizza il suo comportamento dopo ogni iterazione

<div align="center">

| iterazione | $0$ | $1$ | $2$ | $3$ | $\dots$ | $z$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\Large j$ | $63$ | $56$ | $49$ | $42$ | $\dots$ | $7*z$ |

</div>

il ciclo terminerà quando

$$
    \Large 7z = 0
$$

$$
    \Large z = \frac{63}{7} = 9
$$

il costo sarà dunque $\Large \Theta(9) \implies \Theta(1)$


---

- **secondo while**

    *premessa*: il numero di volte che questo ciclo si ripeterà andrà moltiplicato per $9$ in quanto è annidato al primo ciclo

    questo ciclo inizierà sempre con $\Large k = 0$, si analizza il suo comportamento dopo ogni iterazione

<div align="center">

| iterazione | $0$ | $1$ | $2$ | $3$ | $\dots$ | $z$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\Large k$ | $0$ | $1$ | $2$ | $3$ | $\dots$ | z |
| $\Large 3k$ | $0$ | $3$ | $6$ | $9$ | $\dots$ | $3z$ |

</div>

il ciclo terminerà quando

$$
    \Large 3z = n
$$

$$
    \Large z = \frac{n}{3}
$$

il costo sarà dunque $\Large \Theta(9*\frac{n}{3}) \implies \Theta(n)$

***nota***: subito dopo essersi concluso questo ciclo, avverrà una chiamata ricorsiva, avente come parametro $\Large k = z = \frac{n}{3}$, e considerando che il primo ciclo while si ripeterà $\Large 9$ volte, il costo totale della chiamata ricorsiva da andare a sommare al costo degli altri cicli while sarà $\Large 9T(\frac{n}{3})$

---

- **terzo while**

    il ciclo inizierà con $\Large k = \frac{n}{3}$, si analizza il suo comportamento dopo ogni iterazione

<div align="center">

| iterazione | $0$ | $1$ | $2$ | $3$ | $\dots$ | $z$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\Large k$ | $\frac{n}{3}$ | $\frac{n}{3}-1$ | $\frac{n}{3}-2$ | $\frac{n}{3}-3$ | $\dots$ | $\frac{n}{3}-z$ |

</div>

il ciclo terminerà quando

$$
    \Large \frac{n}{3}-z = 0
$$

$$
    \Large z = \frac{n}{3}
$$

il costo sarà dunque $\Large \Theta(\frac{n}{3})$

in quest'ultimo ciclo while tuttavia è presente un ciclo for annidato, il quale eseguirà $\Large n-1$ iterazioni, con costo $\Large \Theta(n-1) \implies \Theta(n)$, quindi possiamo affermare che per $\Large \frac{n}{3}$ volte verrano eseguite $\Large n-1$ iterazioni, da cui il nuovo costo di quest'ultimo ciclo while

$$
    \Large \frac{n}{3}\Theta(n-1) \implies \frac{n}{3}\Theta(n) \implies \Theta(\frac{n^2}{3}) \implies \Theta(n^2)
$$

analizzati tutti i blocchi di codice, possiamo affermare che il costo totale del caso generale sia

$$
    \Large T(n) = 9T(\frac{n}{3}) + \Theta(n^2) + \Theta(n) \implies T(n) = 9T(\frac{n}{3}) + \Theta(n^2)
$$

che unito al caso base darà come equazione di ricorrenza finale

$$
    \Large -T(n) = 9T(\frac{n}{3}) + \Theta(n^2), \quad n > 1
$$

$$
    \Large -T(n) = \Theta(1), \quad n \leq 1
$$

**b)** Si risolva la ricorrenza usando il metodo dell’albero dettagliando i
passaggi del calcolo e giustificando ogni affermazione

> per questioni di spazio qui a schermo, a differenza degli altri walkthrough in cui sviluppavo l'albero in modo grafico, in questo caso riporterò semplicemente il tutto in modo tabellare, al fine comunque di rimanere il più chiaro possibile

<div align="center">

| livello | costo | nodi | costo totale |
| :---: | :---: | :---: | :---: |
| $0$ | $\Large \Theta(n^2)$ | $1$ | $\Large \Theta(n^2)$ |
| $1$ | $\Large \Theta(\frac{n^2}{3})$ | $9$ | $\Large 9\Theta(n^2)$ |
| $2$ | $\Large \Theta(\frac{n^2}{9})$ | $81$ | $\Large 81\Theta(n^2)$ |
| $3$ | $\Large \Theta(\frac{n^2}{27})$ | $729$ | $\Large 729\Theta(n^2)$ |
| $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| $\Large z$ | $\Large \Theta(\frac{n^2}{3^z})$ | $\Large 3^z$ | $\Large 3^{2z}\Theta(n^2)$ |
</div>

l'albero si fermerà quando

$$
    \Large \frac{n^2}{3^{2z}} = 1
$$

$$
    \Large n^2 = 3^{2z}
$$

$$
    \Large \sqrt{n^2} = \sqrt{3^{2z}}
$$

$$
    \Large n = 3^z
$$

$$
    \Large \log_3(n) = z \implies z = \log_3(n)
$$

il costo totale sarà dunque dato dal costo di ogni livello $(\Large \Theta(n^2))$ moltiplicato per il numero dei livelli $(\Large \log_3(n))$

$$
    \Large \Theta(n^2)\log_3(n) \implies \Theta(n^2\log(n))
$$

## Esercizio 2

Dato un array ordinato $A$ di $n$ interi ed un intero $k$
vogliamo sapere quante coppie in $A$ hanno somma $k$.

Si progetti un algoritmo iterativo che risolva il problema in tempo $\Theta(n)$.

Ad esempio:

- se $A = [1, 2, 2, 3, 4, 5, 5, 5, 8, 9, 9]$ e $k = 7$ l’algoritmo deve restituire 7 (le coppie a somma 7 sono infatti (1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7) e (3, 4)).

- se $A = [1, 5, 5, 5, 9]$ e $k = 10$ l’algoritmo deve restituire 4 (le coppie a
somma 10 sono infatti (0, 4), (1, 2), (1, 3), (2, 3)).

Dell’algoritmo proposto:

**a)** si dia la descrizione a parole

Vengono inizializzati il contatore delle coppie count e due indici a e b i quali punteranno rispettivamente ai 2 estremi dell’array.

Succesivamente, fino a quando i due indici non punteranno allo stesso elemento,
vengono effettuati i seguenti controlli:

- se la somma degli elementi puntati è superiore a k, decremento l’indice b

- se invece la somma degli elementi puntati è inferiore a k, incremento l’indice a

- altrimenti, nel caso in cui la somma degli elementi puntati sia uguale a k, bisognerà verificare l'eventuale presenza di altre coppie uguali a quella trovata ma con indici in posizioni diverse, poiché l’array oltre ad essere ordinato potrebbe presentare dei duplicati

- l'indice b viene decrementato ﬁno a raggiungere un elemento diverso (inferiore) da quello attualmente puntato, o comunque fino raggiungere l'elemento successivo a quello puntato dall'indice a.

- e l'indice a viene incrementato ﬁno a raggiungere un elemento diverso (maggiore) di quello attualmente puntato, o comunque fino raggiungere l'elemento precedente a quello puntato dall'indice b.

viene tenuta traccia del numero di incrementi/decrementi effettuati mediante delle variabili ausiliarie x e y.

- Se la coppia trovata inizialmente presenta gli elementi al loro interno uguali, bisognerà calcolare il numero di [combinazioni](https://www.youmath.it/lezioni/probabilita/calcolo-combinatorio/1216-combinazione-semplice.html) di 2 elementi presi da un insieme contenente x + 1 elementi, ovvero dal numero di decrementi + l'elemento corrente. <br> In questo caso y sarà sempre uguale a 1 quindi l'insieme sarà composto da x + y elementi. <br> Dunque bisognerà incrementrare count di $\Large {x+y \choose 2}$ <br> dove con $\Large {x+y \choose 2}$ si intende

$$
    \Large \frac{(x + y)!}{2!(x + y - 2)!}
$$

$$
    \Large \frac{(x + y)(x + y - 1) (x + y - 2)!}{2(x + y - 2)!}
$$

$$
    \Large \frac{(x + y)(x + y - 1)}{2}
$$

ad esempio, in un ipotetico array [1, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6] con k = 4, la coppia  di elementi uguali (1, 6) viene anche trovata

- con (1,5), (1,4), (1,3), (1,2)

- con (2,6), (2,5), (2,4), (2,3)

- con (3,6), (3,5), (3,4)

- con (4,6), (4,5)

- con (5,6)

per un totale di 14 coppie uguali a quella puntata da a e b inizialmente (che aggiunte alla coppia iniziale fanno 15 coppie uguali), ovvero ci sono altri x = 5 elementi uguali a quello puntato da b (lo precedono).

y in questo caso sarà sempre uguale a 1, poiché nonostante a non venga proprio incrementato (perché punta da subito all'elemento precedente a quello puntato da b), come detto prima, nell'insieme di cui bisognerà calcolare le combinazioni, bisogna considerare anche l'elemento corrente.

riprendendo la formula

$$
    \Large \frac{(5 + 1)(5 + 1 - 1)}{2} = \frac{6 \cdot 5}{2} = 15
$$

- altrimenti, se la coppia trovata aveva elementi diversi, count verrà incrementato di $\Large x * y$, poichè

    - per ogni incremento di a, ci saranno b combinazioni da conteggiare

    - o per ogni decremento di b, ci saranno a combinazioni da conteggiare

entrambe le espressioni hanno lo stesso significato (si può usare quella che si preferisce).

riprendendo l'array di esempio fornito dall'esercizio [1, 2, 2, 3, 4, 5, 5, 5, 8, 9, 9], con k = 7, viene trovata come prima coppia (1, 7), stavolta con gli elementi al loro interno diversi.

La stessa coppia viene trovata anche in

- (1, 6), (1, 5)

- (2, 7), (2, 6), (2, 5)

per un totale di 5 coppie uguali a quella puntata da a e b (che aggiunte alla coppia iniziale fanno 6 coppie uguali)

ciò viene conteggiato da b che è stato decrementato di $x = 3$ volte e da a che è stato incrementato di $y = 2$ volte, da cui

$$
    \Large x * y = 3 * 2 = 6
$$

viene infine ritornato il valore di count.

**b)** si scriva lo pseudocodice

```python
def es2(A, k):
    a = 0
    b = len(A) - 1
    count = 0
    while a < b:
        if A[a] + A[b] > k:
            b -= 1
        elif A[a] + A[b] < k:
            a += 1
        else:
            x = 1
            while b - 1 > a and A[b-1] == A[b]:
                x += 1
                b -= 1
            y = 1
            while a + 1 < b and A[a+1] == A[a]:
                y += 1
                a += 1
            if A[a] == A[b]:
                count += (x + y) * (x + y - 1) / 2
            else:
                count += x * y
            a += 1
            b -= 1
    return count
```

**c)** si giustifichi il costo computazionale

si analizzano caso peggiore e caso migliore

- **caso peggiore**: l'array è composto da soli elementi uguali, quindi verranno eseguiti n - 1 decrementi/iterazioni prima di ritornare il valore di count, con costo computazionale pari a

$$
    \Large O(n - 1) \implies O(n)
$$

- **caso migliore**: l'array è composto da soli elementi diversi, quindi verranno eseguiti $\Large \frac{n - 1}{2}$ decrementi e $\Large \frac{n - 1}{2}$ incrementi, per un totale di n iterazioni prima di ritornare il valore di count, con costo computazionale pari a

$$
    \Large \Omega(n)
$$

dato che la funzione è sia in $\Large O(n)$ che in $\Large \Omega(n)$, il suo costo computazionale sarà pari a $\Large \Theta(n)$

## Esercizio 3

Si consideri una lista a puntatori *L*, in cui ogni elemento è un record a tre campi:

- il campo *val* contenente un bit (cioè un valore 0 o 1)

- il campo *next* con il puntatore al nodo seguente (next vale *None* per l’ultimo record della lista)

- ed il campo *prec* con il puntatore al nodo precedente (prec vale *None* per il primo record della lista).

Bisogna verificare se la stringa che si ottiene considerando i bit dei vari nodi della lista è palindroma.

Ad esempio, se la lista *L* in input è quella di sinistra nella figura che segue, la risposta è NO (la stringa binaria 010110 non è palindroma), mentre se *L* è la lista di destra la risposta è SI (la stringa binaria
11011 è palindroma).

                            -------------->                                 -------------->
                             ╱╲ ╱╲ ╱╲ ╱╲ ╱╲                                  ╱╲ ╱╲ ╱╲ ╱╲
                            0  1  0  1  1  0                                1  1  0  1  1
                             ╲╱ ╲╱ ╲╱ ╲╱ ╲╱                                  ╲╱ ╲╱ ╲╱ ╲╱
                            <--------------                                 <--------------

Progettare un algoritmo (iterativo o ricorsivo) che, dato il puntatore *s* alla testa della lista, risolve il problema in tempo $\Theta(n)$, dove *n* è il numero di nodi della lista a puntatori.

Lo spazio di lavoro dell’algoritmo proposto deve essere $O(1)$ (in altri termini NON è possibile definire e utilizzare altre liste).

Dell’algoritmo proposto:

**a)** si dia la descrizione a parole

Viene iterata una prima volta la lista in modo da poter ricavare il puntatore all'ultimo elemento della lista, denominato sotto una variabile ausiliaria *d*.

Cosi facendo si ottengono 2 puntatori rispettivamente all'estremo sinistro e destro della lista.

Viene visitata la lista da entrambe le estremità finchè

- i 2 puntatori puntano a nodi diversi

- i valori dei nodi puntati dai 2 puntatori sono uguali

- il nodo successivo al nodo puntato dal puntatore sinistro è diverso al nodo puntato dal puntatore destro

> la terza condizione potrebbe anche essere sostituita con "il nodo precedente al nodo puntato dal puntatore destro è diverso al nodo puntato dal puntatore sinistro"

ritornando *SI* se dovessere venire violata la prima o la terza condizione, *NO* se dovessere venire violata la seconda.

**b)** si scriva lo pseudocodice

```python
def es3(s):
    d = s

    while d.next != None:
        d = d.next

    while True:
        if s == d:
            return "SI"

        if s.val != d.val:
            return "NO"

        if s.next == d:
            return "SI"

        s = s.next
        d = d.prec
```

**c)** si giustifichi il costo computazionale

- il primo ciclo while viene eseguito n volte, con costo computazionale pari a $\Large \Theta(n)$

- il secondo ciclo while viene eseguito al massimo $\Large \frac{n}{2}$ volte, con costo computazionale pari a $\Large \Theta(\frac{n}{2}) \implies \Theta(n)$

dunque il costo computazionale della funzione sarà pari a $\Large \Theta(n) + \Theta(n) \implies \Theta(n)$

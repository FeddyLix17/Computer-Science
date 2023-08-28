# <p align="center"> Esame 25 Ottobre 2022 </p>

## <p align="center"> Esercizio 1 </p>

Si consideri la seguente funzione:

```python
def es1(n):
    if n <= 1:
        return 5
    a = es1(n/2)
    i = j = 1
    while j < n:
        j*= 2
        i+= 1
    u, j = 1, n
    while j > 1:
        j-= i
        u+= 1
    return a + es1(n/2) + u
```

---

**a)** Si imposti la relazione di ricorrenza che ne definisce il tempo di esecuzione giustificando dettagliatamente l’equazione ottenuta.

Per impostare la relazione di ricorrenza, si analizza il codice

- il caso base verrà raggiunto quando $\Large n <= 1$, con equivalente costo $\Large \Theta(1)$

- altrimenti, il costo del caso generale sarà dato da:

    - il costo delle 2 chiamate ricorsive, ciascuna con parametro $\Large \frac{n}{2}$, corrispondente a $\Large 2T(\frac{n}{2})$

    - il costo dei 2 cicli while, entrambi con sole istruzioni elementari al loro interno ma con condizioni di uscita differenti.

Si analizzano il comportamento di questi ultimi al fine di determinarne il costo

- **Primo ciclo while**

<div align="center">

| iterazione | $0$ | $1$ | $2$ | $3$ | $\dots$ | $k$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $j$ | $1$ | $2$ | $4$ | $8$ | $\dots$ | $2^k$ |
| $i$ | $1$ | $2$ | $3$ | $4$ | $\dots$ | $k+1$ |

</div>

il ciclo terminerà quando

$$
    \Large j = n
$$

$$
    \Large 2^k = n
$$

$$
    \Large k = \log_2(n)
$$

il costo del primo ciclo while sarà dunque $\Large \Theta(\log(n))$

**nota**: si è tenuto traccia anche del valore di $\Large i$ $\Large (k+1 = \log(n)+ 1)$ in quanto sarà determinante per il secondo ciclo while

- **Secondo ciclo while**

<div align="center">

| iterazione | $0$ | $1$ | $2$ | $3$ | $\dots$ | $k$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $j$ | $n$ | $n - i$ | $n - 2i$ | $n - 3i$ | $\dots$ | $n - k*i$ |

</div>

Il ciclo terminerà quando

$$
    \Large j = 1
$$

$$
    \Large n - k*i = 1
$$

$$
    \Large -k*i = -n + 1
$$

$$
    \Large k*i = n - 1
$$

$$
    \Large k = \frac{n - 1}{i}
$$

ricordando che $\Large i = log_2(n) + 1$ si ottiene

$$
    \Large k = \frac{n - 1}{log_2(n) + 1}
$$

il costo del secondo ciclo while sarà dunque

$$
    \Large \Theta(\frac{n - 1}{log_2(n) + 1}) \implies \Large \Theta(\frac{n}{log_2(n)})
$$

è facilmente dimostrabile come $\Large \frac{n}{log_2(n)}$, per valori molto grandi di $\Large n$, sia strettamente maggiore di $\Large \log_2(n)$

<div align="center">

| $n$ | $20$ | $100$ | $200$ | $1000$ | $2000$ |
| :---: | :---: | :---: | :---: | :---: | :---: | 
| $\frac{n}{log_2(n)}$ | $4.6$ | $15$ | $26$ | $100$ | $182$ |
| $\log_2(n)$ | 4.3 | 6.6 | 7.6 | 9.9 | 10.9 |

</div>

dunque il costo del primo ciclo while, essendo strettamente minore del secondo, può essere trascurato.

La relazione di ricorrenza finale sarà dunque

$$
    \Large -T(n) = 2T(\frac{n}{2}) + \Theta(\frac{n}{log_2(n)}), \quad n > 1
$$

$$
    \Large -T(n) = \Theta(1), \quad n \leq 1
$$

---

**b)** Qualora sia possibile, risolvere la ricorrenza utilizzando il teorema principale dettagliando il caso del teorema ed i passaggi logici.

Se il teorema principale non è applicabile spiegarne il motivo.

nella ricorrenza generica $\Large T(n) = aT(\frac{n}{b}) + f(n)$, si individuano

$\Large a = 2$, $\Large b = 2$, $\Large f(n) = \Theta(\frac{n}{log_2(n)})$ e $\Large n^{\log_b(a)} = n^{\log_2(2)} = n$

per verificare l'applicabilità del teorema principale, si analizzano tutti i casi

- **Caso 1**: 

    bisogna dimostrare se $\Large f(n)$ è in $\Large O(n^{1-\epsilon})$ per qualche $\Large \epsilon > 0$.

    Tuttavia, poiché $\Large \frac{n}{log_2(n)}$ cresce più velocemente di $\Large n^{1-\epsilon}$ per ogni $\Large \epsilon > 0$, il primo caso non può essere applicato.

---
- **Caso 2**:

    bisogna dimostrare se $\Large f(n)$ è in $\Large \Theta(n^{\log_b(a)})$

    Tuttavia, poiché $\Large \frac{n}{log_2(n)} \neq n^{\log_b(a)}$ , neanche il secondo caso può essere applicato.

---
- Caso 3:

    bisogna dimostrare se $\Large f(n)$ è in $\Large \Omega(n^{1+\epsilon})$ per qualche $\Large \epsilon > 0$.

    Tuttavia, poiché $\Large \frac{n}{log(n)}$ cresce più lentamente di $\Large n^{1+\epsilon}$ per ogni $\Large \epsilon > 0$, nemmeno il terzo caso può essere applicato.

si conclude dunque che il teorema principale non è applicabile per la seguente equazione di ricorrenza.

> per avere una dimostrazione grafica di quanto riportato sopra, si possono usare siti come [Geogebra](https://www.geogebra.org/calculator) o simili

<br>

## <p align="center"> Esercizio 2 </p>

Sia $A$ un array di $n$ elementi con $n$ pari, contenente uno stesso numero di interi pari ed interi dispari.

Un riarrangiamento degli interi in A è valido se nelle posizioni ad
indice pari compaiono interi pari e in quelle ad indice dispari interi dispari (l’indice 0 è considerato pari).

Ad esempio, per $A = [7, 3, 1, 8, 8, 2, 1, 4]$ esistono diversi riarrangiamenti validi come:

- $[8, 7, 2, 3, 8, 1, 4, 1]$

- oppure $[4, 1, 2, 1, 8, 3, 8, 7]$

- o anche $[2, 3, 8, 1, 8, 7, 4, 1]$

Progettare un algoritmo che, preso l’array $A$, produca un riarrangiamento valido.

L’algoritmo deve avere costo computazionale $O(n)$ e deve utilizzare uno spazio di lavoro costante (in altri termini, non è possibile utilizzare liste concatenate o array di appoggio).

Dell’algoritmo proposto:

---

**a)** si dia la descrizione a parole

Si utilizzano 2 indici, $\Large p$ e $\Large d$, per scorrere rispettivamente le posizioni pari e dispari dell'array, applicando il seguenti controlli:

- se il valore all'indice $p$ é pari, si proseguirà con la posizione pari successiva

- altrimenti, viene controllato se il all'indice $d$ è dispari, passando eventualmente a considerare la posizione dispari successiva in caso di riscontro

- altrimenti, si rientra nel caso in cui si hanno un valore pari in posizione dispari e un valore dispari in posizione pari, dunque si scambiano i valori contenuti in A[p] e A[d], e si passano ad esaminare le posizioni pari e dispari successive.

questi passaggi saranno ripetuti fino a quando non si raggiungerà la fine dell'array, ritornando così un riarrangiamento valido.

---

**b)** si scriva lo pseudocodice

```python
def es2(A):
    p = 0
    d = 1
    while p < len(A) and d < len(A):
        if A[p] % 2 == 0:
            p += 2
        elif A[d] % 2 == 1:
            d += 2
        else:
            A[p], A[d] = A[d], A[p]
            p += 2
            d += 2
    return A
```

---

**c)** si giustiﬁchi il costo computazionale

il costo dell'algoritmo è determinato principalmente dal ciclo while, in quanto le operazioni al suo interno e all'esterno sono tutte elementari

si analizzano caso peggiore e caso migliore

- **Caso migliore**:

    l'array è completamente disordinato, ovvero quando tutti gli elementi pari sono in posizioni dispari e tutti gli elementi dispari sono in posizioni pari, dunque il ciclo while terminerà verrà eseguito $\Large \frac{n}{2}$ volte ed il costo sarà $\Large \Omega(\frac{n}{2}) \implies \Omega(n)$

---

- **Caso peggiore**:

    l'array è completamente ordinato, ovvero quando tutti gli elementi pari sono in posizioni pari e tutti gli elementi dispari sono in posizioni dispari, dunque il ciclo while verrà eseguito $\Large 2 \frac{n}{2} \implies n$ volte ed il costo sarà $\Large O(n)$

si conclude dunque che il costo dell'algoritmo sia $\Large \Theta(n)$ rispettando i vincoli richiesti dall'esercizio.

<br>

## <p align="center"> Esercizio 3 </p>

Si consideri una lista a puntatori circolare $L$ data tramite un puntatore $p$ ad un suo elemento.

In $L$ ogni nodo ha $2$ campi:

- il campo $key$ contenente un intero

- ed il campo $next$ con il puntatore al nodo seguente.

Sappiamo che gli interi dei vari nodi sono tutti distinti e bisogna trovare il valore minimo tra questi.

Ad esempio per la lista circolare di seguito il valore cercato è 3:

                                    -->31 --> 10
                                      /         \
                                     /           \
                                    7            15
                                    ^             |
                                    |             |
                                    |             v
                                    9            12
                                     \          /
                                      \        /
                                       3 <-- 14

Progettare un algoritmo iterativo che, dato il puntatore $p$ ad un nodo della lista circolare, restituisce il valore cercato in tempo $\Theta(n)$ dove $n$ è il numero di nodi della lista.

Dell’algoritmo proposto:

---

**a)** si dia la descrizione a parole

si scorre l'intera lista utilizzando i campi $next$ di ogni nodo, confrontando il valore key di ogni nodo con il valore minimo trovato fino a quel momento, aggiornandolo se necessario e ritornandolo al termine dello scorrimento.

---

**b)** si scriva lo pseudocodice

```python
def es3(p):
    t = p.key
    minimo = p.key
    p = p.next
    while p.key != t:
        if p.key < minimo:
            minimo = p.key
        p = p.next
    return minimo
```

---

**c)** si giustiﬁchi il costo computazionale

il costo dell'algoritmo è determinato principalmente dal ciclo while, in quanto le operazioni al suo interno e all'esterno sono tutte elementari.

il ciclo while verrà eseguito $\Large n$ volte, dove $\Large n$ è la lunghezza della lista, in quanto terminerà quando si tornerà al nodo di partenza.

si conclude dunque che il costo dell'algoritmo sia $\Large \Theta(n)$

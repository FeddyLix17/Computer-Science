# <p align="center"> Esame 3 Marzo 2023 </p>

- ## Esercizio 1 (10 punti)
Si consideri il seguente algoritmo ricorsivo che, dato un array $A$ di dimensione
$n$, verifica se esistono due indici diversi $i$ e $j$ compresi nell’intervallo $[0, n − 1]$ tali
che $A[i] = j$ e $A[j] = i$:

```python
def IndiciValori(A, sx, dx):
    if (sx >= dx): return False     #Θ(1)
    else:
        trovato = False       
        centro = (sx + dx) / 2

        for i in range(sx, centro + 1): 
            for j in range(centro + 1, dx + 1):
                if (A[i] == j) and (A[j] == i): trovato = T rue

    trovato1 = IndiciValori(A, sx, centro)
    trovato2 = IndiciValori(A, centro + 1, dx)
    return trovato or trovato1 or trovato2
```

<b> a) </b> per impostare l'equazione di ricorrenza si analizza il codice

1. si hanno 2 chiamate ricorsive alla fine con parametro $n/2$
2. si analizzano attentamente i 2 cicli for annidati per determinarne il loro costo
- il primo ciclo for esegue ha un range che va da $sx$ a $centro$ e quindi esegue $centro - sx + 1$ iterazioni
- il secondo ciclo for esegue ha un range che va da $centro + 1$ a $dx$ e quindi esegue $dx - centro$ iterazioni

quindi il loro costo *teorico* è $\Theta( (centro - sx + 1) * (dx - centro))$ <br>
dal codice si nota come centro sia ugualmente a $\frac{sx + dx}{2}$, quindi il nuovo costo *teorico* diventa

$$ 
    \Theta( ( \frac{sx + dx}{2} - sx + 1) * (dx - \frac{sx + dx}{2}))
$$

$$
    \Theta( ( \frac{dx + sx -2sx}{2} + 1) * (\frac{- sx -dx + 2dx}{2}))
$$

$$
    \Theta( ( \frac{dx - sx}{2} + 1) * (\frac{dx - sx}{2}))
$$

intuendo dal codice che $dx$ indica la fine dell'array e $sx$ l'inizio, si può dire che la lunghezza n dell'array sarà data da $dx - sx + 1$ e quindi il costo *teorico* diventa

$$
    \Theta( ( \frac{n - 1 + 2 }{2}) * (\frac{n - 1}{2}))
$$

$$
    \Theta( \frac{n^2 + 1}{4} + \frac{n - 1}{2})
$$

$$
    \Theta( \frac{n^2 + 1}{4}) + \Theta(\frac{n -1}{2}) \implies \Theta(n^2) + \Theta(n) \implies \Theta(n^2)
$$

si conclude che il costo dei 2 cicli for annidati sia $\Theta(n^2)$.
L'equazione di ricorrenza sarà data dalla somma di tutti i costi trovati, quindi $T(n) = T(n/2) + T(n/2) + \Theta(n^2) \implies T(n) = 2T(n/2) + \Theta(n^2)$

con caso base $T(1) = \Theta(1)$ (ovvero quando $sx >= dx$ e quindi quanto il sub array ha dimensione 0)

$$
    \begin{cases}
        T(n) = 2T(n/2) + \Theta(n^2) \\
        T(1) = \Theta(1)
    \end{cases}
$$



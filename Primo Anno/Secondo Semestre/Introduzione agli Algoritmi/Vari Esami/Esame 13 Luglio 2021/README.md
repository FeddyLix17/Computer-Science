# <p align= "center"> Esame 13 Luglio 2021 </p>

- ## Esercizio 1 (10 punti)

Si consideri la seguente funzione:

```python
def Exam(n):
    if n <= 2: return 2 * n;                # Θ(1)
    b = n/2;                                # Θ(1)
    tot = n * n;                            # Θ(1)  
    for i in range(1, n + 1):               # Θ(n)
        for j in range(1, i + 1):           # Θ(n)
            tot = tot + i - j;              # Θ(1)
    for i = 1 to 4:                         # Θ(1)
        for j = 1 to 4:                     # Θ(1)
            if i = j: tot = tot + Exam(b)   # T(n/2)
            else: tot = tot + i - j;        # Θ(1)
    return tot                              # Θ(1)
```

**a)** per impostare la relazione di ricorrenza bisogna
analizzare i 3 blocchi distinti del codice.

1. quello in cui sono presenti tutte le istruzioni che hanno complessità costante, ovvero &Theta;(1)

2. quello in cui avviene la chiamata ricorsiva, che di per se ha un costo pari a $T(\frac{n}{2})$ , ma essendo eseguita 4 volte (solo quando $i=j$), avrà un costo pari a  $4T(\frac{n}{2})$

3. quello in cui avviene il doppio ciclo for, di cui bisogna analizzare il suo comportamento per determinarne il costo. <br>

- per $i = 1$, il ciclo for annidato viene eseguito 1 volte in quanto $j$ è già  uguale ad $i$
- per $i = 2$, il ciclo for interno viene eseguito 2 volte (una con $j=1$, una con $j=2$)
- per $i = 3$, il ciclo for interno viene eseguito 3 volte in quanto (una con $j=1$, una con $j=2$, una con $j=3$)
- per $i = n$, il ciclo for interno viene eseguito n volte in quanto una con $j=1$, una con $j=2$, una con $j=3$, $...$ , una con $j=n$)

quindi il costo dei 2 cicli for annidati è pari a 

$$ \sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \frac{n^2}{2} + \frac{n}{2} = \Theta(n^2) $$

quindi la relazione di ricorrenza è $T(n) = 4T(n/2) + \Theta(n^2) + \Theta(1)$

con caso base  $T(2) = \Theta(1)$


$$
    \begin{cases}
    T(n) = 4T(\frac{n}{2}) + \Theta(n^2) + \Theta(1) \\
    T(2) = \Theta(1)
    \end{cases}
$$

# <p align="center"> Esame 3 Marzo 2023 </p>

- ## Esercizio 1 (10 punti)

    Si consideri la seguente funzione:

```python
def Es1(n):
    if n < 10:                      #Θ(1)
        return n
    s = Es1(n / 2) * Es1(n / 2)     #2T(n/2)
    for j in range(n):              #Θ(n)
        k = n
        while k > 1:                #Θ(log_2(n))   
            s = s + 1
            k = k / 2
    return s + Es1(n / 2)           #T(n/2)
```

<b> a) </b>  per trovare l'equazione di ricorrenza che ne deﬁnisce il tempo di esecuzione, si analizza l'intero codice.

1. Le $3$ chiamate ricorsive hanno hanno come parametro $\frac{n}{2}$, quindi il loro tempo di esecuzione è $T(\frac{n}{2})$

2. Si analizzano separatamente prima il ciclo for e il ciclo while

- Il ciclo for viene eseguito $n$ volte, quindi il suo costo è $\Theta(n)$
- per determinare il costo del ciclo while, si analizza il suo comportamento ad ogni iterazione


| z | 0 | 1 | 2 | 3 | . . . |
| :-: | :-: | :-: | :-: | :-: | :-: |
| k | n | $\frac{n}{2}$ | $\frac{n}{4}$ | $\frac{n}{8}$ | $\frac{n}{2^z}$ |

sappiamo che il ciclo while terminerà quando $\frac{n}{2^z} = 1$, da cui

$$
    \frac{n}{2^z} = 1 \implies
    n = 2^z \implies
    \log_2(n) = z
$$


si conclude che il costo del ciclo while è $ \Theta(\log_2(n))$ <br>
che moltiplicato per il costo del ciclo for, si ottiene un costo totale pari a $\Theta(n\log_2(n))$ <br>
L'equazione di ricorrenza quindi sarà data da

$$
    T(n) = T(\frac{n}{2}) + T(\frac{n}{2}) + T(\frac{n}{2}) + \Theta(n\log_2(n)) \implies
    T(n) = 3T(\frac{n}{2}) + \Theta(n\log_2(n))
$$

aggiunta al caso base $T(1) = \Theta(1)$ 

$$
    \begin{cases}
    T(n) = 3T(\frac{n}{2}) + \Theta(n\log_2(n)) \\
    T(1) = \Theta(1)
    \end{cases}
$$

<b> b) </b> si prova a risolvere l'equazione di ricorrenza con il metodo principale

si generalizza l'equazione in

$$
    \begin{cases}
    T(n) = aT(\frac{n}{b}) + f(n) \\
    T(1) = \Theta(1)
    \end{cases}
$$

dove $a = 3$, $b = 2$ e $f(n) = \Theta(n\log_2(n))$ <br>

bisogna dimostrare che $\Theta(n\log_2(n)) è\ in\ O(n^{\log_2(3) - \epsilon})$ con $\epsilon > 0$ <br>

innanzitutto si ha che $\log_2(3) \approx 1.585$ <br>  
quindi bisognerà dimostrare che $\Theta(n\log_2(n)) è\ in\ O(n^{1.585 - \epsilon})$ <br>
si sceglie $\epsilon = 0.085$ <br>
quindi rimane da dimostrare che $\Theta(n\log_2(n)) è\ in\ O(n^{1.5})$ <br>


| n | 1 | 2 | 3 | 10 | 20 | 30 | 100 | 200 | 300 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| $\log_2(n)$ | 0 | 1 | 1.6 | 3.3 | 4.3 | 4.2 | 6.7 | 7.7 | 8.2 |
| $n\log_2(n)$ | 0 | 2 | 4.7 | 33.2 | 86.4 | 147.3 | 664 | 1528 | 2469 |
| $n^{1.5}$ | 1 | 2.8 | 5.2 | 31.6 | 89.4 | 164.3 | 1000 | 2828 | 5196 |

da cui 

$$
    \lim_{n \to \infty} \frac{n^{1.5}}{n\log_2(n)} = +\infty
$$

dimostrato che $n^{1.5}$ cresce più velocemente di $n\log_2(n)$, quindi dimostrato che $\Theta(n\log_2(n)) è\ in\ O(n^{1.5})$ <br>
si ricade nel primo caso del teorema principale con soluzione $T(n) = \Theta(n^{\log_2(3)}) \approx \Theta(n)$ <br>

- ## Esercizio 2 (10 punti)

Dato un array $A$ di $n$ interi non negativi distinti, si vuole determinare se esistono almeno tre numeri consecutivi di valore inferiore a 100. <br>
Ad esempio, se $A = [101, 5, 9, 31, 33, 10, 100, 4, 8, 32, 500, 11, 99]$, gli elementi $8$, $9$
e $10$ così come gli elementi $31$, $32$ e $33$ rispettano la proprietà mentre $99$, $100$ e
$101$ no. <br>
Progettare un algoritmo che, dato $A$, in tempo $\Theta(n)$ restituisce il valore dell’elemento centrale della terna se questa è presente, −1 altrimenti. <br>
Se esistono più terne allora bisogna restituire l’elemento centrale di valore massimo (nell’esempio
sopra, l’algoritmo dovrebbe restituire $32$; se nell’array ci fossero $4$ numeri consecutivi andrebbe restituito il terzo, ad esempio se l’array contenesse soltanto $5$, $6$,
$7$ e $8$, andrebbe restituito il $7$)


<b> a) </b> si scriva lo pseudocodice opportunamente commentato

```python
def trova_terna(A): # Prendo in input un array A di interi non negativi distinti

    # imposto inizialmente il centro della terna a -1 
    # in quanto è ciò che la funzione dovrà restituire se non trova nessuna terna
    centro_terna = -1

    # itero l'intero array confrontando ogni terna di elementi consecutivi possibile
    for i in range(1, len(A) - 1):
        # se trovo una terna con tutti e tre gli elementi minori di 100
        # imposto il valore da restiture come il valore maggiore 
        # tra il suo valore attuale e l'elemento centrale della terna
        if A[i-1] < 100 and A[i] < 100 and A[i+1] < 100:
            centro_terna = max(centro_terna, A[i])

    return centro_terna
```
**Nota:** nella traccia del compito ci viene fornito un array A di esempio ed il valore che la funzione dovrebbe ritornare <br>
ad esempio per l'array $A = [101, 5, 9, 31, 33, 10, 100, 4, 8, 32, 500, 11, 99]$ la funzione dovrebbe ritornare $32$ <br>
si nota come in questo array le sequenze di tre numeri consecutivi minori di 100 sono $[5, 9, 31]$ , $[9, 31, 33]$ , $[31, 33, 10]$ , $[4, 8, 32]$  <br>
con valori centrali rispettivamente $9$, $31$, $33$ ed $8$. <br>
il massimo tra questi valori è $33$ che è il valore che la funzione dovrà ritornare
a differenza del valore $32$ scritto nella traccia

<b> b) </b> il costo computazionale dell'algoritmo è $\Theta(n)$ in quanto vengono semplicemente iterati tutti gli elementi dell'array una sola volta e le operazioni che vengono effettuare su di essi hanno costo $\Theta(1)$

- ## Esercizio 3 (10 punti)

Un nodo di un albero a valori interi si dice nodo valido se la somma dei valori dei suoi antenati è uguale al valore del nodo. <br>
Ad esempio nell’albero binario in figura

                                                           0
                                                         /   \
                                                        /     \
                                                       2       5
                                                      / \     / \
                                                     /   \   /   \
                                                    1     7 6    -40
                                                         /        / 
                                                        /        /
                                                       9       -35


risultano validi $3$ nodi (quello con valore $0$, quello con valore $9$ e quello con valore $−35$). <br>
Dato il puntatore $r$ al nodo radice di un albero binario non vuoto, progettare un
algoritmo ricorsivo che in tempo $\Theta(n)$ calcoli il numero di nodi validi dell’albero. <br>
L’albero è memorizzato tramite puntatori e record a tre campi: <br>
il campo $key$ contenente il valore ed i campi $left$ e $right$ con i puntatori al figlio sinistro e al figlio destro, rispettivamente (questi puntatori valgono *None* in mancanza del
figlio).


<b> a) </b> si scriva lo pseudocodice opportunamente commentato

```python
def counter_nodi_validi(r, somma_antenati=0):   
    if r is None:                           # se mi trovo all'interno di una foglia
        return 0                            # ritorno 0 in quanto sono arrivato alla
                                            # fine di un percorso
    nodi_validi = 0                         # inizializzo il contatore dei nodi validi
    if somma_antenati == r.key:             # se la somma degli antenati è uguale al valore del nodo
        nodi_validi += 1                    # incremento il contatore dei nodi validi

    #chiamata ricorsiva sul figlio sinistro
    if r.left != None:
        nodi_validi += counter_nodi_validi(r.left, somma_antenati + r.key)

    #chiamata ricorsiva sul figlio destro
    if r.right != None:
        nodi_validi += counter_nodi_validi(r.right, somma_antenati + r.key)

    #ritorno ricorsivamente il numero di nodi validi
    return nodi_validi
```


<b> b) </b> sapendo solo che l'albero non è vuoto e che è binario (ma ad esempio non sapendo se è, completo, bilanciato, ecc.) bisognerà analizzare attentamente il codice per ricavare la sua equazione di ricorrenza. <br>
Dando una prima occhiata generale, si nota come l'argoritmo visiti l'albero in pre-order, dove

1. Nella prima parte di codice andiamo a visitare/efferruare operazioni sul nodo corrente 
il tutto in tempo $\Theta(1)$
2. Nella seconda parte di codice andiamo a visitare/efferruare operazioni sul figlio sinistro
(chiamando ricorsivamente la funzione su quest'ultimo).  Supponendo che il sotto albero sinistro sia composto da $k$ nodi, il costo della prima chiamata ricorsiva sarà $T(k)$
3. Nella terza parte di codice andiamo a visitare/efferruare operazioni sul figlio destro
(chiamando ricorsivamente la funzione su quest'ultimo). Per trovare il numero di nodi del sotto albero destro bisogna sottrarre al numero totale di nodi dell'albero (che è $n$) il numero di nodi del sotto albero sinistro (che è $k$) e il nodo corrente (che è $1$). Quindi, con numero di nodi del sotto albero destro uguale a $n - k - 1$, il costo della seconda chiamata ricorsiva sarà $T(n - k - 1)$.

Ricavati i costi dei vari blocchi di codice, l'equazione di ricorrenza generale sarà

$$
    T(n) = T(k) + T(n - k - 1) + \Theta(1)
$$

con caso base $T(0) = \Theta(1)$ (ovvero quando raggiungo una foglia)

$$
    \begin{cases}
    T(n) = T(k) + T(n - k - 1) + \Theta(1) \\
    T(0) = \Theta(1)
    \end{cases}
$$

sappiamo che le chiamate ricorsive terminano quando $n = 0$, il che ci può aiutare a semplificare la nostra equazione di ricorrenza. <br>

$$
    n - k - 1 = 0 \implies n - 1 = k \implies k = n - 1
$$

sostituendo $k$ nella nostra equazione di ricorrenza si ottiene

$$ T(n) = T(n - 1) + T(n - (n - 1) - 1) + \Theta(1) $$

$$ T(n) = T(n - 1) + T(n - n + 1 - 1) + \Theta(1) $$

$$ T(n) = T(n - 1) + T(0) + \Theta(1) $$

$$ T(n) = T(n - 1) + \Theta(1) + \Theta(1) $$

$$ T(n) = T(n - 1) + \Theta(1) $$

l'equazione di ricorrenza semplificata sarà $T(n) = T(n - 1) + \Theta(1)$ per $k = n - 1$ <br>

scegliendo un metodo a piacere (in quanto non ne è richiesto uno in particolare dalla traccia),
ad esempio quello iterativo, si analizza l'andamento dell'equazione dopo alcune chiamate ricorsive
(di cui indicheremo il numero con $z$)

$$ T(n) = T(n - 1) + \Theta(1) \iff per\ z=1 $$

$$ T(n) = [T(n - 2) + \Theta(1)] + \Theta(1) \iff  per\ z=2 $$

$$ T(n) = [T(n - 3) + \Theta(1) + \Theta(1)] + \Theta(1) \iff  per\ z=3 $$

la cui generalizzazione diventa $T(n) = T(n - z) + z\Theta(1) \implies T(n) = T(n - z) + \Theta(z)$ <br>

quindi per arrivare al caso base $T(0)$, bisognerà soddisfare la seguente condizione

$$
    n - z = 0 \implies n = z
$$

sostituendo $z$ nella nostra equazione di ricorrenza si ottiene

$$ T(n) = T(n - n) + \Theta(n) $$

$$ T(n) = T(0) + \Theta(n) $$

$$ T(n) = \Theta(1) + \Theta(n) $$

$$ T(n) = \Theta(n) $$

si conclude che il costo computazionale dell'algoritmo è $\Theta(n)$

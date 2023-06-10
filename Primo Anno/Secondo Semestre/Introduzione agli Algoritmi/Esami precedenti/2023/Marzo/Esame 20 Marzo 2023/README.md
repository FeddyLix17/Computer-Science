# <p align="center"> Esame 20 Marzo 2023 </p>

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

prima di scrivere lo pseudocodice, si fanno delle osservazioni sul problema

1. L'array è composto da interi non negativi distinti. Questa semplice frase ci da 2 informazioni che torneranno estremamente utili

    - Non ci sarà più di un occorenza di uno stesso numero all'interno dell'array
    - Non essendoci numeri negativi, e sapendo che quelli che ci interessano sono quelli **strettamente** minori di $100$

avendo un limite *teorico* del massimo valore che può essere contenuto nell'array, si può utilizzare un array di supporto per contare le occorrenze dei numeri che ci interessano (proprio come accadrebbe nel [Counting_Sort](https://www.programiz.com/dsa/counting-sort)), ovvero quelli **strettamente** minori di $100$ <br>

```python
def trova_max_terna(A):
    # Una prima differenza con il Counting_Sort è il ruolo dell'array di supporto.
    # Nell'algoritmo di ordinamento contiene il numero di occorrenze del numero 
    # corrispondente all'indice.
    # Nell'algoritmo di questo esercizio siccome sappiamo che ogni numero non compare più di una volta,
    # è come se l'array di appoggio fosse un array di booleani, dove se l'elemento è presente nell'array di partenza, 
    # l'indice dell'array di appoggio corrispondente sarà 1. 
    # Sempre nel nostro caso l'array di appoggio avrà dimensione 100, con gli indici che vanno da 0 a 99
    Conta_occorrenze = [0] * 100

    # Inizializzo la variabile che conterrà il valore dell'elemento centrale della terna a -1
    # in quanto se non dovessimo trovare nessuna terna che soddifà le proprietà richieste,
    # il valore da restituire deve essere -1
    max_terne = -1

    # Itero tutti gli elementi dell'array di partenza
    # e incremento di 1 l'indice corrispondente nell'array di appoggio
    # se l'elemento dell'array di partenza corrente è strettamente minore di 100
    for i in range(len(A)):
        if A[i] < 100:
            Conta_occorrenze[A[i]] += 1

    # Itero tutti gli elementi dell'array di appoggio
    # e se dovessimo trovare una terna di elementi consecutivi uguali a 1
    # ci basterà aggiornare la variabile max_terne con il valore massimo
    # tra il suo valore corrente e l'indice corrente del for
    for i in range(len(Conta_occorrenze) - 1):
        if Conta_occorrenze[i - 1] == 1 and Conta_occorrenze[i] == 1 and Conta_occorrenze[i + 1] == 1:
            max_terne = max(max_terne, i)

    # una volta iterati tutti gli elementi dell'array di appoggio
    # ritorno il valore di max_terne
    return max_terne
```

<b> b) </b> una cosa che non cambia rispetto al Counting_Sort è il costo computazionale dell'algoritmo, che rimane $\Theta(n + k)$, con $n$ numero di elementi dell'array di partenza e $k$ numero di elementi dell'array di appoggio, corrispondenti in questo caso al numero di elementi presenti nell'insieme [0, 99] (che è 100). Basta anche analizzare il codice per capire che il costo computazionale del primo ciclo for è $\Theta(n)$, mentre quello del secondo ciclo for è $\Theta(k)$. <br>
Conoscendo il valore di $k$, si può concludere che il costo computazionale dell'algoritmo è $\Theta(n + k) = \Theta(n + 100) = \Theta(n)$ 

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

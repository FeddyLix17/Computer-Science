# <p align="center"> Esame 8 Settembre 2021 </p>

- ## Esercizio 1 (10 punti)
    Si consideri la seguente funzione:

    ```python
    def Exam(n):
        tot = n                 # Θ(1)
        if n <= 4:              # Θ(1)   
            return tot
        b = n / 4               # Θ(1)
        tot += Exam(b)          # T(n/4)
        j = 1                   # Θ(1)
        while j * j <= n:       # Θ(√n)
            tot += j            # Θ(1)
            j += 1              # Θ(1)
        return tot + Exam(b)    # T(n/4)
    ```

    - <b> a) </b> Si imposti la relazione di ricorrenza che ne 
    definisce il tempo di esecuzione giustificando l’equazione ottenuta.

        per trovare l'equazione di ricorrenza che ne deﬁnisce il tempo di esecuzione,
        bisogna analizzare il costo di ogni istruzione/blocco di codice.

        - La somma di tutte le istruzioni con tempo di esecuzione Θ(1) è 6Θ(1) (costo che potremmo successivamente omettere dalla relazione di ricorrenza finale)
        - Le due chiamate ricorsive hanno hanno come parametro b, 
        che è pari a $\frac{n}{4}$, quindi il loro tempo di esecuzione è T($\frac{n}{4}$)
        - Il ciclo while ha come condizione di uscita j * j ≤ n,
        quindi per uscire $j^2$ dovrà essere uguale a $n + 1$, <br> ad ogni iterazione,
        etichettata con la lettera k, si nota la seguente relazione
            <center>

            | k | 0 | 1 | 2 | 3 | . . . |
            | :-: | :-: | :-: | :-: | :-: | :-: |
            | j | 1 | 2 | 3 | 4 | k + 1 |
            | j<sup>2</sup> |  1 | 4 | 9 | 16 | (k + 1)<sup>2</sup> |

            </center>
                s'imposta l'equazione

            $$  (k + 1)^2 = n + 1 $$

            e risolvendola

            $$ k + 1 = \sqrt{n + 1} $$
            $$ k = \sqrt{n + 1} - 1 $$
            $$ k \approx \sqrt{n} $$ 
            si conclude che il costo del ciclo while è Θ(√n)

            Il costo del caso peggiore sarà quindi

            $$ T(n) = T(\frac{n}{4}) + T(\frac{n}{4}) + Θ(\sqrt n) + 6Θ(1) = 2T(\frac{n}{4}) + Θ(\sqrt n) + Θ(1) $$

            che messo a sistema al costo del caso migliore, o anche meglio chiamato caso base,
            verificato quando n ≤ 4, si ottiene
            $$
            \begin{cases}
            T(n) = 2T(\frac{n}{4}) + Θ(\sqrt n) + Θ(1) \\
            T(4) = Θ(1)
            \end{cases}
            $$

    - <b> b) </b> Si risolva l’equazione usando il metodo dell’albero, dettagliando i passaggi del calcolo e giustiﬁcando ogni affermazione.
    <br> Ricavata l'equazione di ricorrenza nel punto a), si risolve con il metodo dell'albero

        <center>

            T(n)
            /      \
            /        \
            /          \
            T(n/4)        T(n/4)
            /      \      /      \
            /        \    /        \
            /          \  /          \
            T(n/16)    ... ...       ...
        </center>

        che può essere rappresentato anche come

        <center>

            Θ(√n) + Θ(1)
            /      \
            /        \
            /          \
            Θ(√n/4) + Θ(1)   Θ(√n/4) + Θ(1)
            /          \      /      \
            /            \    /        \
            /              \  /          \
            Θ(√n/16) + Θ(1)   ... ...       ...
        </center>
        si nota che

        - al livello 0, il costo è Θ(√n) + Θ(1)
            - al livello 1, il costo di un nodo è Θ(√n/4) + Θ(1) mentre il costo totale del livello è 2Θ(√n/4) + 2Θ(1)
            - al livello 2, il costo di un nodo è Θ(√n/16) + Θ(1) mentre il costo totale del livello è 4Θ(√n/16) + 4Θ(1)
            - al livello k, il costo di un nodo è Θ(√n/4<sup>k</sup>) + Θ(1) mentre il costo totale del livello è 2<sup>k</sup> (Θ(√n/4<sup>k</sup>) +
            Θ(1))
            $$ 2^k(\Theta(\sqrt\frac{n}{4^k}) + \Theta(1)) $$
            $$ 2^k(\sqrt\frac{n}{4^k} + 1) $$
            $$ 2^k(\frac{\sqrt n}{2^k} + 1) $$
            $$ \sqrt n + 2^k $$
            $$ \Theta(\sqrt n) + \Theta(2^k) = \Theta(\sqrt{n} 2^k) $$
        - al livello 0 di sono 2<sup>0</sup> nodi
            - al livello 1, ci sono 2<sup>1</sup> nodi
            - al livello 2, ci sono 2<sup>2</sup> nodi
            - al livello k, ci saranno 2<sup>k</sup> nodi

        per trovare l'esatto numero di livelli in relazione a n, s'imposta  l'equazione 
        $$ \frac{n}{4^k} = 4 $$
        $$ n = 4^k * 4 $$
        $$ n = 4^{k + 1} $$
        $$ \log_4(n) = k + 1 $$
        $$ \log_4(n) - 1 = k $$
        $$ k = \log_4(n) - 1 $$



        si conclude che il numero di livelli è $\log_4(n) - 1$.
    <br> per trovare il costo totale dell'albero, si sommano i costi di tutti i livelli
    $$ \sum_{i=0}^{\log_4(n) - 1} \Theta(\sqrt{n} 2^i) $$
    $$ \sum_{i=0}^{\log_4(n) - 1} \sqrt{n} * 2^i $$
    $$ \sqrt{n} \sum_{i=0}^{\log_4(n) - 1} 2^i $$
    sapendo che la sommatoria notevole di

    $$ \sum_{i=0}^{n} r^i = \frac{1 - r^{n + 1}}{1 - r} $$
    si ha
    $$ \sum_{i=0}^{\log_4(n) - 1} 2^i = \frac{1 - 2^{\log_4(n) - 1 + 1}}{1 - 2} $$
    $$ \sqrt{n} (\frac{1 - 2^{\log_4(n)}}{-1})  $$
    $$ \sqrt{n} (\frac{-1 + 2^{\log_4(n)}}{1})  $$
    $$ \sqrt{n} (2^{\log_4(n)}-1)  $$
    $$ \sqrt{n}2^{\log_4(n)} - \sqrt{n} $$
    $$ \sqrt{n} \sqrt{n} - \sqrt{n} $$
    $$ n - \sqrt{n} $$
    $$ \Theta(n) - \Theta(\sqrt{n}) $$
    $$ \Theta(n) $$

    **Nota:**
    nel pdf originale il risultato è $\Theta(\sqrt{n}log(n))$, per verificare se stiamo
    sbagliando noi o il pdf, si prova a risolvere la stessa equazione con il metodo iterativo

    riprendendo l'equazione di ricorrenza
    $$
            \begin{cases}
            T(n) = 2T(\frac{n}{4}) + \Theta(\sqrt n) + \Theta(1) \\
            T(4) = Θ(1)
            \end{cases}
            $$
    sviluppandola, si ottiene
    $$ T(n) = 2T(\frac{n}{4}) + \Theta(\sqrt n) + \Theta(1) $$
    $$ T(n) = 2[2T(\frac{n}{4^2}) + \Theta(\sqrt \frac{n}{4}) + \Theta(1)] + \Theta(\sqrt n) + \Theta(1) $$
    $$ T(n) = 2[2[2T(\frac{n}{4^3}) + Θ(\sqrt\frac{n}{4^2}) + Θ(1)] + Θ(\frac{\sqrt n}{4}) + Θ(1)] + Θ(\sqrt n) + Θ(1) $$
    $$ T(n) = 2^kT(\frac{n}{4^k}) + \sum_{i=0}^{k - 1} 2^i * (Θ(\sqrt\frac{n}{4^i}) + \Theta(1))$$

    avendo k = $\log_4(n) - 1$, ricavato in precedenza, si ottiene

    $$ T(n) = 2^{\log_4(n) - 1}T(\frac{n}{4^{\log_4(n) - 1}}) + \sum_{i=0}^{\log_4(n) - 2} 2^i * (Θ(\sqrt\frac{n}{4^i}) + \Theta(1)) $$
    $$ \frac{\sqrt n}{2}T(\frac{n}{4^{\log_4(n) - 1}}) + \sum_{i=0}^{\log_4(n) - 1} 2^i * \sqrt\frac{n}{4^i} + 1 $$
    $$ \frac{\sqrt n}{2}T(\frac{n}{\frac{1}{4}n}) +  \sqrt n \sum_{i=0}^{\log_4(n) - 1} \frac{2^i}{\sqrt{4^i}} + 2^i $$
    $$ \frac{\sqrt n}{2}T(4) +  \sqrt n \sum_{i=0}^{\log_4(n) - 1} \frac{2^i}{2^i} + 2^i $$
    $$ \frac{\sqrt n}{2}Θ(1) +  \sqrt n \sum_{i=0}^{\log_4(n) - 1} 1 + 2^i $$
    $$ \frac{\sqrt n}{2} +  \sqrt n \sum_{i=0}^{\log_4(n) - 1} 1 + \sqrt n \sum_{i=0}^{\log_4(n) - 1} 2^i $$
    $$ \frac{\sqrt n}{2} +  \sqrt n (\log_4(n) - 1) + \sqrt n \sum_{i=0}^{\log_4(n) - 1} 2^i $$
    $$ \frac{\sqrt n}{2} +  \sqrt n (\log_4(n) - 1) + \sqrt n \frac{1 - 2^{\log_4(n)}}{-1} $$
    $$ \frac{\sqrt n}{2} +  \sqrt n (\log_4(n) - 1) + \sqrt n \frac{-1 + \sqrt{n}}{1} $$
    $$ \frac{\sqrt n}{2} +  \sqrt n (\log_4(n) - 1) - \sqrt n + n $$
    $$ \frac{\sqrt n}{2} +  \sqrt n \log_4(n) - \sqrt n - \sqrt n + n $$
    $$ \frac{\sqrt n}{2} +  \frac{\sqrt n \log_2(n)}{2} - 2\sqrt n + n $$
    $$ \frac{\sqrt n + \sqrt n \log_2(n) - 4\sqrt n + 2n}{2} $$
    $$ \frac{\sqrt n \log_2(n) - 3\sqrt n + 2n}{2} $$
    $$ \Theta(\sqrt n \log_2(n)) - \Theta(\sqrt n) + \Theta(n) $$
    $$ \Theta(n) $$

- ## Esercizio 2 (10 punti)
    Progettare un algoritmo che, dati tre array *A*, *B* e *C* ordinati e contenenti ciascuno *n* interi distinti, stampi in tempo *O(n)* gli interi che compaiono nell’intersezione dei tre array. <br>
    L’algoritmo proposto deve utilizzare spazio    di
    lavoro $\Theta(1)$. <br>
    Ad esempio: <br>
    per *A = [1, 2, 3, 4, 5, 6]*, *B = [1, 4, 5, 6, 8, 9]* e *C = [2, 4,     6, 7, 8, 9]* l’algoritmo deve stampare gli elementi *4* e *6*.
    Dell’algoritmo proposto:
    - <b> a) </b> si dia la descrizione a parole

        L'algoritmo da proggettare è una variante dell'algoritmo di intersezione tra due array ordinati,  che sfrutta il fatto che gli array sono ordinati per scorrerli in modo lineare. <br>
        Si sfrutta la proprietà di intersezione tra due array ordinati, 
        ovvero che se l'elemento di un array è maggiore dell'elemento dell'altro array ad uno stesso indice, allora l'elemento dell'altro array non sarà sicuramente nell'intersezione. <br>
        Bisogna riadattare questa proprietà per tre array, usando un terzo indice per scorrere il terzo array. <br>
        
        - Si inizializzano tre indici, i, j e k, che corrispondono rispettivamente agli indici di A, B e C, a 0.
        - Vengono confrontati inizialmente solo gli elementi di A e B in quanto basta che anche un solo elemento sia diverso per non essere nell'intersezione. <br>
        Nel caso in cui A[i] == B[j], viene confrontato anche C[k] e se anche lui è uguale, allora si stampa l'elemento e si incrementano tutti gli indici, altrimenti viene sempre incrementato solo l'indice dell'array che contiene l'elemento minore. <br>
        In questo modo anche se i 3 indici saranno uguali solo inizialmente non si corre il rischio
        di saltare un elemento che potrebbe essere nell'intersezione.
        - Vengono ripetuti questi confronti con gli indici aggiornati man mano fino a quando uno degli indici supera la lunghezza dell'array.
    

    - <b> b) </b> si scriva lo pseudocodice
    
        ```python
        def intersezione(A, B, C):
            i = 0           #Θ(1)
            j = 0           #Θ(1)
            k = 0           #Θ(1)
            while i < len(A) and j < len(B) and k < len(C):   #Θ(n)
                if A[i] == B[j]:            #Θ(1)
                    if A[i] == C[k]:        #Θ(1)
                        print(A[i])         
                        i += 1              
                        j += 1              
                        k += 1              
                else:                       #Θ(1)
                    minimo = min(A[i], B[j], C[k])      #Θ(1)
                    if minimo == A[i]:                  #Θ(1)
                        i += 1                         
                    elif minimo == B[j]:                #Θ(1)
                        j += 1
                    else:                               #Θ(1)
                        k += 1
        ```
    - <b> c) </b> si giustifichi formalmente il costo computazionale

        Praticamente tutte le istruzioni a eccezione del ciclo while hanno costo Θ(1), per determinare il costo effettivo si analizza quindi il costo del ciclo while. <br>
        
        - Il caso migliore si verifica quando tutti e 3 gli array sono identici, quindi il ciclo while viene eseguito n volte, dove n è la lunghezza di un array, e il costo totale sarà $\Omega(n)$
        - Il caso peggiore si verifica quando gli array non hanno nessun elemento in comune tra tutti e 3, ma sapendo che ad ogni iterazione almeno un indice viene incrementato, si deduce che il ciclo while verrà eseguito al massimo 3n volte, quindi il costo totale sarà $O(3n)$ = $O(n)$

        Per definizione delle notazioni asintotiche ,se una funzione *f(n)* è sia in *Ω(n)* che in *O(n)*, allora sarà anche in *Θ(n)*, quindi il costo computazionale dell'algoritmo è $\Theta(n)$
        ed utilizza uno spazio di lavoro pari a $\Theta(1)$ in quanto lavora sugli array in input senza crearne di nuovi usando solo 3 indici.

    - <b> d) </b> si dia un’idea di quello che accadrebbe al costo computazionale se si
    volesse generalizzarlo a Θ(n) array <br>

        Se si volesse generalizzare l’algoritmo per trovare l’intersezione di Θ(n) array ordinati di lunghezza n, chiaramente il costo computazionale aumenterebbe. <br>
        In questo caso, l’algoritmo avrebbe bisogno di Θ(n) indici, e ad ogni iterazione del ciclo while dovrebbe confrontare Θ(n) valori per trovarne il minimo o comunque per verificare se tutti gli elementi di quella iterazioni sono uguali o meno, aumentando il costo di ogni iterazione del ciclo while da Θ(1) a Θ(n). <br> In conclusione 

        - il caso migliore avrebbe costo $\Omega(n^2)$ in quanto dovremmo confrontare per n volte n elementi uguali
        - il caso peggiore avrebbe costo $O(n^3)$ in quanto dovremmo confrontare per n volte n elementi diversi, quindi n<sup>2</sup> volte per trovare il minimo aggiungte agli n controlli per trovare quale indice incrementare


- ## Esercizio 3 (10 punti)
    Si consideri un albero binario radicato *T* , i cui nodi hanno un campo valore
    contenente un intero. <br>
    Bisogna modiﬁcare l’albero in modo che i nodi fratelli scambino tra loro il valore. <br>
    Si consideri ad esempio l’albero *T* in ﬁgura a sinistra, a destra viene riportato il risultato della modiﬁca di *T*. <br>
    Progettare un algoritmo che, dato il puntatore *r* alla radice di *T* memorizzato tramite record e puntatori, effettui l’operazione di modiﬁca in tempo *O(n)* dove *n* è il numero di nodi presenti nell’albero. <br>
    Ogni nodo dell’albero è memorizzato in un record contenente il campo val con il valore del nodo e i campi *left* e *right* con i puntatori ai ﬁgli di sinistra e destra, rispettivamente.

                            5                                                           5
                           / \                                                         / \            
                          /   \                                                       /   \
                         6     2                                                     2     6
                              / \                                                         / \
                             /   \                                                       /   \
                            4     3                                                     3     4
                           /     / \                                                   /     / \
                          /     /   \                                                 /     /   \
                         5     1     4                                               5     4     1

    - <b> a) </b> si dia la descrizione a parole <br>
        L'algoritmo *scambia_fratelli* prende come input il puntatore *r* alla radice dell'albero binario radicato *T*. <br> L'algoritmo è ricorsivo e si basa sul fatto che se un nodo ha entrambi i figli, allora scambia i valori dei figli e richiama ricorsivamente la funzione 
        prima sul figlio sinistro e poi sul figlio destro. <br>
        L'algoritmo termina quando si è visitato tutto l'albero
    
    - <b> b) </b> si scriva lo pseudocodice
        ```python
        def scambia_fratelli(r):
            if r.left:
                scambia_fratelli(r.left)

            if r.right:
                scambia_fratelli(r.right)

            if r.left and r.right:
                r.left.val, r.right.val = r.right.val, r.left.v
        ```

    - <b> c) </b> si giustifichi formalmente il costo computazionale <br>
    il costo computazionale dell'algoritmo è $\Theta(n)$ in quanto vengono
    semplicemente visitati tutti i nodi dell'albero una sola volta (in postorder) e le operazioni
    che vengono effettuare su di essi hanno costo Θ(1)

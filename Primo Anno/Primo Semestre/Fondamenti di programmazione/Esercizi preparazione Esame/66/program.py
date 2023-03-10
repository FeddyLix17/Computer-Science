import albero


def es66_ric(tree, livello, spostamento, listadelsium):
    if isinstance(tree, list):
        listadelsium.add(spostamento)
        if tree[1]:
            es66_ric(tree[1], livello - 1, spostamento-1, listadelsium)
        if tree[2]:
            es66_ric(tree[2], livello - 1, spostamento+1, listadelsium)

def es66(tree):
    """
    Es  17: 9 punti - ricorsivo

    Si definisca la funzione es66, ricorsiva (o che fa uso di vostre funzioni ricorsive) che:
    - riceve come argomento un AlberoBinario (definito nel file albero.py)

    Calcola la "larghezza massima" dell'albero,  ovvero la differenza tra 
    la livello del nodo che si trova piu' a destra nell'albero
    e la livello del nodo che si trova piu' a sinistra.
    Per calcolare la livello di un nodo rispetto alla radice (che assumiamo sia a livello 0)
    basta sottrarre 1 (uno) ogni volta che si scende su un sottoalbero sinistro
    ed aggiungere 1 (uno) ogni volta che si scende su un sottoalbero destro.
    Esempio: se l'albero e' quello qui sotto a sinistra le posizioni saranno quelle nell'albero a destra
             1           .            0         .
            / \          .           / \        .
           2   3         .         -1   1       .
          / \            .        /  \          .
        4    5           .      -2    0         .
       /    /            .      /    /          .
      6    7             .    -3    -1          .
       \    \            .      \    \          .
        8    9           .      -2    0         .
    Il nodo piu' a sinistra (6) e' a livello -3
    mentre quello piu' a destra (3) e' a livello 1
    Quindi la funzione torna il valore 4=1-(-3)
    """
    tree = tree.toList()
    aoao = set()
    es66_ric(tree, 0, 0, aoao)
    
    return max(aoao) - min(aoao)

if __name__ == "__main__":
    lista = [1, [2, None, None],
              [3, [4, None, None],
                [5, None, None],
              ],
            ]
    #     1
    #    2  3
    #  - - 4 5
    tree = albero.AlberoBinario.fromList(lista)
    es66(tree)

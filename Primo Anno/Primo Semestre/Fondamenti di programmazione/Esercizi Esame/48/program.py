import albero


def do_recursive_stuff(tree, count):
  if isinstance(tree, list):
    if tree[1] and tree[2]:
      count.append(1)
    if tree[1]:
        do_recursive_stuff(tree[1],count)
    if tree[2]:
        do_recursive_stuff(tree[2], count)
  return count
def es48(tree):
    '''
    Si definisca la funzione es48(tree) ricorsiva (o che fa uso di funzioni o metodi ricorsive/i) che:
    - riceve come argomento 'tree' un  albero  formato da nodi di tipo
      AlberoBinario definito nella libreria albero.py allegata
    - calcola il numero di nodi che nell'albero hanno ESATTAMENTE due figli
    - torna come risultato il numero calcolato
    Esempio: se l'albero e':

             7
            /\
           1  3
          / \
        4    6
       /    /
      5    2
     /     \
    9       8

    Nell'albero ci sono solo due nodi con esattamente due figli (il nodo con valore 7 ed il nodo
    con valore 1) cosi'  la funzione tornera' il valore 2.
    '''
    print(tree.toList())
    result = []
    do_recursive_stuff(tree.toList(), result)
    return sum(result)
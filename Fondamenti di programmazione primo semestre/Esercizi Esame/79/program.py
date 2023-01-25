

def es79_recursion(lista, result):
    if lista == []:
        return
    if type(lista[0]) == list:
        es79_recursion(lista[0], result)
    else:
        result[0] += 1
        result[1] += lista[0]
        result[2].append(lista[0])
    es79_recursion(lista[1:], result)
    result[2] = list(set(result[2]))
    result[2].sort()
    print(f"result[0] = {result[0]}")
    print(f"result[1] = {result[1]}")
    print(f"result[2] = {result[2]}")
    return tuple(result)


def modify_es79_list(lista):
    for i in range(len(lista)):
        if type(lista[i]) == list:
            lista[i] = modify_es79_list(lista[i])
    print(f"lista in modify = {lista}")
    return lista[::-1]



def es79(lista):
    '''
    Si definisca la funzione ricorsiva (o che usa una vostra funzione ricorsiva) es79(lista).
    La funzione prende in input una lista che puo' essere vuota, contenere interi e/o altre liste del suo stesso tipo.
    Al termine della funzione la lista deve risultare invertita e lo stesso deve accadere 
    a tutte le liste in essa contenute, ricorsivamente.
    Inoltre la funzione restituisce una tupla di tre elementi.
    Al primo posto della tupla deve comparire il numero totale di interi presenti nella lista e nelle sue sottoliste. 
    Al secondo posto della tupla deve comparire la somma di tutti gli interi presenti nella lista e nelle sue sottoliste.
    Al terzo posto della tupla deve comparire la lista, ordinata in modo crescente, contenente una sola volta i
    differenti interi presenti nella lista e nelle sue sottoliste.
    Ad esempio, se all'inizio la lista e'
     lista = [3, 3, 5, [[1, 8, [9, 3]], 3, [2, [9, [5, 6],[9]] ] ]]
    alla fine la lista dev'essere
     lista = [[[[[9], [6, 5], 9], 2], 3, [[3, 9], 8, 1]], 5, 3, 3]
    la funzione es79(lista) restituisce la tupla 
    (13, 66, [1, 2, 3, 5, 6, 8, 9])
     ''' 
    lista = modify_es79_list(lista)
    result = es79_recursion(lista, [0, 0, []])
    return result

if __name__ == '__main__':
    lista = [3, 3, 5, [[1, 8, [9, 3]], 3, [2, [9, [5, 6],[9]] ] ]]
    print(es79(lista))
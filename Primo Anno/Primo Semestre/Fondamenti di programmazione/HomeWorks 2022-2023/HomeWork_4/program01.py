#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Obiettivo dello homework è leggere alcune stringhe contenute in una serie di
file e generare una nuova stringa a partire da tutte le stringhe lette.
Le stringhe da leggere sono contenute in diversi file, collegati fra loro a
formare una catena chiusa. Infatti, la prima stringa di ogni file è il nome di
un altro file che appartiene alla catena: partendo da un qualsiasi file e
seguendo la catena, si ritorna sempre nel file di partenza.

Esempio: il contenuto di "A.txt" inizia con "B.txt", il file "B.txt", inizia
con "C.txt" e il file "C.txt" inizia con "A.txt", formando la catena
"A.txt"-"B.txt"-"C.txt".

Oltre alla stringa con il nome del file successivo, ogni file contiene anche
altre stringhe separate da spazi, tabulazioni o caratteri di a capo. La
funzione deve leggere tutte le stringhe presenti nei file della catena e
costruire la stringa che si ottiene concatenando i caratteri con la più alta
frequenza in ogni posizione. Ovvero, nella stringa da costruire, alla
posizione p ci sarà il carattere che ha frequenza massima nella posizione p di
ogni stringa letta dai file. Nel caso in cui ci fossero più caratteri con
la stessa frequenza, si consideri l'ordine alfabetico.
La stringa da costruire ha lunghezza pari alla
lunghezza massima delle stringhe lette dai file.

Quindi, si deve scrivere una funzione che prende in ingresso una stringa A 
che rappresenta il nome di un file e restituisce una stringa.
La funzione deve costruire la stringa secondo le indicazioni illustrate sopra
e ritornare le stringa così costruita.

Esempio: se il contenuto dei tre file A.txt, B.txt e C.txt nella directory
test01 è il seguente

test01/A.txt          test01/B.txt         test01/C.txt                                                                 
-------------------------------------------------------------------------------
test01/B.txt          test01/C.txt         test01/A.txt
house                 home                 kite                                                                       
garden                park                 hello                                                                       
kitchen               affair               portrait                                                                     
balloon                                    angel                                                                                                                                               
                                           surfing                                                               

la funzione most_frequent_chars("test01/A.txt") dovrà restituire la stringa
"hareennt".
'''

def most_frequent_chars(filename: str) -> str:
    largetxt, a, txt, dicfreq, result = [], 0, open(filename, encoding="UTF-8", mode="r").read().split(), {}, ""
    largetxt.append(txt)
    while largetxt[a][0] != filename:
        txt = open(largetxt[a][0], encoding="UTF-8", mode="r").read().split()
        largetxt.append(txt)
        a += 1
    for x in range(len(largetxt)):
        for y in range(1,len(largetxt[x])):
            for z in range(len(largetxt[x][y])):
                if f"{largetxt[x][y][z]}{z}" in dicfreq.keys():
                    dicfreq[f"{largetxt[x][y][z]}{z}"] += 1
                else:
                    dicfreq[f"{largetxt[x][y][z]}{z}"] = 1
    dicfreq = {k: v for k, v in sorted(dicfreq.items(), key=lambda item: (int(item[0][1:]), -item[1], item[0][0]))}
    a = 0
    for key in dicfreq.keys():
        if key.endswith(str(a)):
            result += key[0]
            a += 1 
    return result
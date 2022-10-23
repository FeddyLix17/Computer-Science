# -*- coding: utf-8 -*-

''' 
Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)
'''

def ex1(int_seq, subtotal):
    start, end, risultati, zerodealer, int_seq = 0, 0, 0, 1, list(map(int, int_seq.replace(",", "")))
    min_length = float('inf')
    while end < len(int_seq):
        while sum(int_seq[start:end]) >= subtotal:
            if sum(int_seq[start:end]) == subtotal: risultati += 1
            min_length = min(min_length, end-start+1)
            if sum(int_seq[start:end + zerodealer]) > sum(int_seq[start:end]): 
                start += 1
                zerodealer = 1 
            else: zerodealer +=1
        end += 1
    return risultati
    #for startsec in range(len(int_seq)):
    #    for endsec in range(len(int_seq), startsec, -1):
    #        if sum(int_seq[startsec:endsec]) > subtotal or sum(int_seq[startsec:endsec]) < subtotal: continue
    #        elif sum(int_seq[startsec:endsec]) == subtotal: result += 1



if __name__ == '__main__':
    # Inserisci qui i tuoi test personali
    pass


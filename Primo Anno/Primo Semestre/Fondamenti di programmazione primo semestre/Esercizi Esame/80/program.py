

import os

def es80_rec(dir1, parole, profondita):
    for file in os.listdir(dir1):
        if os.path.isdir(f"{dir1}/{file}"):
            es80_rec(f"{dir1}/{file}", parole, profondita + 1)
        elif file.endswith('.txt'):
            with open(f"{dir1}/{file}", 'r') as f:
                for line in f:
                    for word in line.split():
                        if word in parole:
                            parole[word][0] += 1
                            if parole[word][1] < profondita:
                                parole[word][1] = profondita
                f.close()
    return parole 
def es80(dir1, parole):
    '''
    ATTENZIONE: usate come separatore dei file il carattere "/" che funziona sia in Windows che in Linux
    ATTENZIONE: e' VIETATO usare la funzione os.walk

    Si definisca la funzione  es80(dir1, parole), che presi in input:
        dir1:   il path di una directory
        parole: un insieme di parole (stringhe di caratteri tra 'a' e 'z')
    esegue il seguente lavoro:
    Ricerca nella directory il cui path e'  dir1 e nelle sue subdirectories eventuali file con estensione .txt contenenti
    stringhe appartenenti all'insieme delle parole e restituisce un dizionario delle parole trovate.
    Nel dizionario restituito devono comparire  solo le parole effettivamente riscontrate all'interno
    dei file con estensione .txt e ciascuna chiave deve avere  come attributo una lista  di due interi.
    Il primo elemento della lista riporta il numero complessivo di volte che la parola  e' stata ritrovata in questi file,
    il secondo elemento della lista riporta la profondita' massima dei file in cui la parola e' risultata presente.
    La profondita' dei file nella directory dir1 vale 0
    Per parola intendiamo una sequenza di lunghezza massimale di caratteri tra 'a' e 'z'.
    Si puo' assumere che tutti i file con estensione .txt contengono solo parole  separate da  spazi, tab o andate a capo.
    (non sono presenti caratteri maiuscoli o segni di interpunzione)
    '''
    #inserisci qui il tuo codice
    result = es80_rec(dir1, {word: [0, 0] for word in parole}, 0)
    for key in list(result.keys()):
        if result[key][0] == 0:
            del result[key]
    return result
if __name__ == '__main__':
    dir1 = input('Inserisci il path della directory: ')
    parole = set(input('Inserisci le parole da cercare: ').split())
    print(es80(dir1, parole))
